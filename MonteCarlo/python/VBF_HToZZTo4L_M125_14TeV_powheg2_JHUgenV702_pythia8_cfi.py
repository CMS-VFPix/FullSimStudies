import FWCore.ParameterSet.Config as cms

# link to cards
# https://github.com/amagitte/genproductions/blob/9d23e15b6079d6417f84b3a0f3ad1d5ac6fffd54/bin/Powheg/production/V2/14TeV/Higgs/VBF_H_JHUGen_HZZ4L_NNPDF30_14TeV/VBF_H_M125_NNPDF30_14TeV.input
# https://github.com/amagitte/genproductions/blob/fe666f1200df881f0e1eab3ea1a4ebf3b7dc1e40/bin/Powheg/production/V2/14TeV/Higgs/VBF_H_JHUGen_HZZ4L_NNPDF30_14TeV/JHUGen_VBF_H_ZZ4L.input

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/14TeV/powheg/V2/VBF_HZZ4L_NNPDF30_14TeV_M125_JHUGenV702/v2/VBF_HZZ4L_NNPDF30_14TeV_M125_JHUGenV702.tgz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

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
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'processParameters'
                                    )
        )
                         )
