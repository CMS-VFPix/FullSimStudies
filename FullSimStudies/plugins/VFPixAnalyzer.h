#ifndef VFPIX_ANALYZER
#define VFPIX_ANALYZER

#include <unordered_map>
#include <string>

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "SimDataFormats/Track/interface/SimTrack.h"

#include "TH1D.h"
#include "TH2D.h"
#include "TH3D.h"

using namespace std;

class VFPixAnalyzer : public edm::EDAnalyzer
{
  public:
    VFPixAnalyzer (const edm::ParameterSet &);
    ~VFPixAnalyzer ();

    void analyze (const edm::Event &, const edm::EventSetup &);

  private:
    edm::Service<TFileService> fs_;
    unordered_map<string, TH1D *> oneDHists_;
    unordered_map<string, TH2D *> twoDHists_;
    unordered_map<string, TH3D *> threeDHists_;

    edm::InputTag jets_;
    edm::InputTag pus_;
    edm::InputTag vertices_;
    edm::InputTag tracks_;
    edm::InputTag genParticles_;
    edm::InputTag simTracks_;

    long long trackHash (const reco::Track &) const;
    void logSpace (const unsigned, const double, const double, vector<double> &) const;
    void linSpace (const unsigned, const double, const double, vector<double> &) const;
    bool isMatched (const reco::Track &, const edm::Handle<vector<reco::GenParticle> > &, const unsigned, const double, const reco::GenParticle *&) const;
    bool isMatched (const reco::Track &, const edm::Handle<vector<SimTrack> > &, const double, const SimTrack *&) const;
};

#endif
