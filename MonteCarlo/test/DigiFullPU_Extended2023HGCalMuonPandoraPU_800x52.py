# Auto generated configuration file
# using: 
# Revision: 1.20 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions PH2_1K_FB_V6::All --pileup_input das:/RelValMinBias_TuneZ2star_14TeV/CMSSW_6_2_0_SLHC26_patch4-PH2_1K_FB_V6_HLLHCBS-v1/GEN-SIM -n 10 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW --datatier GEN-SIM-DIGI-RAW --pileup AVE_140_BX_25ns --customise RecoParticleFlow/PandoraTranslator/customizeHGCalPandora_cff.cust_2023HGCalPandoraMuon --geometry Extended2023HGCalMuon,Extended2023HGCalMuonReco --magField 38T_PostLS1 --io DigiFullPU_Extended2023HGCalMuonPandoraPU.io --python DigiFullPU_Extended2023HGCalMuonPandoraPU.py --no_exec --filein file:step1.root --fileout file:step2.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('DIGI2RAW')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023HGCalMuonReco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:step1.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    fileName = cms.untracked.string('file:step2_40x52.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW')
    )
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(140.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/06C1EE58-E178-E511-AA98-0025905A48D6.root', '/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/0A1749E7-DF78-E511-9540-0025905A60D2.root', '/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/0A8EE1A3-E178-E511-A0A8-0025905964A2.root', '/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/0C9EE226-E778-E511-9C8A-0025905B859E.root', '/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/0EFF697A-E078-E511-8997-0025905A497A.root', '/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/8E4A142B-E778-E511-8B72-0025905A6138.root', '/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/BCA33BEE-E378-E511-A63A-0025905964B6.root', '/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/BE421FA9-E578-E511-A04B-0025905A60B4.root', '/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/D4C8C3B5-E378-E511-99AE-0025905A48D6.root', '/store/relval/CMSSW_6_2_0_SLHC26_patch4/RelValMinBias_TuneZ2star_14TeV/GEN-SIM/PH2_1K_FB_V6_HLLHCBS-v1/00000/E06DB90C-E178-E511-8E11-0025905B8572.root'])
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PH2_1K_FB_V6::All', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.FEVTDEBUGHLToutput_step)

# customisation of the process.

# Automatic addition of the customisation function from RecoParticleFlow.PandoraTranslator.customizeHGCalPandora_cff
from RecoParticleFlow.PandoraTranslator.customizeHGCalPandora_cff import cust_2023HGCalPandoraMuon 

#call to customisation function cust_2023HGCalPandoraMuon imported from RecoParticleFlow.PandoraTranslator.customizeHGCalPandora_cff
process = cust_2023HGCalPandoraMuon(process)

for i in range (0, len (process.XMLIdealGeometryESSource.geomXMLFiles)):
    xmlFile = process.XMLIdealGeometryESSource.geomXMLFiles[i]
    if not xmlFile.endswith ("trackerStructureTopology_800x52.xml"):
        continue
    process.XMLIdealGeometryESSource.geomXMLFiles[i] = "VFPix/MonteCarlo/data/trackerStructureTopology_800x52.xml"

# End of customisation functions
