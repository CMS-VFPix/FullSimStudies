import FWCore.ParameterSet.Config as cms

# link to card #FIXME:
# https://github.com/cms-sw/genproductions/blob/cbd9f361d33cfe95b76668588168103e986126ff/bin/Powheg/production/V2/13TeV/Higgs/VBF_H_NNPDF30_13TeV/VBF_H_NNPDF30_13TeV_M-125.input

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    ## args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/VBF_H_NNPDF30_13TeV_M125/v1/VBFH_NNPDF30_M-125_13TeV_tarball.tar.gz'),
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/14TeV/powheg/V2/VBFH_NNPDF30_M-125_14TeV/v2/VBFH_NNPDF30_M-125_14TeV_tarball.tgz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

# FIX ME!!
# https://github.com/cms-sw/genproductions/blob/310c3d77c1062b46004c6d253ebf5437ff5858fa/python/ThirteenTeV/Higgs/Hadronizer_TuneCUETP8M1_13TeV_powhegEmissionVeto_3p_HToBB_M-125_LHE_pythia8_cff.py

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(14000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        pythia8PowhegEmissionVetoSettingsBlock,
        processParameters = cms.vstring(
            'POWHEG:nFinal = 3',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 5 -5',
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'processParameters'
                                    )
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)