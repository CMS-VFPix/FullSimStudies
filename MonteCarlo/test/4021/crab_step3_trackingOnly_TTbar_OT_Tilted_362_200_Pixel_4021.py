from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'TTbar_14TeV_step3_trackingOnly_900pre4_PU200'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_PAT_VALIDATION_DQM_trackingOnly_PU200_OT_Tilted_362_200_Pixel_4021.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/TTbar_14TeV_900pre4_OT_Tilted_362_200_Pixel_4021/cmills-step2_PU200-b39198357157f4c214229970743e2f88/USER'
#config.Data.outputDatasetTag = 'step3_trackingOnly_PU140'
config.Data.outputDatasetTag = 'step3_trackingOnly_PU200'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.blacklist = ["T2_US_UCSD"]
config.Site.storageSite = 'T3_US_FNALLPC'
