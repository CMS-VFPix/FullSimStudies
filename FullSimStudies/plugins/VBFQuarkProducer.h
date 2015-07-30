#ifndef VBF_QUARK_PRODUCER
#define VBF_QUARK_PRODUCER

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class VBFQuarkProducer : public edm::EDProducer
{
  public:
    VBFQuarkProducer (const edm::ParameterSet &);
    ~VBFQuarkProducer ();

    void produce (edm::Event &, const edm::EventSetup &);

  private:
    edm::InputTag genParticles_;
    edm::InputTag jets_;
    edm::InputTag tracks_;
};

#endif
