from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'VBF_HToZZTo4L_M125_14TeV_LHE_GEN_SIM_OT_Tilted_362_200_Pixel_4021_dropSmallRespace'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'VBF_HToZZTo4L_M125_14TeV_powheg2_JHUgenV702_pythia8_LHE_GEN_SIM_OT_Tilted_362_200_Pixel_4021_dropSmallRespace.py'

config.Data.outputPrimaryDataset = 'VBF_HToZZTo4L_14TeV_900pre4_OT_Tilted_362_200_Pixel_4021_dropSmallRespace'
config.Data.outputDatasetTag = 'LheGenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
