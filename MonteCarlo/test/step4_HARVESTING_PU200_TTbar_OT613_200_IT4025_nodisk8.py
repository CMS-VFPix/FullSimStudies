# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step4 --conditions auto:phase2_realistic -s HARVESTING:@phase2Validation+@phase2+@miniAODValidation+@miniAODDQM --era Phase2C2 --filein file:step3_inDQM.root --scenario pp --filetype DQM --geometry Extended2023D17 --mc -n 100 --fileout file:step4.root
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
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring([
])
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('FULLMERGE')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step4 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(200.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-3)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring([
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_1.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_10.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_100.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_11.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_12.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_13.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_14.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_15.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_16.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_17.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_18.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_19.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_2.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_20.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_21.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_22.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_23.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_24.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_25.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_26.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_27.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_28.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_29.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_3.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_30.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_31.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_32.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_33.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_34.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_35.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_36.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_37.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_38.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_39.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_4.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_40.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_41.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_42.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_43.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_44.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_45.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_46.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_47.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_48.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_49.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_5.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_50.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_51.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_52.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_53.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_54.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_55.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_56.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_57.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_58.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_59.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_6.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_60.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_61.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_62.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_63.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_64.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_65.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_66.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_67.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_68.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_69.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_7.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_70.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_71.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_72.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_73.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_74.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_75.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_76.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_77.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_78.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_79.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_8.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_80.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_81.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_82.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_83.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_84.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_85.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_86.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_87.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_88.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_89.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_9.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_90.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_91.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_92.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_93.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_94.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_95.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_96.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_97.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_98.root',
'/eos/uscms/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_99.root',
])

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

#change b-tagging to look at 2.4<eta<4 jets
process.bTagCommonBlock.etaMin = cms.double(2.4)
process.bTagCollectorDATA.etaMin = cms.double(2.4)
process.bTagCollectorMC.etaMin = cms.double(2.4)
process.bTagCollectorMCbcl.etaMin = cms.double(2.4)
process.bTagHarvest.etaMin = cms.double(2.4)
process.bTagHarvestMC.etaMin = cms.double(2.4)
process.bTagAnalysis.etaMin = cms.double(2.4)
process.bTagValidation.etaMin = cms.double(2.4)
process.bTagValidationNoall.etaMin = cms.double(2.4)

process.bTagCommonBlock.etaMax = cms.double(4.0)
process.bTagCollectorDATA.etaMax = cms.double(4.0)
process.bTagCollectorMC.etaMax = cms.double(4.0)
process.bTagCollectorMCbcl.etaMax = cms.double(4.0)
process.bTagHarvest.etaMax = cms.double(4.0)
process.bTagHarvestMC.etaMax = cms.double(4.0)
process.bTagAnalysis.etaMax = cms.double(4.0)
process.bTagValidation.etaMax = cms.double(4.0)
process.bTagValidationNoall.etaMax = cms.double(4.0)

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

from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

inputDir = "VFPix/MonteCarlo/data/OT613_200_IT4025_nodisk8/"
fileNames =["pixbar.xml","pixel.xml","pixelProdCuts.xml","pixelStructureTopology.xml","pixelsens.xml","pixfwd.xml","tracker.xml","trackerProdCuts.xml","trackerRecoMaterial.xml","trackerStructureTopology.xml","trackersens.xml"]
for i in range (0, len (process.XMLIdealGeometryESSource.geomXMLFiles)):
        xmlFile = process.XMLIdealGeometryESSource.geomXMLFiles[i]
        fileName = xmlFile.split("/")[-1]
        if fileName in fileNames:
            process.XMLIdealGeometryESSource.geomXMLFiles[i] = inputDir + fileName
