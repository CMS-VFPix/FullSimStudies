# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase2_realistic --pileup_input das:/RelValMinBias_14TeV/1/GEN-SIM --pileup AVE_200_BX_25ns -n 10 --era Phase2C2 --eventcontent RECOSIM,DQM --runUnscheduled -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry Extended2023D17 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Phase2C2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/user/lpcfpix/TTbar_14TeV_923_OT613_200_IT4025_opt6s3l/step2_PU200/170624_081654/0000/step2_999.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

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
    fileName = cms.untracked.string('file:step3.root'),
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
    fileName = cms.untracked.string('file:step3_inMINIAODSIM.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(200.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-3)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring([
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_1.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_10.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_100.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_11.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_12.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_13.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_14.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_15.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_16.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_17.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_18.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_19.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_2.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_20.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_21.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_22.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_23.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_24.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_25.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_26.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_27.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_28.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_29.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_3.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_30.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_31.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_32.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_33.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_34.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_35.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_36.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_37.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_38.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_39.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_4.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_40.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_41.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_42.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_43.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_44.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_45.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_46.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_47.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_48.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_49.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_5.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_50.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_51.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_52.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_53.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_54.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_55.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_56.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_57.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_58.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_59.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_6.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_60.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_61.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_62.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_63.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_64.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_65.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_66.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_67.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_68.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_69.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_7.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_70.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_71.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_72.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_73.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_74.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_75.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_76.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_77.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_78.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_79.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_8.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_80.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_81.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_82.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_83.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_84.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_85.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_86.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_87.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_88.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_89.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_9.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_90.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_91.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_92.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_93.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_94.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_95.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_96.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_97.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_98.root',
'/store/group/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_opt6s3l/GenSim/170721_051411/0000/step1_99.root',
])
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

#change b-tagging to look at 2.4<eta<4 jets
process.bTagCommonBlock.etaMin = cms.double(2.4)
process.bTagHarvest.etaMin = cms.double(2.4)
process.bTagHarvestMC.etaMin = cms.double(2.4)
process.bTagAnalysis.etaMin = cms.double(2.4)
process.bTagValidation.etaMin = cms.double(2.4)
process.bTagValidationNoall.etaMin = cms.double(2.4)

process.bTagCommonBlock.etaMax = cms.double(4.0)
process.bTagHarvest.etaMax = cms.double(4.0)
process.bTagHarvestMC.etaMax = cms.double(4.0)
process.bTagAnalysis.etaMax = cms.double(4.0)
process.bTagValidation.etaMax = cms.double(4.0)
process.bTagValidationNoall.etaMax = cms.double(4.0)

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path()
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path()
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_HBHENoiseFilter = cms.Path()
process.Flag_trkPOG_toomanystripclus53X = cms.Path()
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path()
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.prevalidation_step = cms.Path(process.baseCommonPreValidation)
process.prevalidation_step1 = cms.Path(process.globalPrevalidationTracking)
process.prevalidation_step2 = cms.Path(process.globalPrevalidationMuons)
process.prevalidation_step3 = cms.Path(process.globalPrevalidationJetMETOnly)
process.prevalidation_step4 = cms.Path(process.prebTagSequenceMC)
process.prevalidation_step5 = cms.Path(process.globalPrevalidationHCAL)
process.prevalidation_step6 = cms.Path(process.prevalidationMiniAOD)
process.validation_step = cms.EndPath(process.baseCommonValidation)
process.validation_step1 = cms.EndPath(process.globalValidationTrackingOnly)
process.validation_step2 = cms.EndPath(process.globalValidationMuons)
process.validation_step3 = cms.EndPath(process.globalValidationJetMETonly)
process.validation_step4 = cms.EndPath(process.bTagPlotsMCbcl)
process.validation_step5 = cms.EndPath(process.globalValidationHCAL)
process.validation_step6 = cms.EndPath(process.validationMiniAOD)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineTracking)
process.dqmoffline_1_step = cms.EndPath(process.DQMOuterTracker)
process.dqmoffline_2_step = cms.EndPath(process.DQMOfflineMuon)
process.dqmoffline_3_step = cms.EndPath(process.DQMOfflineHcal)
process.dqmoffline_4_step = cms.EndPath(process.HcalDQMOfflineSequence)
process.dqmoffline_5_step = cms.EndPath(process.DQMOfflineEGamma)
process.dqmoffline_6_step = cms.EndPath(process.DQMOfflineMiniAOD)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.dqmofflineOnPAT_1_step = cms.EndPath(process.PostDQMOfflineMiniAOD)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.prevalidation_step,process.prevalidation_step1,process.prevalidation_step2,process.prevalidation_step3,process.prevalidation_step4,process.prevalidation_step5,process.prevalidation_step6,process.validation_step,process.validation_step1,process.validation_step2,process.validation_step3,process.validation_step4,process.validation_step5,process.validation_step6,process.dqmoffline_step,process.dqmoffline_1_step,process.dqmoffline_2_step,process.dqmoffline_3_step,process.dqmoffline_4_step,process.dqmoffline_5_step,process.dqmoffline_6_step,process.dqmofflineOnPAT_step,process.dqmofflineOnPAT_1_step,process.FEVTDEBUGHLToutput_step,process.MINIAODSIMoutput_step,process.DQMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.
# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

inputDir = "VFPix/MonteCarlo/data/OT613_200_IT4025_opt6s3l/"
fileNames =["pixbar.xml","pixel.xml","pixelProdCuts.xml","pixelStructureTopology.xml","pixelsens.xml","pixfwd.xml","tracker.xml","trackerProdCuts.xml","trackerRecoMaterial.xml","trackerStructureTopology.xml","trackersens.xml"]
for i in range (0, len (process.XMLIdealGeometryESSource.geomXMLFiles)):
        xmlFile = process.XMLIdealGeometryESSource.geomXMLFiles[i]
        fileName = xmlFile.split("/")[-1]
        if fileName in fileNames:
            process.XMLIdealGeometryESSource.geomXMLFiles[i] = inputDir + fileName


