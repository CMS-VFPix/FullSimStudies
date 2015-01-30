#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_set>

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "VFPix/FullSimStudies/plugins/VFPixAnalyzer.h"

VFPixAnalyzer::VFPixAnalyzer (const edm::ParameterSet &cfg) :
  jets_ (cfg.getParameter<edm::InputTag> ("jets")),
  pus_ (cfg.getParameter<edm::InputTag> ("pus")),
  vertices_ (cfg.getParameter<edm::InputTag> ("vertices")),
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks")),
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles"))
{
  vector<double> jetPtBins, trackPtBins, vertexPt2Bins, vertexTrackPtBins;
  double a = 0.0,
         b = 4.0,
         n = 1000.0,
         step = (b - a) / n;
  for (double i = a; i < b + 0.5 * step; i += step)
    jetPtBins.push_back (pow (10.0, i));
  a = -1.0, b = 1.0, n = 100.0, step = (b - a) / n;
  for (double i = a; i < b + 0.5 * step; i += step)
    trackPtBins.push_back (pow (10.0, i));
  a = -1.0, b = 8.0, n = 1000.0, step = (b - a) / n;
  for (double i = a; i < b + 0.5 * step; i += step)
    vertexPt2Bins.push_back (pow (10.0, i));
  a = -2.0, b = 2.0, n = 1000.0, step = (b - a) / n;
  for (double i = a; i < b + 0.5 * step; i += step)
    vertexTrackPtBins.push_back (pow (10.0, i));

  TH1::SetDefaultSumw2 ();
  TFileDirectory jetDir = fs_->mkdir ("jets"),
                 puDir = fs_->mkdir ("pu"),
                 vertexDir = fs_->mkdir ("vertices"),
                 trackDir = fs_->mkdir ("tracks");

  oneDHists_["jetEta"]   = jetDir.make<TH1D> ("jetEta", ";jet #eta", 1000, -5.0, 5.0);
  oneDHists_["jetPt"]    = jetDir.make<TH1D> ("jetPt", ";jet p_{T} [GeV]", jetPtBins.size () - 1, jetPtBins.data ());
  oneDHists_["jetBeta"]    = jetDir.make<TH1D> ("jetBeta", ";jet #beta", 1000, 0.0, 1.0);

  twoDHists_["jetBetaVsJetEta"]    = jetDir.make<TH2D> ("jetBetaVsJetEta", ";jet #eta;jet #beta", 500, -5.0, 5.0, 500, 0.0, 1.0);

  oneDHists_["nPU_bx0"]  = puDir.make<TH1D> ("nPU_bx0", ";number of interactions from current BX", 280, 0.0, 280.0);
  oneDHists_["nPU_bxP1"] = puDir.make<TH1D> ("nPU_bxP1", ";number of interactions from following BX", 280, 0.0, 280.0);
  oneDHists_["nPU_bxM1"] = puDir.make<TH1D> ("nPU_bxM1", ";number of interactions from previous BX", 280, 0.0, 280.0);
  oneDHists_["nPU"] = puDir.make<TH1D> ("nPU", ";number of interactions", 280, 0.0, 280.0);
  oneDHists_["nOOPU"] = puDir.make<TH1D> ("nOOPU", ";number of out-of-time interactions", 280, 0.0, 280.0);

  twoDHists_["nPUVsBX"] = puDir.make<TH2D> ("nPUVsBX", ";BX;number of interactions", 30, -15.0, 15.0, 280, 0.0, 280.0);

  oneDHists_["vertexX"] = vertexDir.make<TH1D> ("vertexX", ";vertex x [cm]", 1000, -1.0, 1.0);
  oneDHists_["vertexY"] = vertexDir.make<TH1D> ("vertexY", ";vertex y [cm]", 1000, -1.0, 1.0);
  oneDHists_["vertexZ"] = vertexDir.make<TH1D> ("vertexZ", ";vertex z [cm]", 1000, -30.0, 30.0);
  oneDHists_["vertexXError"] = vertexDir.make<TH1D> ("vertexXError", ";vertex #sigma_{x} [cm]", 1000, 0.0, 1.0);
  oneDHists_["vertexYError"] = vertexDir.make<TH1D> ("vertexYError", ";vertex #sigma_{y} [cm]", 1000, 0.0, 1.0);
  oneDHists_["vertexZError"] = vertexDir.make<TH1D> ("vertexZError", ";vertex #sigma_{z} [cm]", 1000, 0.0, 1.0);
  oneDHists_["vertexNDF"] = vertexDir.make<TH1D> ("vertexNDF", ";vertex NDF", 500, 0.0, 500.0);
  oneDHists_["vertexNTracks"] = vertexDir.make<TH1D> ("vertexNTracks", ";vertex number of tracks", 500, 0.0, 500.0);
  oneDHists_["vertexTrackPt"] = vertexDir.make<TH1D> ("vertexTrackPt", ";vertex track p_{T} [GeV}", vertexTrackPtBins.size () - 1, vertexTrackPtBins.data ());
  oneDHists_["vertexSumPt2"] = vertexDir.make<TH1D> ("vertexSumPt2", ";vertex #sump_{T}^{2} [GeV^{2}]", vertexPt2Bins.size () - 1, vertexPt2Bins.data ());
  oneDHists_["pvX"] = vertexDir.make<TH1D> ("pvX", ";primary vertex x [cm]", 1000, -1.0, 1.0);
  oneDHists_["pvY"] = vertexDir.make<TH1D> ("pvY", ";primary vertex y [cm]", 1000, -1.0, 1.0);
  oneDHists_["pvZ"] = vertexDir.make<TH1D> ("pvZ", ";primary vertex z [cm]", 1000, -30.0, 30.0);
  oneDHists_["pvXError"] = vertexDir.make<TH1D> ("pvXError", ";primary vertex #sigma_{x} [cm]", 1000, 0.0, 1.0);
  oneDHists_["pvYError"] = vertexDir.make<TH1D> ("pvYError", ";primary vertex #sigma_{y} [cm]", 1000, 0.0, 1.0);
  oneDHists_["pvZError"] = vertexDir.make<TH1D> ("pvZError", ";primary vertex #sigma_{z} [cm]", 1000, 0.0, 1.0);
  oneDHists_["pvDeltaX"] = vertexDir.make<TH1D> ("pvDeltaX", ";primary vertex x_{true} - x_{reco} [cm]", 1000, -1.0, 1.0);
  oneDHists_["pvDeltaY"] = vertexDir.make<TH1D> ("pvDeltaY", ";primary vertex y_{true} - y_{reco} [cm]", 1000, -1.0, 1.0);
  oneDHists_["pvDeltaZ"] = vertexDir.make<TH1D> ("pvDeltaZ", ";primary vertex z_{true} - z_{reco} [cm]", 1000, -1.0, 1.0);
  oneDHists_["pvNDF"] = vertexDir.make<TH1D> ("pvNDF", ";primary vertex NDF", 500, 0.0, 500.0);
  oneDHists_["pvNTracks"] = vertexDir.make<TH1D> ("pvNTracks", ";primary vertex number of tracks", 500, 0.0, 500.0);
  oneDHists_["pvTrackPt"] = vertexDir.make<TH1D> ("pvTrackPt", ";primary vertex track p_{T} [GeV}", vertexTrackPtBins.size () - 1, vertexTrackPtBins.data ());
  oneDHists_["pvSumPt2"] = vertexDir.make<TH1D> ("pvSumPt2", ";primary vertex #sump_{T}^{2} [GeV^{2}]", vertexPt2Bins.size () - 1, vertexPt2Bins.data ());

  twoDHists_["nVerticesVsNPU"] = vertexDir.make<TH2D> ("nVerticesVsNPU", ";number of interactions;number of primary vertices", 280, 0.0, 280.0, 280, 0.0, 280.0);

  twoDHists_["trackPtVsTrackZ"] = trackDir.make<TH2D> ("trackPtVsTrackZ", ";track z [cm];track p_{T} [GeV]", 1000, -15.0, 15.0, trackPtBins.size () - 1, trackPtBins.data ());
}

VFPixAnalyzer::~VFPixAnalyzer ()
{
}

void
VFPixAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::PFJet> > jets;
  event.getByLabel (jets_, jets);
  edm::Handle<vector<PileupSummaryInfo> > pus;
  event.getByLabel (pus_, pus);
  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByLabel (vertices_, vertices);
  edm::Handle<vector<reco::Track> > tracks;
  event.getByLabel (tracks_, tracks);
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);

  double nPU_bx0 = 0.0;
  for (const auto &pu : *pus)
    {
      int currentNPU = pu.getPU_NumInteractions (),
          currentBX = pu.getBunchCrossing ();

      oneDHists_.at ("nPU")->Fill (currentNPU);
      twoDHists_.at ("nPUVsBX")->Fill (currentBX, currentNPU);
      switch (currentBX)
        {
          case -1:
            oneDHists_.at ("nPU_bxM1")->Fill (currentNPU);
            oneDHists_.at ("nOOPU")->Fill (currentNPU);
            break;
          case 0:
            oneDHists_.at ("nPU_bx0")->Fill (currentNPU);
            nPU_bx0 = currentNPU;
            break;
          case 1:
            oneDHists_.at ("nPU_bxP1")->Fill (currentNPU);
            oneDHists_.at ("nOOPU")->Fill (currentNPU);
            break;
          default:
            oneDHists_.at ("nOOPU")->Fill (currentNPU);
        }
    }

  double nVertices = vertices->size (),
         pvTrueX = genParticles->at (2).vx (),
         pvTrueY = genParticles->at (2).vy (),
         pvTrueZ = genParticles->at (2).vz ();
  unordered_set<long long> pvTrackID;
  twoDHists_.at ("nVerticesVsNPU")->Fill (nPU_bx0, nVertices);
  if (nVertices > 0)
    {
      double x = vertices->at (0).x (),
             y = vertices->at (0).y (),
             z = vertices->at (0).z (),
             ex = vertices->at (0).xError (),
             ey = vertices->at (0).yError (),
             ez = vertices->at (0).zError (),
             sumPt2 = 0.0;
      int ndf = vertices->at (0).ndof (),
          nTracks = 0.0;

      oneDHists_.at ("pvX")->Fill (x);
      oneDHists_.at ("pvY")->Fill (y);
      oneDHists_.at ("pvZ")->Fill (z);
      oneDHists_.at ("pvXError")->Fill (ex);
      oneDHists_.at ("pvYError")->Fill (ey);
      oneDHists_.at ("pvZError")->Fill (ez);
      oneDHists_.at ("pvDeltaX")->Fill (pvTrueX - x);
      oneDHists_.at ("pvDeltaY")->Fill (pvTrueY - y);
      oneDHists_.at ("pvDeltaZ")->Fill (pvTrueZ - z);
      oneDHists_.at ("pvNDF")->Fill (ndf);

      for (auto track = vertices->at (0).tracks_begin (); track != vertices->at (0).tracks_end (); track++)
        {
          double pt = (*track)->pt ();
          long long id = trackHash (**track);

          if (pt < 0.7)
            continue;
          nTracks++;
          sumPt2 += pt * pt;
          pvTrackID.insert (id);
        }
      oneDHists_.at ("pvNTracks")->Fill (nTracks);
      oneDHists_.at ("pvSumPt2")->Fill (sumPt2);
    }
  for (const auto &vertex : *vertices)
    {
      double x = vertex.x (),
             y = vertex.y (),
             z = vertex.z (),
             ex = vertex.xError (),
             ey = vertex.yError (),
             ez = vertex.zError (),
             sumPt2 = 0.0;
      int ndf = vertex.ndof (),
          nTracks = 0.0;

      oneDHists_.at ("vertexX")->Fill (x);
      oneDHists_.at ("vertexY")->Fill (y);
      oneDHists_.at ("vertexZ")->Fill (z);
      oneDHists_.at ("vertexXError")->Fill (ex);
      oneDHists_.at ("vertexYError")->Fill (ey);
      oneDHists_.at ("vertexZError")->Fill (ez);
      oneDHists_.at ("vertexNDF")->Fill (ndf);

      for (auto track = vertex.tracks_begin (); track != vertex.tracks_end (); track++)
        {
          double pt = (*track)->pt ();

          if (pt < 0.7)
            continue;
          nTracks++;
          sumPt2 += pt * pt;
        }
      oneDHists_.at ("vertexNTracks")->Fill (nTracks);
      oneDHists_.at ("vertexSumPt2")->Fill (sumPt2);
    }

  for (const auto &track : *tracks)
    {
      double vz = track.vz (),
             pt = track.pt ();

      twoDHists_.at ("trackPtVsTrackZ")->Fill (vz, pt);
    }

  for (const auto &jet : *jets)
    {
      double pt = jet.pt (),
             eta = jet.eta (),
             totalPt = 0.0,
             pvPt = 0.0;

      if (pt < 100.0)
        continue;
      if (fabs (eta) > 5.0)
        continue;

      oneDHists_.at ("jetPt")->Fill (pt);
      oneDHists_.at ("jetEta")->Fill (eta);

      for (const auto &track : jet.getTrackRefs ())
        {
          double pt = track->pt ();
          long long id = trackHash (*track);

          if (pt < 0.7)
            continue;
          totalPt += pt;
          if (pvTrackID.count (id))
            pvPt += pt;
        }
      oneDHists_.at ("jetBeta")->Fill (pvPt / totalPt);
      twoDHists_.at ("jetBetaVsJetEta")->Fill (eta, pvPt / totalPt);
    }
}

long long
VFPixAnalyzer::trackHash (const reco::Track &track) const
{
  stringstream ss0, ss1, ss2;

  ss0 << abs (track.pt () * 1.0e3);
  ss1 << abs ((track.eta () + 10.0) * 1.0e3);
  ss2 << abs ((track.phi () + 4.0) * 1.0e3);

  return atoll ((ss0.str () + ss1.str () + ss2.str ()).c_str ());
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(VFPixAnalyzer);
