import os
from OSUT3Analysis.Configuration.configurationOptions import *

dataset_names = {
    'VBF_HTo4L_FPix8x52' : '/VBF_HToZZTo4L_M_125_TuneZ2star_14TeV_pythia6_tauola_FPix8x52/ahart-PH2_1K_FB_V6_HLLHCBS_140-v1-8f9dc95ed3461ce4e9247d30e1d0250b/USER',
    'VBF_HTo4L_FPix80x520' : '/VBF_HToZZTo4L_M_125_TuneZ2star_14TeV_pythia6_tauola_FPix80x520/ahart-PH2_1K_FB_V6_HLLHCBS_140-v1-644308ecf888c995941d453f7af78e5f/USER',
    'VBF_HTo4L_FPix80x52' : '/VBF_HToZZTo4L_M_125_TuneZ2star_14TeV_pythia6_tauola_FPix80x52/ahart-PH2_1K_FB_V6_HLLHCBS_140-v1-2d66254c9c3cc8fb02a57973d566a6d4/USER',
    'VBF_HTo4L_FPix80x5' : '/VBF_HToZZTo4L_M_125_TuneZ2star_14TeV_pythia6_tauola_FPix80x5/ahart-PH2_1K_FB_V6_HLLHCBS_140-v1-10c3c4ba012eb8b2703fa62befddace1/USER',
    'VBF_HTo4L_FPix800x52' : '/VBF_HToZZTo4L_M_125_TuneZ2star_14TeV_pythia6_tauola_FPix800x52/ahart-PH2_1K_FB_V6_HLLHCBS_140-v1-5afad7224299a99d579dcb9c8271dba9/USER',
}

intLumi = 2460

config_file = "vfpixAnalyzer_forCondor_cfg.py"

datasets = [
    'VBF_HTo4L_FPix8x52',
    'VBF_HTo4L_FPix80x520',
    'VBF_HTo4L_FPix80x52',
    'VBF_HTo4L_FPix80x5',
    'VBF_HTo4L_FPix800x52',
]
    
InputCondorArguments = {
}
