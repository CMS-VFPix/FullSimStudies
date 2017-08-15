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
        cms.PSet(Dead_detID = cms.int32(352588804), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588808), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588812), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588816), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588820), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588824), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588828), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588832), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588836), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588840), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588844), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588848), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588852), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588856), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588860), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588864), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588868), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588872), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588876), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352588880), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592900), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592904), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592908), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592912), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592916), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592920), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592924), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592928), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592932), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592936), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592940), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592944), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592948), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592952), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592956), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592960), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592964), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592968), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592972), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592976), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592980), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592984), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592988), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592992), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352592996), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352593000), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352593004), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352593008), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352593012), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352593016), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352593020), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352593024), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352596996), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597000), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597004), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597008), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597012), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597016), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597020), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597024), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597028), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597032), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597036), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597040), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597044), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597048), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597052), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597056), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597060), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597064), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597068), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597072), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597076), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597080), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597084), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352597088), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601092), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601096), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601100), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601104), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601108), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601112), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601116), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601120), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601124), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601128), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601132), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601136), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601140), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601144), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601148), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601152), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601156), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601160), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601164), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601168), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601172), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601176), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601180), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601184), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601188), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601192), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601196), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601200), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601204), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601208), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601212), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352601216), Module = cms.string('whole')),
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
