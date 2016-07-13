import FWCore.ParameterSet.Config as cms
import sys
import math
import os

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('VFPixAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.TFileService = cms.Service ('TFileService',
  fileName = cms.string ("output.root")
)
process.maxEvents = cms.untracked.PSet (
  input = cms.untracked.int32 (-1)
)
process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring ('/store/user/ahart/VBF_HToZZTo4L_M_125_TuneZ2star_14TeV_pythia6_tauola_FPix800x52/PH2_1K_FB_V6_HLLHCBS_140-v1/160329_175458/0000/step3_1.root',)
)

process.load ("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load ('Configuration.Geometry.GeometryExtended2023MuonReco_cff')
process.load ('Configuration.Geometry.GeometryExtended2023Muon_cff')
process.load ("Configuration.StandardSequences.MagneticField_cff")
process.load ('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'DES23_62_V1::All'

#from CommonTools.RecoAlgos.sortedPrimaryVertices_cfi import *
#process.betterOfflinePrimaryVertices=sortedPrimaryVertices.clone(jets = "ak5CaloJets")

process.load("CondCore.DBCommon.CondDBCommon_cfi")
from CondCore.DBCommon.CondDBSetup_cfi import *
process.jec = cms.ESSource("PoolDBESSource",
      DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
      timetype = cms.string('runnumber'),
      toGet = cms.VPSet(
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag    = cms.string('JetCorrectorParametersCollection_PhaseII_HGCal140PU_AK4PFchs'),
          label  = cms.untracked.string('AK4PFchs')
        ),
        cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag    = cms.string('JetCorrectorParametersCollection_PhaseII_HGCal140PU_AK4PF'),
          label  = cms.untracked.string('AK4PF')
        ),
      ## here you add as many jet types as you need
      ## note that the tag name is specific for the particular sqlite file 
      ), 
      connect = cms.string('sqlite_file:'+os.environ['CMSSW_BASE'] + '/src/VFPix/FullSimStudies/test/PhaseII_HGCal140PU.db')
)
## add an es_prefer statement to resolve a possible conflict from simultaneous connection to a global tag
process.es_prefer_jec = cms.ESPrefer('PoolDBESSource','jec')

process.load("JetMETCorrections.Configuration.JetCorrectionServices_cff")
process.load("JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff")
process.ak4PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6PFJets","rho"),
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet')
)
process.ak4PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)
process.ak4PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)
process.ak4PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Fastjet', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute')
)
process.ak4PFCHSJetsL1FastL2L3   = cms.EDProducer('PFJetCorrectionProducer',
    src         = cms.InputTag('ak4PFJetsCHS'),
    correctors  = cms.vstring('ak4PFCHSL1FastL2L3')
)

process.ak4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    srcRho = cms.InputTag("kt6PFJets","rho"),
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet')
)
process.ak4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)
process.ak4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)
process.ak4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute')
)
process.ak4PFJetsL1FastL2L3   = cms.EDProducer('PFJetCorrectionProducer',
    src         = cms.InputTag('ak4PFJets'),
    correctors  = cms.vstring('ak4PFL1FastL2L3')
)

process.VFPixAnalyzer = cms.EDAnalyzer ('VFPixAnalyzer',
  jets = cms.InputTag ("ak4PFCHSJetsL1FastL2L3", ""),
  jetsNoCHS = cms.InputTag ("ak4PFJetsL1FastL2L3", ""),
  trackJets = cms.InputTag ("ak5TrackJets", ""),
  pus = cms.InputTag ("addPileupInfo", ""),
  vertices = cms.InputTag ("offlinePrimaryVertices", ""),
  tracks = cms.InputTag ("generalTracks", ""),
  genParticles = cms.InputTag ("genParticles", ""),
  simTracks = cms.InputTag ("g4SimHits", ""),
  pfCandidates = cms.InputTag ("particleFlow", ""),
)

process.VFPixAnalyzerWithSortedPVs = cms.EDAnalyzer ('VFPixAnalyzer',
  jets = cms.InputTag ("ak4PFCHSJetsL1FastL2L3", ""),
  jetsNoCHS = cms.InputTag ("ak4PFJetsL1FastL2L3", ""),
  trackJets = cms.InputTag ("ak5TrackJets", ""),
  pus = cms.InputTag ("addPileupInfo", ""),
  vertices = cms.InputTag ("betterOfflinePrimaryVertices", ""),
  tracks = cms.InputTag ("generalTracks", ""),
  genParticles = cms.InputTag ("genParticles", ""),
  simTracks = cms.InputTag ("g4SimHits", ""),
  pfCandidates = cms.InputTag ("particleFlow", ""),
)

process.delphesVertices = cms.EDProducer ('DelphesVertexProducer',
  tracks = cms.InputTag ("generalTracks", ""),
  sigma = cms.double (2.0),
  minPT = cms.double (0.7),
  maxEta = cms.double (10.0),
  seedMinPT = cms.double (0.7),
  minNDF = cms.int32 (4),
  growSeeds = cms.int32 (1),
)

process.VFPixAnalyzerWithDelphesVertices = cms.EDAnalyzer ('VFPixAnalyzer',
  jets = cms.InputTag ("ak4PFCHSJetsL1FastL2L3", ""),
  jetsNoCHS = cms.InputTag ("ak4PFJetsL1FastL2L3", ""),
  trackJets = cms.InputTag ("ak5TrackJets", ""),
  pus = cms.InputTag ("addPileupInfo", ""),
  vertices = cms.InputTag ("delphesVertices", ""),
  tracks = cms.InputTag ("generalTracks", ""),
  genParticles = cms.InputTag ("genParticles", ""),
  simTracks = cms.InputTag ("g4SimHits", ""),
  pfCandidates = cms.InputTag ("particleFlow", ""),
)

#process.myPath = cms.Path (process.betterOfflinePrimaryVertices*process.ak4PFCHSJetsL1FastL2L3*process.ak4PFJetsL1FastL2L3*process.VFPixAnalyzer*process.VFPixAnalyzerWithSortedPVs*process.delphesVertices*process.VFPixAnalyzerWithDelphesVertices)
process.myPath = cms.Path (process.ak4PFCHSJetsL1FastL2L3*process.ak4PFJetsL1FastL2L3*process.VFPixAnalyzer)
