from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'vbf_fpix80x52_digi'
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DigiFullPU_Extended2023HGCalMuonPandoraPU_80x52.py'      # for the DIGI step
#config.JobType.psetName = 'RecoFullPUHGCAL_Extended2023HGCalMuonPandoraPU_80x52.py' # for the RECO step

config.Data.inputDataset = '/VBF_HToZZTo4L_M_125_TuneZ2star_14TeV_pythia6_tauola_FPix80x52/ahart-CMSSW_6_2_0_SLHC26_patch4-PH2_1K_FB_V6_HLLHCBS_140-v1-90f126b761c3bb3d2eb04620ea384282/USER' # CHANGE ME
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CMSSW_6_2_0_SLHC26_patch4-PH2_1K_FB_V6_HLLHCBS_140-v2' # for the DIGI step
#config.Data.outputDatasetTag = 'PH2_1K_FB_V6_HLLHCBS_140-v2' # for the RECO step

config.Site.storageSite = 'T2_US_Purdue'
