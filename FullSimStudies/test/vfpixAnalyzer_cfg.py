fileNames = [
  #'root://xrootd-cms.infn.it///store/mc/TP2023SHCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/SHCALJan23_PU140BX25_PH2_1K_FB_V6-v1/00000/04FCCE66-7FA5-E411-B282-002590D0AFF2.root',
  #'root://xrootd-cms.infn.it///store/mc/TP2023SHCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/SHCALJan23_PU140BX25_PH2_1K_FB_V6-v1/00000/0A6FDF5E-27A4-E411-B46D-E0CB4E29C4C8.root',
  #'root://xrootd-cms.infn.it///store/mc/TP2023SHCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/SHCALJan23_PU140BX25_PH2_1K_FB_V6-v1/00000/0EC643D1-F0A3-E411-AF5D-002590D0AF78.root',
  #'root://xrootd-cms.infn.it///store/mc/TP2023SHCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/SHCALJan23_PU140BX25_PH2_1K_FB_V6-v1/00000/1229581F-F5A3-E411-BA81-20CF305B0599.root',
  #'root://xrootd-cms.infn.it///store/mc/TP2023SHCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/SHCALJan23_PU140BX25_PH2_1K_FB_V6-v1/00000/14E7ED8A-01A4-E411-9CD6-00259073E35A.root',
  #'root://xrootd-cms.infn.it///store/mc/TP2023SHCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/SHCALJan23_PU140BX25_PH2_1K_FB_V6-v1/00000/169A4E1D-27A4-E411-802C-002590D0AFF2.root',
  #'root://xrootd-cms.infn.it///store/mc/TP2023SHCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/SHCALJan23_PU140BX25_PH2_1K_FB_V6-v1/00000/2098C15C-26A4-E411-A916-E0CB4E29C4F7.root',
  #'root://xrootd-cms.infn.it///store/mc/TP2023SHCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/SHCALJan23_PU140BX25_PH2_1K_FB_V6-v1/00000/246D86C4-F3A3-E411-9F5A-E0CB4E29C4FC.root',
  #'root://xrootd-cms.infn.it///store/mc/TP2023SHCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/SHCALJan23_PU140BX25_PH2_1K_FB_V6-v1/00000/2840136D-19A4-E411-94B7-5254009A38FA.root',

  'file:btaggedEvents0.root'
]

import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('VFPixAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.TFileService = cms.Service ('TFileService',
  fileName = cms.string ('vbfHToTauTau.root')
)
process.maxEvents = cms.untracked.PSet (
  input = cms.untracked.int32 (-1)
)
process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring (fileNames)
)

process.VFPixAnalyzer = cms.EDAnalyzer ('VFPixAnalyzer',
  jets = cms.InputTag ("ak4PFJetsCHS", ""),
  pus = cms.InputTag ("addPileupInfo", ""),
  vertices = cms.InputTag ("offlinePrimaryVertices", ""),
  tracks = cms.InputTag ("generalTracks", ""),
  genParticles = cms.InputTag ("genParticles", ""),
  simTracks = cms.InputTag ("g4SimHits", ""),
)

process.myPath = cms.Path (process.VFPixAnalyzer)
