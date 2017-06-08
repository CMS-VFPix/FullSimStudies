from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'TTbar_14TeV_step2_921_PU200_OT613_200_IT4025_opt8s3l'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT_PU200_OT613_200_IT4025_opt8s3l.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/TTbar_14TeV_921_OT613_200_IT4025_opt8s3l/jalimena-GenSim-e2677be2d3a81ef7e2a31dd2df03ad44/USER'
config.Data.outputDatasetTag = 'step2_PU200'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
