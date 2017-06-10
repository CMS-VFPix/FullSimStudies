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
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/user/lpcfpix/TTbar_14TeV_921_OT613_200_IT4025/step2_PU200/170608_155443/0000/step2_999.root'),
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

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:step3.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
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
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_1.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_10.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_100.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_11.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_12.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_13.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_14.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_15.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_16.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_17.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_18.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_19.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_2.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_20.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_21.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_22.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_23.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_24.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_25.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_26.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_27.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_28.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_29.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_3.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_30.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_31.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_32.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_33.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_34.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_35.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_36.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_37.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_38.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_39.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_4.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_40.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_41.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_42.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_43.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_44.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_45.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_46.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_47.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_48.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_49.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_5.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_50.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_51.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_52.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_53.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_54.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_55.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_56.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_57.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_58.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_59.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_6.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_60.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_61.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_62.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_63.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_64.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_65.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_66.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_67.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_68.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_69.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_7.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_70.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_71.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_72.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_73.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_74.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_75.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_76.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_77.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_78.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_79.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_8.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_80.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_81.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_82.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_83.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_84.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_85.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_86.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_87.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_88.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_89.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_9.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_90.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_91.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_92.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_93.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_94.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_95.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_96.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_97.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_98.root',
'/store/group/lpcfpix/MinBias_14TeV_921_OT613_200_IT4025_opt8s3l/GenSim/170607_174647/0000/step1_99.root',
])
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
process.prevalidation_step = cms.Path(process.globalPrevalidationTrackingOnly)
process.validation_step = cms.EndPath(process.globalValidationTrackingOnly)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineTracking)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.RECOSIMoutput_step,process.DQMoutput_step)
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


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

inputDir = "VFPix/MonteCarlo/data/OT613_200_IT4025_opt8s3l/"
fileNames =["pixbar.xml","pixel.xml","pixelProdCuts.xml","pixelStructureTopology.xml","pixelsens.xml","pixfwd.xml","tracker.xml","trackerProdCuts.xml","trackerRecoMaterial.xml","trackerStructureTopology.xml","trackersens.xml"]
for i in range (0, len (process.XMLIdealGeometryESSource.geomXMLFiles)):
        xmlFile = process.XMLIdealGeometryESSource.geomXMLFiles[i]
        fileName = xmlFile.split("/")[-1]
        if fileName in fileNames:
            process.XMLIdealGeometryESSource.geomXMLFiles[i] = inputDir + fileName


