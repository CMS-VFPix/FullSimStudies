import FWCore.ParameterSet.Config as cms
import sys
import math

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('VFPIX')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
  input = cms.untracked.int32 (-1)
)
process.source = cms.Source ('PoolSource',
  fileNames = cms.untracked.vstring ('root://xrootd-cms.infn.it///store/mc/TP2023HGCALDR/VBF_HToTauTau_M-125_14TeV-powheg-pythia6/GEN-SIM-RECO/HGCALnewsplit_PU140BX25_newsplitPU140_PH2_1K_FB_V6-v2/00000/02BD6259-AEF9-E411-8447-00A0D1EEF204.root')
)

process.DelphesVertexProducer = cms.EDProducer ('DelphesVertexProducer',
  tracks = cms.InputTag ("generalTracks", ""),
  sigma = cms.double (2.0),
  minPT = cms.double (0.7),
  maxEta = cms.double (10.0),
  seedMinPT = cms.double (0.7),
  minNDF = cms.int32 (4),
  growSeeds = cms.int32 (1),
)

process.PoolOutputModule = cms.OutputModule ("PoolOutputModule",
  splitLevel = cms.untracked.int32 (0),
  eventAutoFlushCompressedSize = cms.untracked.int32 (5242880),
  fileName = cms.untracked.string ("delphesVertices.root"),
  outputCommands = cms.untracked.vstring (
    'keep *',
  ),
  dropMetaData = cms.untracked.string ("ALL")
)

process.myPath = cms.Path (process.DelphesVertexProducer)
process.myEndPath = cms.EndPath (process.PoolOutputModule)
