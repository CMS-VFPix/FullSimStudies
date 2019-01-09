from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'FourMuExtended_dropLargeRespace'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'FourMuExtendedPt_1_200_pythia8_cfi_GEN_SIM_OT_Tilted_362_200_Pixel_4021_dropLargeRespace.py'

config.Data.outputPrimaryDataset = 'FourMuExtended_14TeV_900pre4_OT_Tilted_362_200_Pixel_4021_dropLargeRespace'
config.Data.outputDatasetTag = 'GenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
NJOBS = 5  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = False

config.Site.storageSite = 'T3_US_FNALLPC'
