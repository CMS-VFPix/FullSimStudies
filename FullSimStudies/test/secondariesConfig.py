import os
from OSUT3Analysis.Configuration.configurationOptions import *

dataset_names = {'ttbar_pre12_PU140' : '/RelValTTbar_14TeV/CMSSW_8_1_0_pre12-PU25ns_81X_mcRun2_asymptotic_v8_2023D1PU140-v1/GEN-SIM-RECO'}
nJobs = {'ttbar_pre12_PU140' : 200}
maxEvents ={'ttbar_pre12_PU140' : -1}
types ={'ttbar_pre12_PU140' : 'bgMC'}
#colors
#labels
#intLumi = 2460

config_file = "secondariesAnalyzer_cfg.py"

datasets = ['ttbar_pre12_PU140']
    
InputCondorArguments = {}
