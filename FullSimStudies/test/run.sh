#!/usr/bin/env bash

SCENARIO=$1
BATCH=$2

if [ $BATCH -eq 0 ]
then
  echo "launching batch 0..."
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  0   32  $1  >  output00.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  1   32  $1  >  output01.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  2   32  $1  >  output02.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  3   32  $1  >  output03.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  4   32  $1  >  output04.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  5   32  $1  >  output05.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  6   32  $1  >  output06.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  7   32  $1  >  output07.txt  2>&1  &
elif [ $BATCH -eq 1 ]
then
  echo "launching batch 1..."
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  8   32  $1  >  output08.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  9   32  $1  >  output09.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  10  32  $1  >  output10.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  11  32  $1  >  output11.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  12  32  $1  >  output12.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  13  32  $1  >  output13.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  14  32  $1  >  output14.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  15  32  $1  >  output15.txt  2>&1  &
elif [ $BATCH -eq 2 ]
then
  echo "launching batch 2..."
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  16  32  $1  >  output16.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  17  32  $1  >  output17.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  18  32  $1  >  output18.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  19  32  $1  >  output19.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  20  32  $1  >  output20.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  21  32  $1  >  output21.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  22  32  $1  >  output22.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  23  32  $1  >  output23.txt  2>&1  &
elif [ $BATCH -eq 3 ]
then
  echo "launching batch 3..."
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  24  32  $1  >  output24.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  25  32  $1  >  output25.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  26  32  $1  >  output26.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  27  32  $1  >  output27.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  28  32  $1  >  output28.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  29  32  $1  >  output29.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  30  32  $1  >  output30.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  31  32  $1  >  output31.txt  2>&1  &
fi
