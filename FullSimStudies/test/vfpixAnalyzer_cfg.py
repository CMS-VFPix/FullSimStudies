import FWCore.ParameterSet.Config as cms
import sys
import math

import VFPix.FullSimStudies.fileNames_cfg as fileNames

jobNumber = int (sys.argv[2])
#jobNumber = 0
nJobs = int (sys.argv[3])
#nJobs = 8
scenario = sys.argv[4]
#scenario = "noTrkExt"

files = []
outputFile = ""
if scenario == "noTrkExt":
  files = fileNames.noTrkExt
  outputFile = "vbfHToTauTau_withJEC_noTrkExt"
  print "using the scenario without the tracker extension..."
if scenario == "trkExt":
  files = fileNames.trkExt
  outputFile = "vbfHToTauTau_withJEC_trkExt"
  print "using the scenario with the tracker extension..."
if scenario == "trkExt_HToMuMu":
  files = fileNames.trkExt_HToMuMu
  outputFile = "vbfHToMuMu_withJEC_trkExt"
  print "using the HToMuMu scenario with the tracker extension..."

filesPerJob = int (math.ceil (len (files) / float (nJobs)))
files = files[(jobNumber * filesPerJob):((jobNumber + 1) * filesPerJob)]
print "job " + str (jobNumber) + "/" + str (nJobs) + " will process " + str (len (files)) + " files..."

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('VFPixAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.TFileService = cms.Service ('TFileService',
  fileName = cms.string (outputFile + str (jobNumber) + ".root")
)
process.maxEvents = cms.untracked.PSet (
  input = cms.untracked.int32 (-1)
)
process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring (files)
)

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
      ## here you add as many jet types as you need
      ## note that the tag name is specific for the particular sqlite file 
      ), 
      connect = cms.string('sqlite:PhaseII_HGCal140PU.db')
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

process.VFPixAnalyzer = cms.EDAnalyzer ('VFPixAnalyzer',
  jets = cms.InputTag ("ak4PFCHSJetsL1FastL2L3", ""),
  trackJets = cms.InputTag ("ak5TrackJets", ""),
  pus = cms.InputTag ("addPileupInfo", ""),
  vertices = cms.InputTag ("offlinePrimaryVertices", ""),
  tracks = cms.InputTag ("generalTracks", ""),
  genParticles = cms.InputTag ("genParticles", ""),
  simTracks = cms.InputTag ("g4SimHits", ""),
)

process.myPath = cms.Path (process.ak4PFCHSJetsL1FastL2L3*process.VFPixAnalyzer)
