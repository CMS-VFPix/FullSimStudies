# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step4 --conditions auto:phase2_realistic -s HARVESTING:@trackingOnlyValidation+@trackingOnlyDQM --pileup_input das:/RelValMinBias_14TeV/CMSSW_9_0_0_pre4-90X_upgrade2023_realistic_v3_2023D4Timing-v1/GEN-SIM -n 10 --era Phase2C2 --filein file:step3_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU_inDQM.root --scenario pp --pileup AVE_140_BX_25ns --filetype DQM --geometry Extended2023D4 --mc
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HARVESTING',eras.Phase2C2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D4Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DQMSaverAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring('file:step3_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU_inDQM.root')
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('FULLMERGE')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step4 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(140.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/2093C03F-86EC-E611-A92E-0025905A6092.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/2AE8141B-84EC-E611-874D-0025905A48C0.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/32F79DB9-8BEC-E611-8900-0CC47A4D767E.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/46899547-7EEC-E611-9A7C-0025905B85DA.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/5269E346-81EC-E611-9964-0CC47A4D7604.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/549C9A1D-82EC-E611-8B33-0CC47A4D7604.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/6A1EE0C1-87EC-E611-9700-0025905A6092.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/7C0D2846-7EEC-E611-AD8E-0CC47A4C8EB0.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/A0138BBD-83EC-E611-98A6-0025905B85DA.root', '/store/relval/CMSSW_9_0_0_pre4/RelValMinBias_14TeV/GEN-SIM/90X_upgrade2023_realistic_v3_2023D4Timing-v1/10000/A4E80C79-8BEC-E611-B2C7-0CC47A74525A.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# Path and EndPath definitions
process.validationHarvestingHI = cms.Path(process.postValidationHI)
process.alcaHarvesting = cms.Path()
process.validationHarvestingFS = cms.Path(process.postValidation+process.hltpostvalidation+process.postValidation_gen)
process.validationpreprodHarvesting = cms.Path(process.postValidation_preprod+process.hltpostvalidation_preprod+process.postValidation_gen)
process.genHarvesting = cms.Path(process.postValidation_gen)
process.dqmHarvestingPOG = cms.Path(process.DQMOffline_SecondStep_PrePOG)
process.validationprodHarvesting = cms.Path(process.hltpostvalidation_prod+process.postValidation_gen)
process.validationHarvesting = cms.Path(process.postValidation+process.hltpostvalidation+process.postValidation_gen)
process.dqmHarvestingPOGMC = cms.Path(process.DQMOffline_SecondStep_PrePOGMC)
process.dqmHarvestingFakeHLT = cms.Path(process.DQMOffline_SecondStep_FakeHLT+process.DQMOffline_Certification)
process.validationHarvestingMiniAOD = cms.Path(process.JetPostProcessor+process.METPostProcessorHarvesting+process.postValidationMiniAOD)
process.dqmHarvesting = cms.Path(process.DQMOffline_SecondStep+process.DQMOffline_Certification)
process.postValidation_trackingOnly_step = cms.Path(process.postValidation_trackingOnly)
process.DQMHarvestTracking_step = cms.Path(process.DQMHarvestTracking)
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(process.postValidation_trackingOnly_step,process.DQMHarvestTracking_step,process.dqmsave_step)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
