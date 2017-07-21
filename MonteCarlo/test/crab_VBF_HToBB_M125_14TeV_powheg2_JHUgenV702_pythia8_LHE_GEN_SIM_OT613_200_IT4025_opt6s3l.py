from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()


config.General.requestName = 'VBF_HToBB_M125_14TeV_LHE_GEN_SIM_OT613_200_IT4025_opt6s3l'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'VBF_HToBB_M125_14TeV_powheg2_JHUgenV702_pythia8_LHE_GEN_SIM_OT613_200_IT4025_opt6s3l.py'

config.Data.outputPrimaryDataset = 'VBF_HToBB_14TeV_923_OT613_200_IT4025_opt6s3l'
config.Data.outputDatasetTag = 'LheGenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
