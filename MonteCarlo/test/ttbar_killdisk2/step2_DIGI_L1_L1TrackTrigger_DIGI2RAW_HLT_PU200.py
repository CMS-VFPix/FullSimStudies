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
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
process.mix.digitizers.pixel.PixelDigitizerAlgorithm.KillModules = True

dead=cms.VPSet()
dead.extend([
        cms.PSet(Dead_detID = cms.int32(352850948), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850952), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850956), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850960), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850964), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850968), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850972), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850976), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850980), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850984), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850988), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850992), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352850996), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352851000), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352851004), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352851008), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352851012), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352851016), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352851020), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352851024), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855044), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855048), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855052), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855056), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855060), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855064), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855068), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855072), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855076), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855080), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855084), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855088), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855092), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855096), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855100), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855104), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855108), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855112), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855116), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855120), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855124), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855128), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855132), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855136), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855140), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855144), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855148), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855152), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855156), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855160), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855164), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352855168), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859140), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859144), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859148), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859152), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859156), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859160), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859164), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859168), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859172), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859176), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859180), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859184), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859188), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859192), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859196), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859200), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859204), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859208), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859212), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859216), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859220), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859224), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859228), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352859232), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863236), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863240), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863244), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863248), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863252), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863256), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863260), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863264), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863268), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863272), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863276), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863280), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863284), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863288), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863292), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863296), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863300), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863304), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863308), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863312), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863316), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863320), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863324), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863328), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863332), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863336), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863340), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863344), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863348), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863352), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863356), Module = cms.string('whole')),
        cms.PSet(Dead_detID = cms.int32(352863360), Module = cms.string('whole')),
        ]);

process.mix.digitizers.pixel.PixelDigitizerAlgorithm.DeadModules = dead

# process.mix.digitizers.pixel.SiPixelSimBlock.DeadModules = cms.VPSet(dead)

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
