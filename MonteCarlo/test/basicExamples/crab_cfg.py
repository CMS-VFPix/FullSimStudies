from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'vbf_fpix80x52'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'VBF_HToZZTo4L_M_125_TuneZ2star_14TeV_pythia6_tauola_Extended2023HGCalMuonPandoraPU_GenSimHLBeamSpotFull_80x52.py'

config.Data.outputPrimaryDataset = 'VBF_HToZZTo4L_M_125_TuneZ2star_14TeV_pythia6_tauola_FPix80x52'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
NJOBS = 5000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CMSSW_6_2_0_SLHC26_patch4-PH2_1K_FB_V6_HLLHCBS_140-v1'

config.Site.storageSite = 'T2_US_Purdue'
