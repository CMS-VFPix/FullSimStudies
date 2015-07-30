#include <iostream>

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include "VFPix/FullSimStudies/plugins/VBFQuarkProducer.h"

VBFQuarkProducer::VBFQuarkProducer (const edm::ParameterSet &cfg) :
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles")),
  jets_ (cfg.getParameter<edm::InputTag> ("jets")),
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks"))
{
  produces<vector<reco::GenParticle> > ("vbfQuarks");
  produces<vector<reco::PFJet> > ("vbfJets");
  produces<vector<reco::Track> > ("vbfJetsTracks");
}

VBFQuarkProducer::~VBFQuarkProducer ()
{
}

void
VBFQuarkProducer::produce (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);
  edm::Handle<vector<reco::PFJet> > jets;
  event.getByLabel (jets_, jets);
  edm::Handle<vector<reco::Track> > tracks;
  event.getByLabel (tracks_, tracks);

  auto_ptr<vector<reco::GenParticle> > vbfQuarks (new vector<reco::GenParticle> ());
  auto_ptr<vector<reco::PFJet> > vbfJets (new vector<reco::PFJet> ());
  auto_ptr<vector<reco::Track> > vbfJetsTracks (new vector<reco::Track> ());

  for (const auto &particle : *genParticles)
    {
      int status = particle.status (),
          pid = particle.pdgId ();

      bool isVBFquark = false ; 
      if ( status == 3 && abs(pid) < 10 && particle.numberOfMothers() > 0 ) { 
        for (unsigned int j=0; !isVBFquark && j<particle.numberOfMothers(); j++) {
          for (unsigned int k=0; k<particle.mother(j)->numberOfDaughters(); k++) {
            if ( abs(particle.mother(j)->daughter(k)->pdgId()) == 25 ) {
              isVBFquark = true ; break ;
            }
          }
        }
      }
      if (isVBFquark)
        vbfQuarks->push_back (particle);
    }
  for (const auto &quark : *vbfQuarks)
    {
      if (quark.pt () < 30.0)
        continue;

      const reco::PFJet *closestJet = NULL;
      double closestJetDeltaR = -1.0;
      for (const auto &jet : *jets)
        {
          double dR;

          if (jet.pt () < 30.0)
            continue;

          dR = deltaR (quark, jet);

          if (dR > 0.4)
            continue;

          if (dR < closestJetDeltaR || !closestJet)
            {
              closestJetDeltaR = dR;
              closestJet = &jet;
            }
        }
      if (!closestJet)
        continue;
      vbfJets->push_back (*closestJet);
    }
  for (const auto &track : *tracks)
    {
      if (track.pt () < 0.7)
        continue;
      if (track.normalizedChi2 () > 20.0)
        continue;
      if (track.hitPattern ().pixelLayersWithMeasurement () < 2)
        continue;
      if (track.hitPattern ().trackerLayersWithMeasurement () < 5)
        continue;
      if (fabs (track.d0 () / track.d0Error ()) > 5.0)
        continue;
      for (const auto &jet : *vbfJets)
        {
          if (deltaR (track, jet) > 0.4)
            continue;
          vbfJetsTracks->push_back (track);
        }
    }
  event.put (vbfQuarks, "vbfQuarks");
  event.put (vbfJets, "vbfJets");
  event.put (vbfJetsTracks, "vbfJetsTracks");
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(VBFQuarkProducer);
