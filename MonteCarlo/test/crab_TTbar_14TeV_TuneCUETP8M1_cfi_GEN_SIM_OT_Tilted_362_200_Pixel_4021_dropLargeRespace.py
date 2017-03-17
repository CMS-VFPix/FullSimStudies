from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'TTbar_14TeV_GEN_SIM_900pre4_OT_Tilted_362_200_Pixel_4021_dropLargeRespace'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'TTbar_14TeV_TuneCUETP8M1_cfi_GEN_SIM_OT_Tilted_362_200_Pixel_4021_dropLargeRespace.py'

config.Data.outputPrimaryDataset = 'TTbar_14TeV_OT_Tilted_362_200_Pixel_4021_dropLargeRespace_900pre4'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True
config.Site.storageSite = 'T3_US_FNALLPC'
