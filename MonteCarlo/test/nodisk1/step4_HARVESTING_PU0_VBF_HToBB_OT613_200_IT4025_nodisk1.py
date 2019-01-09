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
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DQMSaverAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring([
'file:step3_inDQM.root',
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

inputDir = "VFPix/MonteCarlo/data/OT613_200_IT4025_nodisk1/"
fileNames =["pixbar.xml","pixel.xml","pixelProdCuts.xml","pixelStructureTopology.xml","pixelsens.xml","pixfwd.xml","tracker.xml","trackerProdCuts.xml","trackerRecoMaterial.xml","trackerStructureTopology.xml","trackersens.xml"]
for i in range (0, len (process.XMLIdealGeometryESSource.geomXMLFiles)):
        xmlFile = process.XMLIdealGeometryESSource.geomXMLFiles[i]
        fileName = xmlFile.split("/")[-1]
        if fileName in fileNames:
            process.XMLIdealGeometryESSource.geomXMLFiles[i] = inputDir + fileName
