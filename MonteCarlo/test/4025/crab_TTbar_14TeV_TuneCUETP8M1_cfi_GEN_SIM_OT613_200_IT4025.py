from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'TTbar_14TeV_GenSim_OT613_200_IT4025'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'TTbar_14TeV_TuneCUETP8M1_cfi_GEN_SIM_OT613_200_IT4025.py'

config.Data.outputPrimaryDataset = 'TTbar_14TeV_932_OT613_200_IT4025'
config.Data.outputDatasetTag = 'GenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
