# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:phase2_realistic -s DIGI:pdigi_valid,L1,L1TrackTrigger,DIGI2RAW,HLT:@fake2 --datatier GEN-SIM-DIGI-RAW -n 10 --geometry Extended2023D17 --era Phase2C2 --eventcontent FEVTDEBUGHLT --filein file:step1.root --fileout file:step2.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Phase2C2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
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
    input = cms.untracked.int32(500)
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
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
process.mix.digitizers.pixel.PixelDigitizerAlgorithm.KillModules = True

dead=cms.VPSet()
dead.extend([ 
        cms.PSet(Dead_detID = cms.int32(353899524), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899528), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899532), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899536), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899540), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899544), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899548), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899552), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899556), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899560), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899564), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899568), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899572), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899576), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899580), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899584), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899588), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899592), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899596), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353899600), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903620), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903624), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903628), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903632), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903636), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903640), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903644), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903648), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903652), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903656), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903660), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903664), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903668), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903672), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903676), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903680), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903684), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903688), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903692), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903696), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903700), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903704), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903708), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903712), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903716), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903720), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903724), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903728), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903732), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903736), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903740), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353903744), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907716), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907720), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907724), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907728), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907732), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907736), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907740), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907744), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907748), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907752), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907756), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907760), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907764), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907768), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907772), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907776), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907780), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907784), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907788), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907792), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907796), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907800), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907804), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353907808), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911812), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911816), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911820), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911824), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911828), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911832), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911836), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911840), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911844), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911848), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911852), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911856), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911860), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911864), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911868), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911872), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911876), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911880), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911884), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911888), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911892), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911896), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911900), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911904), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911908), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911912), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911916), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911920), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911924), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911928), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911932), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(353911936), Module = cms.string('whole')),
        ]);

process.mix.digitizers.pixel.PixelDigitizerAlgorithm.DeadModules = dead
        
# process.mix.digitizers.pixel.SiPixelSimBlock.DeadModules = cms.VPSet(dead)
        
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
