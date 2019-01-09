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
    input = cms.untracked.int32(5)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:step2_PU140.root'
        '/store/group/lpcfpix/TTbar_14TeV_GEN_SIM_900pre4_OT_Tilted_362_200_Pixel_4021_dropLargeRespace/TTbar_14TeV_step2_900pre4_PU140_OT_Tilted_362_200_Pixel_4021_dropLargeRespace/170314_092230/0000/step2_PU140_1.root'
        ),
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
process.mix.input.fileNames = cms.untracked.vstring([
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_1.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_16.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_2.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_23.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_24.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_25.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_26.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_27.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_29.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_3.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_30.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_31.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_33.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_4.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_42.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_43.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_44.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_45.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_46.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_47.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_48.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_49.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_5.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_50.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_51.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_52.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_53.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_54.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_55.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_56.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_57.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_58.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_59.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_60.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_61.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_62.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_63.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_64.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_65.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_66.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_67.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_68.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_69.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_70.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_71.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_72.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_73.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_74.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_75.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_76.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_77.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_78.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_79.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_80.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_81.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_82.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_83.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_84.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_85.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_86.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_87.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_88.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_89.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_90.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_91.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_92.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_93.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_94.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_95.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_96.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_97.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_98.root',
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_99.root',
])
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
inputDir = "VFPix/MonteCarlo/data/OT_Tilted_362_200_Pixel_4021_dropLargeRespace/"
fileNames =["pixbar.xml","pixel.xml","pixelProdCuts.xml","pixelStructureTopology.xml","pixelsens.xml","pixfwd.xml","tracker.xml","trackerProdCuts.xml","trackerRecoMaterial.xml","trackerStructureTopology.xml","trackersens.xml"]
for i in range (0, len (process.XMLIdealGeometryESSource.geomXMLFiles)):
	xmlFile = process.XMLIdealGeometryESSource.geomXMLFiles[i]
	fileName = xmlFile.split("/")[-1]
	if fileName in fileNames:
		process.XMLIdealGeometryESSource.geomXMLFiles[i] = inputDir + fileName
