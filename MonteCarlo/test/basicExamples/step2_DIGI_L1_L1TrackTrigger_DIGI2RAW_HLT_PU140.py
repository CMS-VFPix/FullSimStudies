# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:phase2_realistic --pileup_input das:/RelValMinBias_14TeV/CMSSW_9_0_0_pre4-90X_upgrade2023_realistic_v3_2023D4Timing-v1/GEN-SIM -n 10 --era Phase2C2 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,L1TrackTrigger,DIGI2RAW,HLT:@fake --datatier GEN-SIM-DIGI-RAW --pileup AVE_140_BX_25ns --geometry Extended2023D4 --filein file:step1.root --fileout file:step2.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Phase2C2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D4Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:step1.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(10485760),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(140.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/2093C03F-86EC-E611-A92E-0025905A6092.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/2AE8141B-84EC-E611-874D-0025905A48C0.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/32F79DB9-8BEC-E611-8900-0CC47A4D767E.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/46899547-7EEC-E611-9A7C-0025905B85DA.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/5269E346-81EC-E611-9964-0CC47A4D7604.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/549C9A1D-82EC-E611-8B33-0CC47A4D7604.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/6A1EE0C1-87EC-E611-9700-0025905A6092.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/7C0D2846-7EEC-E611-AD8E-0CC47A4C8EB0.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/A0138BBD-83EC-E611-98A6-0025905B85DA.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/A4E80C79-8BEC-E611-B2C7-0CC47A74525A.root'])
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.L1TrackTrigger_step = cms.Path(process.L1TrackTrigger)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.L1TrackTrigger_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
