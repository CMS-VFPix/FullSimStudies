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
  outputFile = "/afs/cern.ch/user/a/ahart/T3/VBFHToTauTau_noTrkExt"
  print "using the scenario without the tracker extension..."
if scenario == "trkExt":
  files = fileNames.trkExt
  outputFile = "/afs/cern.ch/user/a/ahart/T3/VBFHToTauTau_trkExt"
  print "using the scenario with the tracker extension..."

filesPerJob = int (math.ceil (len (files) / float (nJobs)))
files = files[(jobNumber * filesPerJob):((jobNumber + 1) * filesPerJob)]
print "job " + str (jobNumber) + "/" + str (nJobs) + " will process " + str (len (files)) + " files..."

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('VFPIX')
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

process.PileupProducer = cms.EDProducer ('PileupProducer',
  tracks = cms.InputTag ("generalTracks", ""),
  pfCandidates = cms.InputTag ("particleFlow", ""),
  genParticles = cms.InputTag ("genParticles", ""),
  simTracks = cms.InputTag ("g4SimHits", ""),
)

process.PoolOutputModule = cms.OutputModule ("PoolOutputModule",
  splitLevel = cms.untracked.int32 (0),
  eventAutoFlushCompressedSize = cms.untracked.int32 (5242880),
  fileName = cms.untracked.string ("" + outputFile + str (jobNumber) + ".root"),
  outputCommands = cms.untracked.vstring (
    'drop *',
    'keep *_PileupProducer_*_*',
    'keep PileupSummaryInfos_addPileupInfo_*_*',
    'keep recoGenParticles_genParticles_*_*',
  ),
  dropMetaData = cms.untracked.string ("ALL")
)

process.myPath = cms.Path (process.PileupProducer)
process.myEndPath = cms.EndPath (process.PoolOutputModule)
