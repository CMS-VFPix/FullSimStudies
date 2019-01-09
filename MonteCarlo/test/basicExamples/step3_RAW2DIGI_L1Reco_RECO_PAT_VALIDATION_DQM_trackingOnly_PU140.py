# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase2_realistic -n 10 --era Phase2C2 --eventcontent FEVTDEBUGHLT,MINIAODSIM,DQM --runUnscheduled -s RAW2DIGI,L1Reco,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO --geometry Extended2023D4 --filein file:step2_PU140.root --pileup_input das:/RelValMinBias_14TeV/CMSSW_9_0_0_pre4-90X_upgrade2023_realistic_v3_2023D4Timing-v1/GEN-SIM --pileup AVE_140_BX_25ns
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Phase2C2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D4Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step2_PU140.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(10485760),
    fileName = cms.untracked.string('step3_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('step3_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU_inMINIAODSIM.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('step3_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(140.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/2093C03F-86EC-E611-A92E-0025905A6092.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/2AE8141B-84EC-E611-874D-0025905A48C0.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/32F79DB9-8BEC-E611-8900-0CC47A4D767E.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/46899547-7EEC-E611-9A7C-0025905B85DA.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/5269E346-81EC-E611-9964-0CC47A4D7604.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/549C9A1D-82EC-E611-8B33-0CC47A4D7604.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/6A1EE0C1-87EC-E611-9700-0025905A6092.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/7C0D2846-7EEC-E611-AD8E-0CC47A4C8EB0.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/A0138BBD-83EC-E611-98A6-0025905B85DA.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/A4E80C79-8BEC-E611-B2C7-0CC47A74525A.root'])
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
process.prevalidation_step = cms.Path(process.globalPrevalidationTrackingOnly)
process.validation_step = cms.EndPath(process.globalValidationTrackingOnly)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineTracking)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.FEVTDEBUGHLToutput_step,process.MINIAODSIMoutput_step,process.DQMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn 

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
