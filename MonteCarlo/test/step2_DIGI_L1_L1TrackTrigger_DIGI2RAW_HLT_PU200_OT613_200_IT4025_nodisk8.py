# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step2 --conditions auto:phase2_realistic --pileup_input das:/RelValMinBias_14TeV/1/GEN-SIM -n 10 --era Phase2C2 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@fake2 --datatier GEN-SIM-DIGI-RAW --pileup AVE_200_BX_25ns --geometry Extended2023D17 --filein file:step1.root --fileout file:step2.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Phase2C2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake2_cff')
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
process.mix.input.nbPileupEvents.averageNumber = cms.double(200.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-3)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring([
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_1.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_10.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_100.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_11.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_12.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_13.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_14.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_15.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_16.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_17.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_18.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_19.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_2.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_20.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_21.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_22.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_23.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_24.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_25.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_26.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_27.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_28.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_29.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_3.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_30.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_31.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_32.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_33.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_34.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_35.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_36.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_37.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_38.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_39.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_4.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_40.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_41.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_42.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_43.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_44.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_45.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_46.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_47.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_48.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_49.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_5.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_50.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_51.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_52.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_53.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_54.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_55.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_56.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_57.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_58.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_59.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_6.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_60.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_61.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_62.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_63.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_64.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_65.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_66.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_67.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_68.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_69.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_7.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_70.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_71.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_72.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_73.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_74.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_75.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_76.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_77.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_78.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_79.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_8.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_80.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_81.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_82.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_83.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_84.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_85.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_86.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_87.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_88.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_89.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_9.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_90.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_91.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_92.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_93.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_94.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_95.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_96.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_97.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_98.root',
'/store/user/lpcfpix/MinBias_14TeV_923_OT613_200_IT4025_nodisk8/GenSim/181203_093211/0000/step1_99.root',
])
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
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

inputDir = "VFPix/MonteCarlo/data/OT613_200_IT4025_nodisk8/"
fileNames =["pixbar.xml","pixelProdCuts.xml","pixelStructureTopology.xml","pixelsens.xml","pixfwd.xml","tracker.xml","trackerProdCuts.xml","trackerRecoMaterial.xml","trackerStructureTopology.xml","trackersens.xml","pixel.xml"]
for i in range (0, len (process.XMLIdealGeometryESSource.geomXMLFiles)):
        xmlFile = process.XMLIdealGeometryESSource.geomXMLFiles[i]
        fileName = xmlFile.split("/")[-1]
        if fileName in fileNames:
            process.XMLIdealGeometryESSource.geomXMLFiles[i] = inputDir + fileName
