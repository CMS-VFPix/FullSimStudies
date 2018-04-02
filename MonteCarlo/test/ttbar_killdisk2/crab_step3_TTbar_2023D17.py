from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'TTbar_14TeV_step3_932_PU200_2023D17_OT613_IT4025'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_PAT_VALIDATION_DQM_PU200_OT613_IT4025.py'
config.JobType.maxMemoryMB = 16000
config.JobType.numCores = 4

config.Data.inputDataset = '/TTbar_14TeV_932_OT613_200_IT4025/jalimena-step2_PU200_deadFPix2pos-15b244caa00a89f5ae32cac14dfe5cce/USER'
config.Data.outputDatasetTag = 'step3_PU200_deadFPix2pos_noTrackingChange'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
