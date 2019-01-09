from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'VBF_HToBB_14TeV_step3_923_PU200_OT613_200_IT4025_nodisk1_BTagEta2p4To4p0'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RAW2DIGI_RECO_VALIDATION_DQM_PU200_OT613_200_IT4025_nodisk1.py'
config.JobType.maxMemoryMB = 8000

config.Data.inputDataset = '/VBF_HToBB_14TeV_923_OT613_200_IT4025_nodisk1/jalimena-step2_PU200-23dba3775f05c13a4d52ca3ddadced1e/USER'
config.Data.outputDatasetTag = 'step3_PU200_BTagEta2p4To4p0'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
