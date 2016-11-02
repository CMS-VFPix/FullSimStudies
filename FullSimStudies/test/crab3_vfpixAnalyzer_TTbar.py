from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'vfpixAnalyzer_ttbar_2023D1PU140_810pre12'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'vfpixAnalyzer_simple_cfg.py'

config.Data.inputDataset = '/RelValTTbar_14TeV/CMSSW_8_1_0_pre12-PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/GEN-SIM-RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'vfpixAnalyzerOutput_ttbar_2023D1PU140_810pre12'

config.Site.storageSite = 'T3_US_OSU'
