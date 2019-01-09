from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'VBF_HToBB_14TeV_step2_923_PU200_OT613_200_IT4025_opt7s4l'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT_PU200_OT613_200_IT4025_opt7s4l.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/VBF_HToBB_14TeV_923_OT613_200_IT4025_opt7s4l/jalimena-LheGenSim_RAWSIMoutput-57f8a4feebcf5dce70d7fad4f66c9f9e/USER'
config.Data.outputDatasetTag = 'step2_PU200'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
