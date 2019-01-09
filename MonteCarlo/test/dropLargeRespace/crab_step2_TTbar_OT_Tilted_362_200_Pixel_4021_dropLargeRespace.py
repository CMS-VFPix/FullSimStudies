from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


#config.General.requestName = 'TTbar_14TeV_step2_900pre4_PU140_OT_Tilted_362_200_Pixel_4021_dropLargeRespace'
config.General.requestName = 'TTbar_14TeV_step2_900pre4_PU200_OT_Tilted_362_200_Pixel_4021_dropLargeRespace_dupMatRemoved'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'step2_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT_PU140_OT_Tilted_362_200_Pixel_4021_dropLargeRespace.py'
config.JobType.psetName = 'step2_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT_PU200_OT_Tilted_362_200_Pixel_4021_dropLargeRespace.py'
config.JobType.maxMemoryMB = 4000

#config.Data.inputDataset = '/TTbar_14TeV_GEN_SIM_900pre4_OT_Tilted_362_200_Pixel_4021_dropLargeRespace/jalimena-crab_TTbar_14TeV_GEN_SIM_900pre4_OT_Tilted_362_200_Pixel_4021_dropLargeRespace-83d2b6da0996944bae2d6bc716cce958/USER'
config.Data.inputDataset = '/TTbar_14TeV_900pre4_OT_Tilted_362_200_Pixel_4021_dropLargeRespace_duplicateMaterialRemoved/jalimena-GenSim-83d2b6da0996944bae2d6bc716cce958/USER'
#config.Data.outputDatasetTag = 'step2_PU140'
config.Data.outputDatasetTag = 'step2_PU200'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.whitelist = ["T1_US_FNAL"]
config.Site.storageSite = 'T3_US_FNALLPC'
