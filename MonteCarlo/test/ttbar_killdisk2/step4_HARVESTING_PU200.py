# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step4 --conditions auto:phase2_realistic -s HARVESTING:@phase2Validation+@phase2+@miniAODValidation+@miniAODDQM --era Phase2C2 --filein file:step3_inDQM.root --scenario pp --filetype DQM --geometry Extended2023D17 --mc -n 200 --fileout file:step4.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HARVESTING',eras.Phase2C2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DQMSaverAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

# Input source
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring('file:step3_inDQM.root')
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('FULLMERGE')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step4 nevts:200'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

process.mix.input.nbPileupEvents.averageNumber = cms.double(200.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-3)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring([
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/0646FF72-D4A6-E711-B5C6-0025905A6060.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/4E8BEB5D-CFA6-E711-A91D-0CC47A4C8E86.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/5A84EF72-D4A6-E711-9C56-0025905B85FC.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/645914CF-C9A6-E711-9543-0CC47A7C3610.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/70A4DC8F-CBA6-E711-8F8C-0025905B856E.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/70DB2B46-D0A6-E711-B3CF-0025905A60B6.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/94421F10-CEA6-E711-866D-0CC47A4D7630.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/AA74F12C-C9A6-E711-AC09-0025905A612A.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/B434C293-CCA6-E711-84F3-0025905B856E.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/F20388C1-D0A6-E711-A346-0CC47A7C3610.root',
'/store/relval/CMSSW_9_3_2/RelValMinBias_14TeV/GEN-SIM/93X_upgrade2023_realistic_v2_2023D17noPU-v1/10000/FA70BC2A-CDA6-E711-B289-0CC47A4D7630.root'
])

# Path and EndPath definitions
process.dqmHarvestingFakeHLT = cms.Path(process.DQMOffline_SecondStep_FakeHLT+process.DQMOffline_Certification)
process.validationHarvestingHI = cms.Path(process.postValidationHI)
process.alcaHarvesting = cms.Path()
process.validationHarvestingNoHLT = cms.Path(process.postValidation+process.postValidation_gen)
process.validationHarvestingFS = cms.Path(process.postValidation+process.hltpostvalidation+process.postValidation_gen)
process.validationpreprodHarvesting = cms.Path(process.postValidation_preprod+process.hltpostvalidation_preprod+process.postValidation_gen)
process.genHarvesting = cms.Path(process.postValidation_gen)
process.validationprodHarvesting = cms.Path(process.hltpostvalidation_prod+process.postValidation_gen)
process.validationHarvesting = cms.Path(process.postValidation+process.hltpostvalidation+process.postValidation_gen)
process.validationpreprodHarvestingNoHLT = cms.Path(process.postValidation_preprod+process.postValidation_gen)
process.dqmHarvestingPOGMC = cms.Path(process.DQMOffline_SecondStep_PrePOGMC)
process.dqmHarvesting = cms.Path(process.DQMOffline_SecondStep+process.DQMOffline_Certification)
process.postValidation_common_step = cms.Path(process.postValidation_common)
process.postValidationTracking_step = cms.Path(process.postValidationTracking)
process.postValidation_muons_step = cms.Path(process.postValidation_muons)
process.postValidation_JetMET_step = cms.Path(process.postValidation_JetMET)
process.bTagCollectorSequenceMCbcl_step = cms.Path(process.bTagCollectorSequenceMCbcl)
process.postValidation_HCAL_step = cms.Path(process.postValidation_HCAL)
process.DQMHarvestTracking_step = cms.Path(process.DQMHarvestTracking)
process.DQMHarvestOuterTracker_step = cms.Path(process.DQMHarvestOuterTracker)
process.DQMHarvestMuon_step = cms.Path(process.DQMHarvestMuon)
process.DQMCertMuon_step = cms.Path(process.DQMCertMuon)
process.DQMHarvestHcal_step = cms.Path(process.DQMHarvestHcal)
process.HcalDQMOfflinePostProcessor_step = cms.Path(process.HcalDQMOfflinePostProcessor)
process.DQMHarvestEGamma_step = cms.Path(process.DQMHarvestEGamma)
process.DQMHarvestMiniAOD_step = cms.Path(process.DQMHarvestMiniAOD)
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(process.postValidation_common_step,process.postValidationTracking_step,process.postValidation_muons_step,process.postValidation_JetMET_step,process.bTagCollectorSequenceMCbcl_step,process.postValidation_HCAL_step,process.DQMHarvestTracking_step,process.DQMHarvestOuterTracker_step,process.DQMHarvestMuon_step,process.DQMCertMuon_step,process.DQMHarvestHcal_step,process.HcalDQMOfflinePostProcessor_step,process.DQMHarvestEGamma_step,process.validationHarvestingMiniAOD,process.DQMHarvestMiniAOD_step,process.dqmsave_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
