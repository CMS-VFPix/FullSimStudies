from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'TTbar_14TeV_step3_trackingOnly_921_PU200_OT613_200_IT4025_opt8s3l'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_RECO_VALIDATION_DQM_trackingOnly_PU200_OT613_200_IT4025_opt8s3l.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/TTbar_14TeV_921_OT613_200_IT4025_opt8s3l/jalimena-step2_PU200-99916c02f1fbb27bf5841f984462d465/USER'
config.Data.outputDatasetTag = 'step3_trackingOnly_PU200'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
