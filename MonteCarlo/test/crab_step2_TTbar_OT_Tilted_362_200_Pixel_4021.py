from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'TTbar_14TeV_step2_900pre4_PU140_OT_Tilted_362_200_Pixel_4021'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT_PU_OT_Tilted_362_200_Pixel_4021.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/TTbar_14TeV_900pre4_OT_Tilted_362_200_Pixel_4021/cmills-GenSim-fa8ce440575f3977a2938ba8914fc217/USER'
config.Data.outputDatasetTag = 'step2_PU200'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
