#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_set>

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "VFPix/FullSimStudies/plugins/VFPixAnalyzer.h"

VFPixAnalyzer::VFPixAnalyzer (const edm::ParameterSet &cfg) :
  jets_ (cfg.getParameter<edm::InputTag> ("jets")),
  trackJets_ (cfg.getParameter<edm::InputTag> ("trackJets")),
  pus_ (cfg.getParameter<edm::InputTag> ("pus")),
  vertices_ (cfg.getParameter<edm::InputTag> ("vertices")),
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks")),
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles")),
  simTracks_ (cfg.getParameter<edm::InputTag> ("simTracks"))
{
  vector<double> jetPtBins, trackPtBins, fineTrackPtBins, vertexPt2Bins, vertexTrackPtBins, ptErrorBins, d0ErrorBins, dzErrorBins, xErrorBins, yErrorBins, trackErrorPtBins, trackErrorBins, trackEtaBins,
                 ptDeltaBins, d0DeltaBins, dzDeltaBins, trackDeltaPtBins, trackDeltaBins;
  logSpace  (1000,  0.0,   4.0,  jetPtBins);
  logSpace  (100,   -1.0,  1.0,  trackPtBins);
  logSpace  (1000,  -1.0,  3.0,  fineTrackPtBins);
  logSpace  (1000,  -1.0,  8.0,  vertexPt2Bins);
  logSpace  (1000,  -2.0,  2.0,  vertexTrackPtBins);
  logSpace  (1000,  -2.0,  5.0,  ptErrorBins);
  logSpace  (1000,  -5.0,  0.0,  d0ErrorBins);
  logSpace  (1000,  -5.0,  1.0,  dzErrorBins);
  linSpace  (1000,  -10.0, 10.0,  ptDeltaBins);
  linSpace  (1000,  -0.1,  0.1,  d0DeltaBins);
  linSpace  (1000,  -0.05,  0.05,  dzDeltaBins);
  logSpace  (1000,  -5.0,  1.0,  xErrorBins);
  logSpace  (1000,  -5.0,  1.0,  yErrorBins);
  logSpace  (100,   -1.0,  3.0,  trackErrorPtBins);
  logSpace  (1000,  -6.0,  6.0,  trackErrorBins);

  linSpace  (50,    0.0,   5.0,  trackEtaBins);

  TH1::SetDefaultSumw2 ();
  TFileDirectory jetDir = fs_->mkdir ("jets"),
                 puDir = fs_->mkdir ("pu"),
                 vertexDir = fs_->mkdir ("vertices"),
                 trackDir = fs_->mkdir ("tracks"),
                 electronDir = fs_->mkdir ("electrons"),
                 muonDir = fs_->mkdir ("muons"),
                 chargedHadronDir = fs_->mkdir ("chargedHadrons"),
                 fakeTrackDir = fs_->mkdir ("fakeTracks"),
                 pvAssociationFactoredDir = fs_->mkdir ("pvAssociationFactored"),
                 pvAssociationFactored_TrackJetsDir = fs_->mkdir ("pvAssociationFactored_TrackJets");

  oneDHists_["jetEta"]   = jetDir.make<TH1D> ("jetEta", ";jet #eta", 1000, -5.0, 5.0);
  oneDHists_["jetPt"]    = jetDir.make<TH1D> ("jetPt", ";jet p_{T} [GeV]", jetPtBins.size () - 1, jetPtBins.data ());
  oneDHists_["jetSSV"]   = jetDir.make<TH1D> ("jetSSV", ";jet SSV discriminator", 1000, 0.0, 10.0);

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

  oneDHists_["bpixHitsVsTrackEta"] = trackDir.make<TH1D> ("bpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["fpixHitsVsTrackEta"] = trackDir.make<TH1D> ("fpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["nTracks"] = trackDir.make<TH1D> ("nTracks", ";number of tracks", 1000000, 0.0, 1000000.0);

  twoDHists_["trackEtaVsTrackPt"] = trackDir.make<TH2D> ("trackEtaVsTrackPt", ";track p_{T} [GeV];track #eta", fineTrackPtBins.size () - 1, fineTrackPtBins.data (), 1000, -5.0, 5.0);
  twoDHists_["trackPtVsTrackZ"] = trackDir.make<TH2D> ("trackPtVsTrackZ", ";track z [cm];track p_{T} [GeV]", 1000, -15.0, 15.0, trackPtBins.size () - 1, trackPtBins.data ());
  twoDHists_["ptErrorVsTrackEta_0p7"] = trackDir.make<TH2D> ("ptErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["d0ErrorVsTrackEta_0p7"] = trackDir.make<TH2D> ("d0ErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["dzErrorVsTrackEta_0p7"] = trackDir.make<TH2D> ("dzErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["ptErrorVsTrackEta_1p0"] = trackDir.make<TH2D> ("ptErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["d0ErrorVsTrackEta_1p0"] = trackDir.make<TH2D> ("d0ErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["dzErrorVsTrackEta_1p0"] = trackDir.make<TH2D> ("dzErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["ptErrorVsTrackEta_10p0"] = trackDir.make<TH2D> ("ptErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["d0ErrorVsTrackEta_10p0"] = trackDir.make<TH2D> ("d0ErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["dzErrorVsTrackEta_10p0"] = trackDir.make<TH2D> ("dzErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["ptErrorVsTrackEta_50p0"] = trackDir.make<TH2D> ("ptErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["d0ErrorVsTrackEta_50p0"] = trackDir.make<TH2D> ("d0ErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["dzErrorVsTrackEta_50p0"] = trackDir.make<TH2D> ("dzErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["ptErrorVsTrackEta_100p0"] = trackDir.make<TH2D> ("ptErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["d0ErrorVsTrackEta_100p0"] = trackDir.make<TH2D> ("d0ErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["dzErrorVsTrackEta_100p0"] = trackDir.make<TH2D> ("dzErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["bpixXErrorVsTrackEta"] = trackDir.make<TH2D> ("bpixXErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["bpixYErrorVsTrackEta"] = trackDir.make<TH2D> ("bpixYErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());
  twoDHists_["fpixXErrorVsTrackEta"] = trackDir.make<TH2D> ("fpixXErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["fpixYErrorVsTrackEta"] = trackDir.make<TH2D> ("fpixYErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());

  threeDHists_["trackPtError"] = trackDir.make<TH3D> ("trackPtError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltap_{T}/p_{T}) [%]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["trackD0Error"] = trackDir.make<TH3D> ("trackD0Error", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{0}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["trackDzError"] = trackDir.make<TH3D> ("trackDzError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{z}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());

  oneDHists_["electrons/bpixHitsVsTrackEta"] = electronDir.make<TH1D> ("bpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["electrons/fpixHitsVsTrackEta"] = electronDir.make<TH1D> ("fpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["electrons/nTracks"] = electronDir.make<TH1D> ("nTracks", ";number of tracks", 1000000, 0.0, 1000000.0);

  twoDHists_["electrons/trackEtaVsTrackPt"] = electronDir.make<TH2D> ("trackEtaVsTrackPt", ";track p_{T} [GeV];track #eta", fineTrackPtBins.size () - 1, fineTrackPtBins.data (), 1000, -5.0, 5.0);
  twoDHists_["electrons/trackPtVsTrackZ"] = electronDir.make<TH2D> ("trackPtVsTrackZ", ";track z [cm];track p_{T} [GeV]", 1000, -15.0, 15.0, trackPtBins.size () - 1, trackPtBins.data ());
  twoDHists_["electrons/ptErrorVsTrackEta_0p7"] = electronDir.make<TH2D> ("ptErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["electrons/d0ErrorVsTrackEta_0p7"] = electronDir.make<TH2D> ("d0ErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["electrons/dzErrorVsTrackEta_0p7"] = electronDir.make<TH2D> ("dzErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["electrons/ptErrorVsTrackEta_1p0"] = electronDir.make<TH2D> ("ptErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["electrons/d0ErrorVsTrackEta_1p0"] = electronDir.make<TH2D> ("d0ErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["electrons/dzErrorVsTrackEta_1p0"] = electronDir.make<TH2D> ("dzErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["electrons/ptErrorVsTrackEta_10p0"] = electronDir.make<TH2D> ("ptErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["electrons/d0ErrorVsTrackEta_10p0"] = electronDir.make<TH2D> ("d0ErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["electrons/dzErrorVsTrackEta_10p0"] = electronDir.make<TH2D> ("dzErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["electrons/ptErrorVsTrackEta_50p0"] = electronDir.make<TH2D> ("ptErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["electrons/d0ErrorVsTrackEta_50p0"] = electronDir.make<TH2D> ("d0ErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["electrons/dzErrorVsTrackEta_50p0"] = electronDir.make<TH2D> ("dzErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["electrons/ptErrorVsTrackEta_100p0"] = electronDir.make<TH2D> ("ptErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["electrons/d0ErrorVsTrackEta_100p0"] = electronDir.make<TH2D> ("d0ErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["electrons/dzErrorVsTrackEta_100p0"] = electronDir.make<TH2D> ("dzErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["electrons/ptDeltaVsTrackEta_0p7"] = electronDir.make<TH2D> ("ptDeltaVsTrackEta_0p7", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["electrons/d0DeltaVsTrackEta_0p7"] = electronDir.make<TH2D> ("d0DeltaVsTrackEta_0p7", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["electrons/dzDeltaVsTrackEta_0p7"] = electronDir.make<TH2D> ("dzDeltaVsTrackEta_0p7", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["electrons/ptDeltaVsTrackEta_1p0"] = electronDir.make<TH2D> ("ptDeltaVsTrackEta_1p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["electrons/d0DeltaVsTrackEta_1p0"] = electronDir.make<TH2D> ("d0DeltaVsTrackEta_1p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["electrons/dzDeltaVsTrackEta_1p0"] = electronDir.make<TH2D> ("dzDeltaVsTrackEta_1p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["electrons/ptDeltaVsTrackEta_10p0"] = electronDir.make<TH2D> ("ptDeltaVsTrackEta_10p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["electrons/d0DeltaVsTrackEta_10p0"] = electronDir.make<TH2D> ("d0DeltaVsTrackEta_10p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["electrons/dzDeltaVsTrackEta_10p0"] = electronDir.make<TH2D> ("dzDeltaVsTrackEta_10p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["electrons/ptDeltaVsTrackEta_50p0"] = electronDir.make<TH2D> ("ptDeltaVsTrackEta_50p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["electrons/d0DeltaVsTrackEta_50p0"] = electronDir.make<TH2D> ("d0DeltaVsTrackEta_50p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["electrons/dzDeltaVsTrackEta_50p0"] = electronDir.make<TH2D> ("dzDeltaVsTrackEta_50p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["electrons/ptDeltaVsTrackEta_100p0"] = electronDir.make<TH2D> ("ptDeltaVsTrackEta_100p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["electrons/d0DeltaVsTrackEta_100p0"] = electronDir.make<TH2D> ("d0DeltaVsTrackEta_100p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["electrons/dzDeltaVsTrackEta_100p0"] = electronDir.make<TH2D> ("dzDeltaVsTrackEta_100p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["electrons/bpixXErrorVsTrackEta"] = electronDir.make<TH2D> ("bpixXErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["electrons/bpixYErrorVsTrackEta"] = electronDir.make<TH2D> ("bpixYErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());
  twoDHists_["electrons/fpixXErrorVsTrackEta"] = electronDir.make<TH2D> ("fpixXErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["electrons/fpixYErrorVsTrackEta"] = electronDir.make<TH2D> ("fpixYErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());

  threeDHists_["electrons/trackPtError"] = electronDir.make<TH3D> ("trackPtError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltap_{T}/p_{T}) [%]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["electrons/trackD0Error"] = electronDir.make<TH3D> ("trackD0Error", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{0}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["electrons/trackDzError"] = electronDir.make<TH3D> ("trackDzError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{z}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());

  oneDHists_["muons/bpixHitsVsTrackEta"] = muonDir.make<TH1D> ("bpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["muons/fpixHitsVsTrackEta"] = muonDir.make<TH1D> ("fpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["muons/nTracks"] = muonDir.make<TH1D> ("nTracks", ";number of tracks", 1000000, 0.0, 1000000.0);

  twoDHists_["muons/trackEtaVsTrackPt"] = muonDir.make<TH2D> ("trackEtaVsTrackPt", ";track p_{T} [GeV];track #eta", fineTrackPtBins.size () - 1, fineTrackPtBins.data (), 1000, -5.0, 5.0);
  twoDHists_["muons/trackPtVsTrackZ"] = muonDir.make<TH2D> ("trackPtVsTrackZ", ";track z [cm];track p_{T} [GeV]", 1000, -15.0, 15.0, trackPtBins.size () - 1, trackPtBins.data ());
  twoDHists_["muons/ptErrorVsTrackEta_0p7"] = muonDir.make<TH2D> ("ptErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["muons/d0ErrorVsTrackEta_0p7"] = muonDir.make<TH2D> ("d0ErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["muons/dzErrorVsTrackEta_0p7"] = muonDir.make<TH2D> ("dzErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["muons/ptErrorVsTrackEta_1p0"] = muonDir.make<TH2D> ("ptErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["muons/d0ErrorVsTrackEta_1p0"] = muonDir.make<TH2D> ("d0ErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["muons/dzErrorVsTrackEta_1p0"] = muonDir.make<TH2D> ("dzErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["muons/ptErrorVsTrackEta_10p0"] = muonDir.make<TH2D> ("ptErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["muons/d0ErrorVsTrackEta_10p0"] = muonDir.make<TH2D> ("d0ErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["muons/dzErrorVsTrackEta_10p0"] = muonDir.make<TH2D> ("dzErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["muons/ptErrorVsTrackEta_50p0"] = muonDir.make<TH2D> ("ptErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["muons/d0ErrorVsTrackEta_50p0"] = muonDir.make<TH2D> ("d0ErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["muons/dzErrorVsTrackEta_50p0"] = muonDir.make<TH2D> ("dzErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["muons/ptErrorVsTrackEta_100p0"] = muonDir.make<TH2D> ("ptErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["muons/d0ErrorVsTrackEta_100p0"] = muonDir.make<TH2D> ("d0ErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["muons/dzErrorVsTrackEta_100p0"] = muonDir.make<TH2D> ("dzErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["muons/ptDeltaVsTrackEta_0p7"] = muonDir.make<TH2D> ("ptDeltaVsTrackEta_0p7", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["muons/d0DeltaVsTrackEta_0p7"] = muonDir.make<TH2D> ("d0DeltaVsTrackEta_0p7", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["muons/dzDeltaVsTrackEta_0p7"] = muonDir.make<TH2D> ("dzDeltaVsTrackEta_0p7", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["muons/ptDeltaVsTrackEta_1p0"] = muonDir.make<TH2D> ("ptDeltaVsTrackEta_1p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["muons/d0DeltaVsTrackEta_1p0"] = muonDir.make<TH2D> ("d0DeltaVsTrackEta_1p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["muons/dzDeltaVsTrackEta_1p0"] = muonDir.make<TH2D> ("dzDeltaVsTrackEta_1p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["muons/ptDeltaVsTrackEta_10p0"] = muonDir.make<TH2D> ("ptDeltaVsTrackEta_10p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["muons/d0DeltaVsTrackEta_10p0"] = muonDir.make<TH2D> ("d0DeltaVsTrackEta_10p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["muons/dzDeltaVsTrackEta_10p0"] = muonDir.make<TH2D> ("dzDeltaVsTrackEta_10p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["muons/ptDeltaVsTrackEta_50p0"] = muonDir.make<TH2D> ("ptDeltaVsTrackEta_50p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["muons/d0DeltaVsTrackEta_50p0"] = muonDir.make<TH2D> ("d0DeltaVsTrackEta_50p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["muons/dzDeltaVsTrackEta_50p0"] = muonDir.make<TH2D> ("dzDeltaVsTrackEta_50p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["muons/ptDeltaVsTrackEta_100p0"] = muonDir.make<TH2D> ("ptDeltaVsTrackEta_100p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["muons/d0DeltaVsTrackEta_100p0"] = muonDir.make<TH2D> ("d0DeltaVsTrackEta_100p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["muons/dzDeltaVsTrackEta_100p0"] = muonDir.make<TH2D> ("dzDeltaVsTrackEta_100p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["muons/bpixXErrorVsTrackEta"] = muonDir.make<TH2D> ("bpixXErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["muons/bpixYErrorVsTrackEta"] = muonDir.make<TH2D> ("bpixYErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());
  twoDHists_["muons/fpixXErrorVsTrackEta"] = muonDir.make<TH2D> ("fpixXErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["muons/fpixYErrorVsTrackEta"] = muonDir.make<TH2D> ("fpixYErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());

  threeDHists_["muons/trackPtError"] = muonDir.make<TH3D> ("trackPtError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltap_{T}/p_{T}) [%]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["muons/trackD0Error"] = muonDir.make<TH3D> ("trackD0Error", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{0}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["muons/trackDzError"] = muonDir.make<TH3D> ("trackDzError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{z}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());

  oneDHists_["chargedHadrons/bpixHitsVsTrackEta"] = chargedHadronDir.make<TH1D> ("bpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["chargedHadrons/fpixHitsVsTrackEta"] = chargedHadronDir.make<TH1D> ("fpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["chargedHadrons/nTracks"] = chargedHadronDir.make<TH1D> ("nTracks", ";number of tracks", 1000000, 0.0, 1000000.0);

  twoDHists_["chargedHadrons/trackEtaVsTrackPt"] = chargedHadronDir.make<TH2D> ("trackEtaVsTrackPt", ";track p_{T} [GeV];track #eta", fineTrackPtBins.size () - 1, fineTrackPtBins.data (), 1000, -5.0, 5.0);
  twoDHists_["chargedHadrons/trackPtVsTrackZ"] = chargedHadronDir.make<TH2D> ("trackPtVsTrackZ", ";track z [cm];track p_{T} [GeV]", 1000, -15.0, 15.0, trackPtBins.size () - 1, trackPtBins.data ());
  twoDHists_["chargedHadrons/ptErrorVsTrackEta_0p7"] = chargedHadronDir.make<TH2D> ("ptErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["chargedHadrons/d0ErrorVsTrackEta_0p7"] = chargedHadronDir.make<TH2D> ("d0ErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["chargedHadrons/dzErrorVsTrackEta_0p7"] = chargedHadronDir.make<TH2D> ("dzErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["chargedHadrons/ptErrorVsTrackEta_1p0"] = chargedHadronDir.make<TH2D> ("ptErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["chargedHadrons/d0ErrorVsTrackEta_1p0"] = chargedHadronDir.make<TH2D> ("d0ErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["chargedHadrons/dzErrorVsTrackEta_1p0"] = chargedHadronDir.make<TH2D> ("dzErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["chargedHadrons/ptErrorVsTrackEta_10p0"] = chargedHadronDir.make<TH2D> ("ptErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["chargedHadrons/d0ErrorVsTrackEta_10p0"] = chargedHadronDir.make<TH2D> ("d0ErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["chargedHadrons/dzErrorVsTrackEta_10p0"] = chargedHadronDir.make<TH2D> ("dzErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["chargedHadrons/ptErrorVsTrackEta_50p0"] = chargedHadronDir.make<TH2D> ("ptErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["chargedHadrons/d0ErrorVsTrackEta_50p0"] = chargedHadronDir.make<TH2D> ("d0ErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["chargedHadrons/dzErrorVsTrackEta_50p0"] = chargedHadronDir.make<TH2D> ("dzErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["chargedHadrons/ptErrorVsTrackEta_100p0"] = chargedHadronDir.make<TH2D> ("ptErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["chargedHadrons/d0ErrorVsTrackEta_100p0"] = chargedHadronDir.make<TH2D> ("d0ErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["chargedHadrons/dzErrorVsTrackEta_100p0"] = chargedHadronDir.make<TH2D> ("dzErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["chargedHadrons/ptDeltaVsTrackEta_0p7"] = chargedHadronDir.make<TH2D> ("ptDeltaVsTrackEta_0p7", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["chargedHadrons/d0DeltaVsTrackEta_0p7"] = chargedHadronDir.make<TH2D> ("d0DeltaVsTrackEta_0p7", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["chargedHadrons/dzDeltaVsTrackEta_0p7"] = chargedHadronDir.make<TH2D> ("dzDeltaVsTrackEta_0p7", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["chargedHadrons/ptDeltaVsTrackEta_1p0"] = chargedHadronDir.make<TH2D> ("ptDeltaVsTrackEta_1p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["chargedHadrons/d0DeltaVsTrackEta_1p0"] = chargedHadronDir.make<TH2D> ("d0DeltaVsTrackEta_1p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["chargedHadrons/dzDeltaVsTrackEta_1p0"] = chargedHadronDir.make<TH2D> ("dzDeltaVsTrackEta_1p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["chargedHadrons/ptDeltaVsTrackEta_10p0"] = chargedHadronDir.make<TH2D> ("ptDeltaVsTrackEta_10p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["chargedHadrons/d0DeltaVsTrackEta_10p0"] = chargedHadronDir.make<TH2D> ("d0DeltaVsTrackEta_10p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["chargedHadrons/dzDeltaVsTrackEta_10p0"] = chargedHadronDir.make<TH2D> ("dzDeltaVsTrackEta_10p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["chargedHadrons/ptDeltaVsTrackEta_50p0"] = chargedHadronDir.make<TH2D> ("ptDeltaVsTrackEta_50p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["chargedHadrons/d0DeltaVsTrackEta_50p0"] = chargedHadronDir.make<TH2D> ("d0DeltaVsTrackEta_50p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["chargedHadrons/dzDeltaVsTrackEta_50p0"] = chargedHadronDir.make<TH2D> ("dzDeltaVsTrackEta_50p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["chargedHadrons/ptDeltaVsTrackEta_100p0"] = chargedHadronDir.make<TH2D> ("ptDeltaVsTrackEta_100p0", ";track |#eta|;track #delta_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptDeltaBins.size () - 1, ptDeltaBins.data ());
  twoDHists_["chargedHadrons/d0DeltaVsTrackEta_100p0"] = chargedHadronDir.make<TH2D> ("d0DeltaVsTrackEta_100p0", ";track |#eta|;track #delta_{d_{0}} [cm]", 1000, 0.0, 5.0, d0DeltaBins.size () - 1, d0DeltaBins.data ());
  twoDHists_["chargedHadrons/dzDeltaVsTrackEta_100p0"] = chargedHadronDir.make<TH2D> ("dzDeltaVsTrackEta_100p0", ";track |#eta|;track #delta_{d_{z}} [cm]", 1000, 0.0, 5.0, dzDeltaBins.size () - 1, dzDeltaBins.data ());
  twoDHists_["chargedHadrons/bpixXErrorVsTrackEta"] = chargedHadronDir.make<TH2D> ("bpixXErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["chargedHadrons/bpixYErrorVsTrackEta"] = chargedHadronDir.make<TH2D> ("bpixYErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());
  twoDHists_["chargedHadrons/fpixXErrorVsTrackEta"] = chargedHadronDir.make<TH2D> ("fpixXErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["chargedHadrons/fpixYErrorVsTrackEta"] = chargedHadronDir.make<TH2D> ("fpixYErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());

  threeDHists_["chargedHadrons/trackPtError"] = chargedHadronDir.make<TH3D> ("trackPtError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltap_{T}/p_{T}) [%]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["chargedHadrons/trackD0Error"] = chargedHadronDir.make<TH3D> ("trackD0Error", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{0}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["chargedHadrons/trackDzError"] = chargedHadronDir.make<TH3D> ("trackDzError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{z}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());

  oneDHists_["fakeTracks/bpixHitsVsTrackEta"] = fakeTrackDir.make<TH1D> ("bpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["fakeTracks/fpixHitsVsTrackEta"] = fakeTrackDir.make<TH1D> ("fpixHitsVsTrackEta", ";track #eta", 1000, -5.0, 5.0);
  oneDHists_["fakeTracks/nTracks"] = fakeTrackDir.make<TH1D> ("nTracks", ";number of tracks", 1000000, 0.0, 1000000.0);

  twoDHists_["fakeTracks/trackEtaVsTrackPt"] = fakeTrackDir.make<TH2D> ("trackEtaVsTrackPt", ";track p_{T} [GeV];track #eta", fineTrackPtBins.size () - 1, fineTrackPtBins.data (), 1000, -5.0, 5.0);
  twoDHists_["fakeTracks/trackPtVsTrackZ"] = fakeTrackDir.make<TH2D> ("trackPtVsTrackZ", ";track z [cm];track p_{T} [GeV]", 1000, -15.0, 15.0, trackPtBins.size () - 1, trackPtBins.data ());
  twoDHists_["fakeTracks/ptErrorVsTrackEta_0p7"] = fakeTrackDir.make<TH2D> ("ptErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["fakeTracks/d0ErrorVsTrackEta_0p7"] = fakeTrackDir.make<TH2D> ("d0ErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["fakeTracks/dzErrorVsTrackEta_0p7"] = fakeTrackDir.make<TH2D> ("dzErrorVsTrackEta_0p7", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["fakeTracks/ptErrorVsTrackEta_1p0"] = fakeTrackDir.make<TH2D> ("ptErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["fakeTracks/d0ErrorVsTrackEta_1p0"] = fakeTrackDir.make<TH2D> ("d0ErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["fakeTracks/dzErrorVsTrackEta_1p0"] = fakeTrackDir.make<TH2D> ("dzErrorVsTrackEta_1p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["fakeTracks/ptErrorVsTrackEta_10p0"] = fakeTrackDir.make<TH2D> ("ptErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["fakeTracks/d0ErrorVsTrackEta_10p0"] = fakeTrackDir.make<TH2D> ("d0ErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["fakeTracks/dzErrorVsTrackEta_10p0"] = fakeTrackDir.make<TH2D> ("dzErrorVsTrackEta_10p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["fakeTracks/ptErrorVsTrackEta_50p0"] = fakeTrackDir.make<TH2D> ("ptErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["fakeTracks/d0ErrorVsTrackEta_50p0"] = fakeTrackDir.make<TH2D> ("d0ErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["fakeTracks/dzErrorVsTrackEta_50p0"] = fakeTrackDir.make<TH2D> ("dzErrorVsTrackEta_50p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["fakeTracks/ptErrorVsTrackEta_100p0"] = fakeTrackDir.make<TH2D> ("ptErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{p_{T}} / p_{T} [%]", 1000, 0.0, 5.0, ptErrorBins.size () - 1, ptErrorBins.data ());
  twoDHists_["fakeTracks/d0ErrorVsTrackEta_100p0"] = fakeTrackDir.make<TH2D> ("d0ErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{0}} [cm]", 1000, 0.0, 5.0, d0ErrorBins.size () - 1, d0ErrorBins.data ());
  twoDHists_["fakeTracks/dzErrorVsTrackEta_100p0"] = fakeTrackDir.make<TH2D> ("dzErrorVsTrackEta_100p0", ";track |#eta|;track #sigma_{d_{z}} [cm]", 1000, 0.0, 5.0, dzErrorBins.size () - 1, dzErrorBins.data ());
  twoDHists_["fakeTracks/bpixXErrorVsTrackEta"] = fakeTrackDir.make<TH2D> ("bpixXErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["fakeTracks/bpixYErrorVsTrackEta"] = fakeTrackDir.make<TH2D> ("bpixYErrorVsTrackEta", ";track |#eta|;BPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());
  twoDHists_["fakeTracks/fpixXErrorVsTrackEta"] = fakeTrackDir.make<TH2D> ("fpixXErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{x} [cm]", 1000, 0.0, 5.0, xErrorBins.size () - 1, xErrorBins.data ());
  twoDHists_["fakeTracks/fpixYErrorVsTrackEta"] = fakeTrackDir.make<TH2D> ("fpixYErrorVsTrackEta", ";track |#eta|;FPIX hit #sigma_{y} [cm]", 1000, 0.0, 5.0, yErrorBins.size () - 1, yErrorBins.data ());

  threeDHists_["fakeTracks/trackPtError"] = fakeTrackDir.make<TH3D> ("trackPtError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltap_{T}/p_{T}) [%]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["fakeTracks/trackD0Error"] = fakeTrackDir.make<TH3D> ("trackD0Error", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{0}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());
  threeDHists_["fakeTracks/trackDzError"] = fakeTrackDir.make<TH3D> ("trackDzError", ";track |#eta|;track p_{} [GeV];track #sigma(#deltad_{z}) [cm]", trackEtaBins.size () - 1, trackEtaBins.data (), trackErrorPtBins.size () - 1, trackErrorPtBins.data (), trackErrorBins.size () - 1, trackErrorBins.data ());

  oneDHists_["pvAssociationFactored/vbfQuarkEta"] = pvAssociationFactoredDir.make<TH1D> ("vbfQuarkEta", ";VBF quark |#eta|", 1000, 0.0, 5.0);
  oneDHists_["pvAssociationFactored/vbfJetsFound"] = pvAssociationFactoredDir.make<TH1D> ("vbfJetsFound", ";VBF quark |#eta|", 1000, 0.0, 5.0);
  oneDHists_["pvAssociationFactored_TrackJets/vbfQuarkEta"] = pvAssociationFactored_TrackJetsDir.make<TH1D> ("vbfQuarkEta", ";VBF quark |#eta|", 1000, 0.0, 5.0);
  oneDHists_["pvAssociationFactored_TrackJets/vbfJetsFound"] = pvAssociationFactored_TrackJetsDir.make<TH1D> ("vbfJetsFound", ";VBF quark |#eta|", 1000, 0.0, 5.0);
}

VFPixAnalyzer::~VFPixAnalyzer ()
{
}

void
VFPixAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::PFJet> > jets;
  event.getByLabel (jets_, jets);
  edm::Handle<vector<reco::TrackJet> > trackJets;
  event.getByLabel (trackJets_, trackJets);
  edm::Handle<vector<PileupSummaryInfo> > pus;
  event.getByLabel (pus_, pus);
  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByLabel (vertices_, vertices);
  edm::Handle<vector<reco::Track> > tracks;
  event.getByLabel (tracks_, tracks);
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);
  edm::Handle<vector<SimTrack> > simTracks;
  event.getByLabel (simTracks_, simTracks);

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
            oneDHists_.at ("nPU_bx0")->Fill (nPU_bx0 = currentNPU);
            break;
          case 1:
            oneDHists_.at ("nPU_bxP1")->Fill (currentNPU);
            oneDHists_.at ("nOOPU")->Fill (currentNPU);
            break;
          default:
            oneDHists_.at ("nOOPU")->Fill (currentNPU);
        }
    }

  double pvTrueX = genParticles->at (2).vx (),
         pvTrueY = genParticles->at (2).vy (),
         pvTrueZ = genParticles->at (2).vz ();
  unordered_set<long long> pvTrackID;
  if (vertices->size () > 0)
    {
      double x = vertices->at (0).x (),
             y = vertices->at (0).y (),
             z = vertices->at (0).z (),
             ex = vertices->at (0).xError (),
             ey = vertices->at (0).yError (),
             ez = vertices->at (0).zError (),
             sumPt2 = 0.0;
      int ndf = vertices->at (0).ndof (),
          nTracks = 0;

      if (ndf >= 4)
        {
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

              if (pt < 0.7)
                continue;
              nTracks++;
              sumPt2 += pt * pt;
            }
          oneDHists_.at ("pvNTracks")->Fill (nTracks);
          oneDHists_.at ("pvSumPt2")->Fill (sumPt2);
        }
    }
  unsigned nVertices = 0;
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
          nTracks = 0;

      if (ndf < 4)
        continue;
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
      nVertices++;
    }
  twoDHists_.at ("nVerticesVsNPU")->Fill (nPU_bx0, nVertices);

  unsigned nTracks = 0, nElectrons = 0, nMuons = 0, nChargedHadrons = 0, nFakeTracks = 0;
  /*for (const auto &track : *tracks)
    {
      double vz = track.vz (),
             pt = track.pt (),
             d0 = track.d0 (),
             dz = track.dz (),
             eta = track.eta (),
             normalizedChi2 = track.normalizedChi2 (),
             ptError = track.ptError (),
             d0Error = track.d0Error (),
             dzError = track.dzError ();
      unsigned pixelLayersWithMeasurement = track.hitPattern ().pixelLayersWithMeasurement (),
               trackerLayersWithMeasurement = track.hitPattern ().trackerLayersWithMeasurement ();

      if (normalizedChi2 > 20.0
       || pixelLayersWithMeasurement < 2
       || trackerLayersWithMeasurement < 5
       || (d0 / d0Error) > 5.0)
        continue;
      if (pt > 0.7)
        nTracks++;
      twoDHists_.at ("trackEtaVsTrackPt")->Fill (pt, eta);
      twoDHists_.at ("trackPtVsTrackZ")->Fill (vz, pt);
      if (fabs (pt - 0.7) / 0.7 < 0.1)
        {
          twoDHists_.at ("ptErrorVsTrackEta_0p7")->Fill (fabs (eta), (ptError / pt) * 100.0);
          twoDHists_.at ("d0ErrorVsTrackEta_0p7")->Fill (fabs (eta), d0Error);
          twoDHists_.at ("dzErrorVsTrackEta_0p7")->Fill (fabs (eta), dzError);
        }
      if (fabs (pt - 1.0) / 1.0 < 0.1)
        {
          twoDHists_.at ("ptErrorVsTrackEta_1p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
          twoDHists_.at ("d0ErrorVsTrackEta_1p0")->Fill (fabs (eta), d0Error);
          twoDHists_.at ("dzErrorVsTrackEta_1p0")->Fill (fabs (eta), dzError);
        }
      if (fabs (pt - 10.0) / 10.0 < 0.1)
        {
          twoDHists_.at ("ptErrorVsTrackEta_10p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
          twoDHists_.at ("d0ErrorVsTrackEta_10p0")->Fill (fabs (eta), d0Error);
          twoDHists_.at ("dzErrorVsTrackEta_10p0")->Fill (fabs (eta), dzError);
        }
      if (fabs (pt - 50.0) / 50.0 < 0.1)
        {
          twoDHists_.at ("ptErrorVsTrackEta_50p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
          twoDHists_.at ("d0ErrorVsTrackEta_50p0")->Fill (fabs (eta), d0Error);
          twoDHists_.at ("dzErrorVsTrackEta_50p0")->Fill (fabs (eta), dzError);
        }
      if (fabs (pt - 100.0) / 100.0 < 0.1)
        {
          twoDHists_.at ("ptErrorVsTrackEta_100p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
          twoDHists_.at ("d0ErrorVsTrackEta_100p0")->Fill (fabs (eta), d0Error);
          twoDHists_.at ("dzErrorVsTrackEta_100p0")->Fill (fabs (eta), dzError);
        }

      threeDHists_.at ("trackPtError")->Fill (eta, pt, (ptError / pt) * 100.0);
      threeDHists_.at ("trackD0Error")->Fill (eta, pt, d0Error);
      threeDHists_.at ("trackDzError")->Fill (eta, pt, dzError);

      const reco::GenParticle *closestParticle = NULL;
      const SimTrack *closestTrack = NULL;

      if (isMatched (track, genParticles, 11, 0.1, closestParticle))
        {
          double genPt = closestParticle->pt (),
                 genD0 = (closestParticle->vx () * closestParticle->py () - closestParticle->vy () * closestParticle->px ()) / closestParticle->pt (),
                 genDz = closestParticle->vz () - (closestParticle->vx () * closestParticle->px () + closestParticle->vy () * closestParticle->py ()) / closestParticle->pt () * (closestParticle->pz () / closestParticle->pt ()),
                 ptDelta = genPt - pt,
                 d0Delta = genD0 - d0,
                 dzDelta = genDz - dz;

          if (pt > 0.7)
            nElectrons++;
          twoDHists_.at ("electrons/trackEtaVsTrackPt")->Fill (pt, eta);
          twoDHists_.at ("electrons/trackPtVsTrackZ")->Fill (vz, pt);
          if (fabs (pt - 0.7) / 0.7 < 0.1)
            {
              twoDHists_.at ("electrons/ptErrorVsTrackEta_0p7")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("electrons/d0ErrorVsTrackEta_0p7")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("electrons/dzErrorVsTrackEta_0p7")->Fill (fabs (eta), dzError);
              twoDHists_.at ("electrons/ptDeltaVsTrackEta_0p7")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("electrons/d0DeltaVsTrackEta_0p7")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("electrons/dzDeltaVsTrackEta_0p7")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 1.0) / 1.0 < 0.1)
            {
              twoDHists_.at ("electrons/ptErrorVsTrackEta_1p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("electrons/d0ErrorVsTrackEta_1p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("electrons/dzErrorVsTrackEta_1p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("electrons/ptDeltaVsTrackEta_1p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("electrons/d0DeltaVsTrackEta_1p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("electrons/dzDeltaVsTrackEta_1p0")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 10.0) / 10.0 < 0.1)
            {
              twoDHists_.at ("electrons/ptErrorVsTrackEta_10p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("electrons/d0ErrorVsTrackEta_10p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("electrons/dzErrorVsTrackEta_10p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("electrons/ptDeltaVsTrackEta_10p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("electrons/d0DeltaVsTrackEta_10p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("electrons/dzDeltaVsTrackEta_10p0")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 50.0) / 50.0 < 0.1)
            {
              twoDHists_.at ("electrons/ptErrorVsTrackEta_50p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("electrons/d0ErrorVsTrackEta_50p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("electrons/dzErrorVsTrackEta_50p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("electrons/ptDeltaVsTrackEta_50p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("electrons/d0DeltaVsTrackEta_50p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("electrons/dzDeltaVsTrackEta_50p0")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 100.0) / 100.0 < 0.1)
            {
              twoDHists_.at ("electrons/ptErrorVsTrackEta_100p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("electrons/d0ErrorVsTrackEta_100p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("electrons/dzErrorVsTrackEta_100p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("electrons/ptDeltaVsTrackEta_100p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("electrons/d0DeltaVsTrackEta_100p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("electrons/dzDeltaVsTrackEta_100p0")->Fill (fabs (eta), dzDelta);
            }

          threeDHists_.at ("electrons/trackPtError")->Fill (eta, pt, (ptError / pt) * 100.0);
          threeDHists_.at ("electrons/trackD0Error")->Fill (eta, pt, d0Error);
          threeDHists_.at ("electrons/trackDzError")->Fill (eta, pt, dzError);
        }
      else if (isMatched (track, genParticles, 13, 0.1, closestParticle))
        {
          double genPt = closestParticle->pt (),
                 genD0 = (closestParticle->vx () * closestParticle->py () - closestParticle->vy () * closestParticle->px ()) / closestParticle->pt (),
                 genDz = closestParticle->vz () - (closestParticle->vx () * closestParticle->px () + closestParticle->vy () * closestParticle->py ()) / closestParticle->pt () * (closestParticle->pz () / closestParticle->pt ()),
                 ptDelta = genPt - pt,
                 d0Delta = genD0 - d0,
                 dzDelta = genDz - dz;

          if (pt > 0.7)
            nMuons++;
          twoDHists_.at ("muons/trackEtaVsTrackPt")->Fill (pt, eta);
          twoDHists_.at ("muons/trackPtVsTrackZ")->Fill (vz, pt);
          if (fabs (pt - 0.7) / 0.7 < 0.1)
            {
              twoDHists_.at ("muons/ptErrorVsTrackEta_0p7")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("muons/d0ErrorVsTrackEta_0p7")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("muons/dzErrorVsTrackEta_0p7")->Fill (fabs (eta), dzError);
              twoDHists_.at ("muons/ptDeltaVsTrackEta_0p7")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("muons/d0DeltaVsTrackEta_0p7")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("muons/dzDeltaVsTrackEta_0p7")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 1.0) / 1.0 < 0.1)
            {
              twoDHists_.at ("muons/ptErrorVsTrackEta_1p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("muons/d0ErrorVsTrackEta_1p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("muons/dzErrorVsTrackEta_1p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("muons/ptDeltaVsTrackEta_1p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("muons/d0DeltaVsTrackEta_1p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("muons/dzDeltaVsTrackEta_1p0")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 10.0) / 10.0 < 0.1)
            {
              twoDHists_.at ("muons/ptErrorVsTrackEta_10p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("muons/d0ErrorVsTrackEta_10p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("muons/dzErrorVsTrackEta_10p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("muons/ptDeltaVsTrackEta_10p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("muons/d0DeltaVsTrackEta_10p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("muons/dzDeltaVsTrackEta_10p0")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 50.0) / 50.0 < 0.1)
            {
              twoDHists_.at ("muons/ptErrorVsTrackEta_50p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("muons/d0ErrorVsTrackEta_50p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("muons/dzErrorVsTrackEta_50p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("muons/ptDeltaVsTrackEta_50p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("muons/d0DeltaVsTrackEta_50p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("muons/dzDeltaVsTrackEta_50p0")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 100.0) / 100.0 < 0.1)
            {
              twoDHists_.at ("muons/ptErrorVsTrackEta_100p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("muons/d0ErrorVsTrackEta_100p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("muons/dzErrorVsTrackEta_100p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("muons/ptDeltaVsTrackEta_100p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("muons/d0DeltaVsTrackEta_100p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("muons/dzDeltaVsTrackEta_100p0")->Fill (fabs (eta), dzDelta);
            }

          threeDHists_.at ("muons/trackPtError")->Fill (eta, pt, (ptError / pt) * 100.0);
          threeDHists_.at ("muons/trackD0Error")->Fill (eta, pt, d0Error);
          threeDHists_.at ("muons/trackDzError")->Fill (eta, pt, dzError);
        }
      else if (isMatched (track, simTracks, 0.001, closestTrack))
        {
          double genPt = -1.0, genD0 = -1.0, genDz = -1.0, ptDelta = -1.0, d0Delta = -1.0, dzDelta = -1.0;

          if (!closestTrack->noGenpart ())
            {
              closestParticle = &(genParticles->at (closestTrack->genpartIndex () - 1));
              genPt = closestParticle->pt (),
              genD0 = (closestParticle->vx () * closestParticle->py () - closestParticle->vy () * closestParticle->px ()) / closestParticle->pt (),
              genDz = closestParticle->vz () - (closestParticle->vx () * closestParticle->px () + closestParticle->vy () * closestParticle->py ()) / closestParticle->pt () * (closestParticle->pz () / closestParticle->pt ()),
              ptDelta = genPt - pt,
              d0Delta = genD0 - d0,
              dzDelta = genDz - dz;
            }

          if (pt > 0.7)
            nChargedHadrons++;
          twoDHists_.at ("chargedHadrons/trackEtaVsTrackPt")->Fill (pt, eta);
          twoDHists_.at ("chargedHadrons/trackPtVsTrackZ")->Fill (vz, pt);
          if (fabs (pt - 0.7) / 0.7 < 0.1)
            {
              twoDHists_.at ("chargedHadrons/ptErrorVsTrackEta_0p7")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0ErrorVsTrackEta_0p7")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("chargedHadrons/dzErrorVsTrackEta_0p7")->Fill (fabs (eta), dzError);
              twoDHists_.at ("chargedHadrons/ptDeltaVsTrackEta_0p7")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0DeltaVsTrackEta_0p7")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("chargedHadrons/dzDeltaVsTrackEta_0p7")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 1.0) / 1.0 < 0.1)
            {
              twoDHists_.at ("chargedHadrons/ptErrorVsTrackEta_1p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0ErrorVsTrackEta_1p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("chargedHadrons/dzErrorVsTrackEta_1p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("chargedHadrons/ptDeltaVsTrackEta_1p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0DeltaVsTrackEta_1p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("chargedHadrons/dzDeltaVsTrackEta_1p0")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 10.0) / 10.0 < 0.1)
            {
              twoDHists_.at ("chargedHadrons/ptErrorVsTrackEta_10p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0ErrorVsTrackEta_10p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("chargedHadrons/dzErrorVsTrackEta_10p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("chargedHadrons/ptDeltaVsTrackEta_10p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0DeltaVsTrackEta_10p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("chargedHadrons/dzDeltaVsTrackEta_10p0")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 50.0) / 50.0 < 0.1)
            {
              twoDHists_.at ("chargedHadrons/ptErrorVsTrackEta_50p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0ErrorVsTrackEta_50p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("chargedHadrons/dzErrorVsTrackEta_50p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("chargedHadrons/ptDeltaVsTrackEta_50p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0DeltaVsTrackEta_50p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("chargedHadrons/dzDeltaVsTrackEta_50p0")->Fill (fabs (eta), dzDelta);
            }
          if (fabs (pt - 100.0) / 100.0 < 0.1)
            {
              twoDHists_.at ("chargedHadrons/ptErrorVsTrackEta_100p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0ErrorVsTrackEta_100p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("chargedHadrons/dzErrorVsTrackEta_100p0")->Fill (fabs (eta), dzError);
              twoDHists_.at ("chargedHadrons/ptDeltaVsTrackEta_100p0")->Fill (fabs (eta), (ptDelta / genPt) * 100.0);
              twoDHists_.at ("chargedHadrons/d0DeltaVsTrackEta_100p0")->Fill (fabs (eta), d0Delta);
              twoDHists_.at ("chargedHadrons/dzDeltaVsTrackEta_100p0")->Fill (fabs (eta), dzDelta);
            }

          threeDHists_.at ("chargedHadrons/trackPtError")->Fill (eta, pt, (ptError / pt) * 100.0);
          threeDHists_.at ("chargedHadrons/trackD0Error")->Fill (eta, pt, d0Error);
          threeDHists_.at ("chargedHadrons/trackDzError")->Fill (eta, pt, dzError);
        }
      else
        {
          if (pt > 0.7)
            nFakeTracks++;
          twoDHists_.at ("fakeTracks/trackEtaVsTrackPt")->Fill (pt, eta);
          twoDHists_.at ("fakeTracks/trackPtVsTrackZ")->Fill (vz, pt);
          if (fabs (pt - 0.7) / 0.7 < 0.1)
            {
              twoDHists_.at ("fakeTracks/ptErrorVsTrackEta_0p7")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("fakeTracks/d0ErrorVsTrackEta_0p7")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("fakeTracks/dzErrorVsTrackEta_0p7")->Fill (fabs (eta), dzError);
            }
          if (fabs (pt - 1.0) / 1.0 < 0.1)
            {
              twoDHists_.at ("fakeTracks/ptErrorVsTrackEta_1p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("fakeTracks/d0ErrorVsTrackEta_1p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("fakeTracks/dzErrorVsTrackEta_1p0")->Fill (fabs (eta), dzError);
            }
          if (fabs (pt - 10.0) / 10.0 < 0.1)
            {
              twoDHists_.at ("fakeTracks/ptErrorVsTrackEta_10p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("fakeTracks/d0ErrorVsTrackEta_10p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("fakeTracks/dzErrorVsTrackEta_10p0")->Fill (fabs (eta), dzError);
            }
          if (fabs (pt - 50.0) / 50.0 < 0.1)
            {
              twoDHists_.at ("fakeTracks/ptErrorVsTrackEta_50p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("fakeTracks/d0ErrorVsTrackEta_50p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("fakeTracks/dzErrorVsTrackEta_50p0")->Fill (fabs (eta), dzError);
            }
          if (fabs (pt - 100.0) / 100.0 < 0.1)
            {
              twoDHists_.at ("fakeTracks/ptErrorVsTrackEta_100p0")->Fill (fabs (eta), (ptError / pt) * 100.0);
              twoDHists_.at ("fakeTracks/d0ErrorVsTrackEta_100p0")->Fill (fabs (eta), d0Error);
              twoDHists_.at ("fakeTracks/dzErrorVsTrackEta_100p0")->Fill (fabs (eta), dzError);
            }

          threeDHists_.at ("fakeTracks/trackPtError")->Fill (eta, pt, (ptError / pt) * 100.0);
          threeDHists_.at ("fakeTracks/trackD0Error")->Fill (eta, pt, d0Error);
          threeDHists_.at ("fakeTracks/trackDzError")->Fill (eta, pt, dzError);
        }


      for (const auto &hit : track.extra ()->recHits ())
        {
          int det = hit->geographicalId ().det (),
              subdetId = hit->geographicalId ().subdetId ();
          double xError = sqrt (hit->localPositionError ().xx ()),
                 yError = sqrt (hit->localPositionError ().yy ());

          if (det == DetId::Tracker && subdetId == PixelSubdetector::PixelBarrel)
            {
              oneDHists_.at ("bpixHitsVsTrackEta")->Fill (eta);
              twoDHists_.at ("bpixXErrorVsTrackEta")->Fill (fabs (eta), xError);
              twoDHists_.at ("bpixYErrorVsTrackEta")->Fill (fabs (eta), yError);
            }
          if (det == DetId::Tracker && subdetId == PixelSubdetector::PixelEndcap)
            {
              oneDHists_.at ("fpixHitsVsTrackEta")->Fill (eta);
              twoDHists_.at ("fpixXErrorVsTrackEta")->Fill (fabs (eta), xError);
              twoDHists_.at ("fpixYErrorVsTrackEta")->Fill (fabs (eta), yError);
            }
        }
    }*/
  oneDHists_.at ("nTracks")->Fill (nTracks);
  oneDHists_.at ("electrons/nTracks")->Fill (nElectrons);
  oneDHists_.at ("muons/nTracks")->Fill (nMuons);
  oneDHists_.at ("chargedHadrons/nTracks")->Fill (nChargedHadrons);
  oneDHists_.at ("fakeTracks/nTracks")->Fill (nFakeTracks);

  vector<reco::GenParticle> quarks;
  for (const auto &particle : *genParticles)
    {
      unsigned status = particle.status ();
      int pid = particle.pdgId ();

      bool isVBFquark = false ; 
      // cout << "Checking VBF status: " << pid << endl ; 
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
        quarks.push_back (particle);
    }

  for (const auto &quark : quarks)
    {
      if (quark.pt () < 30.0)
        continue;

      const reco::PFJet *closestJet = NULL;
      double closestJetDeltaR = -1.0;
      bool foundAJet = false;
      for (const auto &jet : *jets)
        {
          double dR, jetBeta;

          if (jet.pt () < 30.0)
            continue;

          dR = deltaR (quark, jet);

          if (dR > 0.4)
            continue;

          foundAJet = true;

          if (dR < closestJetDeltaR || !closestJet)
            {
              jetBeta = beta (jet, tracks, vertices);
              if (jetBeta < 0.1)
                continue;

              closestJetDeltaR = dR;
              closestJet = &jet;
            }
        }
      if (foundAJet)
        oneDHists_.at ("pvAssociationFactored/vbfQuarkEta")->Fill (fabs (quark.eta ()));
      if (closestJet)
        oneDHists_.at ("pvAssociationFactored/vbfJetsFound")->Fill (fabs (quark.eta ()));
      if (foundAJet && !closestJet && fabs (quark.eta ()) > 2.8 && fabs (quark.eta ()) < 3.0)
        cout << event.id () << endl;
    }
  for (const auto &quark : quarks)
    {
      if (quark.pt () < 30.0)
        continue;

      const reco::TrackJet *closestJet = NULL;
      double closestJetDeltaR = -1.0;
      bool foundAJet = false;
      for (const auto &jet : *trackJets)
        {
          double dR, jetBeta;

          if (jet.pt () < 30.0)
            continue;

          dR = deltaR (quark, jet);

          if (dR > 0.4)
            continue;

          foundAJet = true;

          if (dR < closestJetDeltaR || !closestJet)
            {
              jetBeta = beta (jet, tracks, vertices);
              if (jetBeta < 0.1)
                continue;

              closestJetDeltaR = dR;
              closestJet = &jet;
            }
        }
      if (foundAJet)
        oneDHists_.at ("pvAssociationFactored_TrackJets/vbfQuarkEta")->Fill (fabs (quark.eta ()));
      if (closestJet)
        oneDHists_.at ("pvAssociationFactored_TrackJets/vbfJetsFound")->Fill (fabs (quark.eta ()));
    }

  for (const auto &jet : *jets)
    {
      double pt = jet.pt (),
             eta = jet.eta ();

      if (pt < 100.0)
        continue;
      if (fabs (eta) > 5.0)
        continue;

      oneDHists_.at ("jetPt")->Fill (pt);
      oneDHists_.at ("jetEta")->Fill (eta);
    }
}

void
VFPixAnalyzer::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

void
VFPixAnalyzer::linSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (i);
}

bool
VFPixAnalyzer::isMatched (const reco::Track &track, const edm::Handle<vector<reco::GenParticle> > &genParticles, const unsigned id, const double maxDeltaR, const reco::GenParticle *&closest) const
{
  double minDeltaR = 999.9;
  closest = NULL;
  for (const auto &genParticle : *genParticles)
    {
      if (abs (genParticle.pdgId ()) != id
       || genParticle.status () != 1
       || genParticle.numberOfDaughters () != 0)
        continue;

      double dR = deltaR (track, genParticle);
      if (dR < minDeltaR)
        {
          minDeltaR = dR;
          closest = &genParticle;
        }

    }
  if (minDeltaR < maxDeltaR)
    return true;
  return false;
}

bool
VFPixAnalyzer::isMatched (const reco::Track &track, const edm::Handle<vector<SimTrack> > &simTracks, const double maxDeltaR, const SimTrack *&closest) const
{
  double minDeltaR = 999.9;
  closest = NULL;
  for (const auto &simTrack : *simTracks)
    {
      double dR = deltaR (track.eta (), track.phi (), simTrack.momentum ().Eta (), simTrack.momentum ().Phi ());
      if (dR < minDeltaR)
        {
          minDeltaR = dR;
          closest = &simTrack;
        }
    }
  if (minDeltaR < maxDeltaR)
    return true;
  return false;
}

double
VFPixAnalyzer::beta (const reco::PFJet &jet, const edm::Handle<vector<reco::Track> > &tracks, const edm::Handle<vector<reco::Vertex> > &vertices) const
{
  double sumptchpv = 0.0, sumptch = 0.0;
  for (const auto &track : *tracks)
    {
      if (track.pt () < 0.7)
        continue;
      if (deltaR (track, jet) > 0.4)
        continue;
      sumptch += track.pt ();
    }
  if (vertices->size () > 0)
    {
      for (auto track = vertices->at (0).tracks_begin (); track != vertices->at (0).tracks_end (); track++)
        {
          if ((*track)->pt () < 0.7)
            continue;
          if (deltaR (**track, jet) > 0.4)
            continue;
          sumptchpv += (*track)->pt ();
        }
    }

  return (sumptch > 0.0 ? (sumptchpv / sumptch) : -999.0);
}

double
VFPixAnalyzer::beta (const reco::TrackJet &jet, const edm::Handle<vector<reco::Track> > &tracks, const edm::Handle<vector<reco::Vertex> > &vertices) const
{
  double sumptchpv = 0.0, sumptch = 0.0;
  for (const auto &track : *tracks)
    {
      if (track.pt () < 0.7)
        continue;
      if (deltaR (track, jet) > 0.4)
        continue;
      sumptch += track.pt ();
    }
  if (vertices->size () > 0)
    {
      for (auto track = vertices->at (0).tracks_begin (); track != vertices->at (0).tracks_end (); track++)
        {
          if ((*track)->pt () < 0.7)
            continue;
          if (deltaR (**track, jet) > 0.4)
            continue;
          sumptchpv += (*track)->pt ();
        }
    }

  return (sumptch > 0.0 ? (sumptchpv / sumptch) : -999.0);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(VFPixAnalyzer);
