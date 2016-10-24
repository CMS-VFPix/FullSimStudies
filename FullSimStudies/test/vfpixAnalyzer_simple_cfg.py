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
#  fileNames = cms.untracked.vstring ('/store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/81X_mcRun2_asymptotic_v8_2023D1-v1/00000/3800737E-1083-E611-8885-0025905A60A8.root',)
  fileNames = cms.untracked.vstring ('/store/relval/CMSSW_8_1_0_pre12/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/00000/00970C32-B983-E611-A0D8-0025905B8566.root')
#  fileNames = cms.untracked.vstring ('file:singleMuPt100.root')
)



process.VFPixAnalyzer = cms.EDAnalyzer ('VFPixAnalyzer',
  jets = cms.InputTag ("ak4PFCHSJets", ""),
  jetsNoCHS = cms.InputTag ("ak4PFJets", ""),
  trackJets = cms.InputTag ("ak5TrackJets", ""),
  pus = cms.InputTag ("addPileupInfo", ""),
  vertices = cms.InputTag ("offlinePrimaryVertices", ""),
  tracks = cms.InputTag ("generalTracks", ""),
  genParticles = cms.InputTag ("genParticles", ""),
  simTracks = cms.InputTag ("g4SimHits", ""),
  pfCandidates = cms.InputTag ("particleFlow", ""),
)

process.myPath = cms.Path (process.VFPixAnalyzer)
