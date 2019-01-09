# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step4 --conditions auto:phase2_realistic -s HARVESTING:@phase2Validation+@phase2+@miniAODValidation+@miniAODDQM --pileup_input /store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_1.root -n 10 --era Phase2C2 --filein file:step3_RAW2DIGI_L1Reco_RECO_PAT_VALIDATION_DQM_PU_inDQM.root --scenario pp --pileup AVE_140_BX_25ns --filetype DQM --geometry Extended2023D4 --mc --no_exec
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
    fileNames = cms.untracked.vstring('file:step3_RAW2DIGI_L1Reco_RECO_PAT_VALIDATION_DQM_PU_inDQM.root')
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
process.mix.input.fileNames = cms.untracked.vstring([
'/store/group/lpcfpix/MinBias_dropLargeRespace/crab_MinBias_dropLargeRespace/170222_201635/0000/step1_1.root'
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
process.dqmHarvesting = cms.Path(process.DQMOffline_SecondStep+process.DQMOffline_Certification)
process.postValidation_common_step = cms.Path(process.postValidation_common)
process.postValidationTracking_step = cms.Path(process.postValidationTracking)
process.postValidation_muons_step = cms.Path(process.postValidation_muons)
process.postValidation_JetMET_step = cms.Path(process.postValidation_JetMET)
process.bTagCollectorSequenceMCbcl_step = cms.Path(process.bTagCollectorSequenceMCbcl)
process.postValidation_HCAL_step = cms.Path(process.postValidation_HCAL)
process.DQMHarvestTracking_step = cms.Path(process.DQMHarvestTracking)
process.DQMHarvestMuon_step = cms.Path(process.DQMHarvestMuon)
process.DQMCertMuon_step = cms.Path(process.DQMCertMuon)
process.DQMHarvestHcal_step = cms.Path(process.DQMHarvestHcal)
process.HcalDQMOfflinePostProcessor_step = cms.Path(process.HcalDQMOfflinePostProcessor)
process.DQMHarvestEGamma_step = cms.Path(process.DQMHarvestEGamma)
process.DQMHarvestMiniAOD_step = cms.Path(process.DQMHarvestMiniAOD)
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(process.postValidation_common_step,process.postValidationTracking_step,process.postValidation_muons_step,process.postValidation_JetMET_step,process.bTagCollectorSequenceMCbcl_step,process.postValidation_HCAL_step,process.DQMHarvestTracking_step,process.DQMHarvestMuon_step,process.DQMCertMuon_step,process.DQMHarvestHcal_step,process.HcalDQMOfflinePostProcessor_step,process.DQMHarvestEGamma_step,process.validationHarvestingMiniAOD,process.DQMHarvestMiniAOD_step,process.dqmsave_step)


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
