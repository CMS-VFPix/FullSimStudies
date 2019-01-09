from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'VBF_HToZZTo4L_14TeV_step2_900pre4_PU200_OT_Tilted_362_200_Pixel_4021'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT_PU_OT_Tilted_362_200_Pixel_4021.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/VBF_HToZZTo4L_14TeV_900pre4_OT_Tilted_362_200_Pixel_4021/jalimena-LheGenSim-8b58b86aefc768372f32dd3a9e13a840/USER'
config.Data.outputDatasetTag = 'step2_PU200'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
