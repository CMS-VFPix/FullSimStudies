#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_set>

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/DetId/interface/DetId.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"

#include "SimDataFormats/TrackingHit/interface/PSimHit.h"

#include "VFPix/FullSimStudies/plugins/SimHitAnalyzer.h"

SimHitAnalyzer::SimHitAnalyzer (const edm::ParameterSet &cfg) :
  simHitsBarrelHighTof_ (cfg.getParameter<edm::InputTag> ("simHitsBarrelHighTof")),
  simHitsBarrelLowTof_ (cfg.getParameter<edm::InputTag> ("simHitsBarrelLowTof")),
  simHitsEndcapHighTof_ (cfg.getParameter<edm::InputTag> ("simHitsEndcapHighTof")),
  simHitsEndcapLowTof_ (cfg.getParameter<edm::InputTag> ("simHitsEndcapLowTof"))
{
  TH1::SetDefaultSumw2 ();

  twoDHists_["rhoPhi"] = fs_->make<TH2D> ("rhoPhi", ";x [cm];y [cm]", 500, 0.0, 20.0, 500, 0.0, 20.0);
  twoDHists_["rhoZ"] = fs_->make<TH2D> ("rhoZ", ";z [cm];#rho [cm]", 500, 0.0, 300.0, 500, 0.0, 20.0);

  simHitsBarrelHighTofToken_ = consumes<vector<PSimHit> > (simHitsBarrelHighTof_);
  simHitsBarrelLowTofToken_ = consumes<vector<PSimHit> > (simHitsBarrelLowTof_);
  simHitsEndcapHighTofToken_ = consumes<vector<PSimHit> > (simHitsEndcapHighTof_);
  simHitsEndcapLowTofToken_ = consumes<vector<PSimHit> > (simHitsEndcapLowTof_);
}

SimHitAnalyzer::~SimHitAnalyzer ()
{
}

void
SimHitAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<PSimHit> > simHitsBarrelHighTof;
  event.getByToken (simHitsBarrelHighTofToken_, simHitsBarrelHighTof);
  edm::Handle<vector<PSimHit> > simHitsBarrelLowTof;
  event.getByToken (simHitsBarrelLowTofToken_, simHitsBarrelLowTof);
  edm::Handle<vector<PSimHit> > simHitsEndcapHighTof;
  event.getByToken (simHitsEndcapHighTofToken_, simHitsEndcapHighTof);
  edm::Handle<vector<PSimHit> > simHitsEndcapLowTof;
  event.getByToken (simHitsEndcapLowTofToken_, simHitsEndcapLowTof);

  edm::ESHandle<TrackerGeometry> theTrackerGeometry;
  setup.get<TrackerDigiGeometryRecord> ().get (theTrackerGeometry);
  const TrackerGeometry &theTracker (*theTrackerGeometry);

  for (const auto &simHit : *simHitsBarrelHighTof)
    {
      DetId theDetUnitId (simHit.detUnitId ());
      const GeomDet *theDet = theTracker.idToDet (theDetUnitId);

      double x, y, z;
      x = theDet->surface ().toGlobal (simHit.localPosition ()).x ();
      y = theDet->surface ().toGlobal (simHit.localPosition ()).y ();
      z = theDet->surface ().toGlobal (simHit.localPosition ()).z ();

      twoDHists_.at ("rhoPhi")->Fill (x, y);
      twoDHists_.at ("rhoZ")->Fill (z, hypot (x, y));
    }
  for (const auto &simHit : *simHitsBarrelLowTof)
    {
      DetId theDetUnitId (simHit.detUnitId ());
      const GeomDet *theDet = theTracker.idToDet (theDetUnitId);

      double x, y, z;
      x = theDet->surface ().toGlobal (simHit.localPosition ()).x ();
      y = theDet->surface ().toGlobal (simHit.localPosition ()).y ();
      z = theDet->surface ().toGlobal (simHit.localPosition ()).z ();

      twoDHists_.at ("rhoPhi")->Fill (x, y);
      twoDHists_.at ("rhoZ")->Fill (z, hypot (x, y));
    }
  for (const auto &simHit : *simHitsEndcapHighTof)
    {
      DetId theDetUnitId (simHit.detUnitId ());
      const GeomDet *theDet = theTracker.idToDet (theDetUnitId);

      double x, y, z;
      x = theDet->surface ().toGlobal (simHit.localPosition ()).x ();
      y = theDet->surface ().toGlobal (simHit.localPosition ()).y ();
      z = theDet->surface ().toGlobal (simHit.localPosition ()).z ();

      twoDHists_.at ("rhoZ")->Fill (z, hypot (x, y));
    }
  for (const auto &simHit : *simHitsEndcapLowTof)
    {
      DetId theDetUnitId (simHit.detUnitId ());
      const GeomDet *theDet = theTracker.idToDet (theDetUnitId);

      double x, y, z;
      x = theDet->surface ().toGlobal (simHit.localPosition ()).x ();
      y = theDet->surface ().toGlobal (simHit.localPosition ()).y ();
      z = theDet->surface ().toGlobal (simHit.localPosition ()).z ();

      twoDHists_.at ("rhoZ")->Fill (z, hypot (x, y));
    }
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(SimHitAnalyzer);
