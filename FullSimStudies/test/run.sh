#!/usr/bin/env bash

SCENARIO=$1
nohup nice cmsRun vfpixAnalyzer_cfg.py 0 8 $1 > output0.txt 2>&1 &
nohup nice cmsRun vfpixAnalyzer_cfg.py 1 8 $1 > output1.txt 2>&1 &
nohup nice cmsRun vfpixAnalyzer_cfg.py 2 8 $1 > output2.txt 2>&1 &
nohup nice cmsRun vfpixAnalyzer_cfg.py 3 8 $1 > output3.txt 2>&1 &
nohup nice cmsRun vfpixAnalyzer_cfg.py 4 8 $1 > output4.txt 2>&1 &
nohup nice cmsRun vfpixAnalyzer_cfg.py 5 8 $1 > output5.txt 2>&1 &
nohup nice cmsRun vfpixAnalyzer_cfg.py 6 8 $1 > output6.txt 2>&1 &
nohup nice cmsRun vfpixAnalyzer_cfg.py 7 8 $1 > output7.txt 2>&1 &
