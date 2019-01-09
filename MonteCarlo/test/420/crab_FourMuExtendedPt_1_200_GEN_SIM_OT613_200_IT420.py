from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'FourMuExtendedPt_1_200_GEN_SIM_OT613_200_IT420'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'FourMuExtendedPt_1_200_pythia8_cfi_GEN_SIM_OT613_200_IT420.py'

config.Data.outputPrimaryDataset = 'FourMuExtendedPt_1_200_pythia8_14TeV_GEN_SIM_OT613_200_IT420'
config.Data.outputDatasetTag = 'GenSim'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/lpcfpix'
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC'
