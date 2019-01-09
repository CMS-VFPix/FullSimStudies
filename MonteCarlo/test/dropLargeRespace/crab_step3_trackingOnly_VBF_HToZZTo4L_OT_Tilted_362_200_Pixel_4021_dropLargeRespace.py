from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'VBF_HToZZTo4L_14TeV_step3_trackingOnly_900pre4_PU200_dropLargeRespace'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_PAT_VALIDATION_DQM_trackingOnly_PU200_OT_Tilted_362_200_Pixel_4021_dropLargeRespace.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/VBF_HToZZTo4L_14TeV_900pre4_OT_Tilted_362_200_Pixel_4021_dropLargeRespace/jalimena-step2_PU200-175b7864029fdedb456f1063baf0d493/USER'
config.Data.outputDatasetTag = 'step3_trackingOnly_PU200'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
