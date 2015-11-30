#!/usr/bin/env bash

SCENARIO=$1
BATCH=$2

if [ $BATCH -eq 0 ]
then
  echo "launching batch 0..."
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  0   32  ${SCENARIO}  >  ${SCENARIO}_0_00.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  1   32  ${SCENARIO}  >  ${SCENARIO}_0_01.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  2   32  ${SCENARIO}  >  ${SCENARIO}_0_02.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  3   32  ${SCENARIO}  >  ${SCENARIO}_0_03.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  4   32  ${SCENARIO}  >  ${SCENARIO}_0_04.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  5   32  ${SCENARIO}  >  ${SCENARIO}_0_05.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  6   32  ${SCENARIO}  >  ${SCENARIO}_0_06.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  7   32  ${SCENARIO}  >  ${SCENARIO}_0_07.txt  2>&1  &
elif [ $BATCH -eq 1 ]
then
  echo "launching batch 1..."
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  8   32  ${SCENARIO}  >  ${SCENARIO}_1_08.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  9   32  ${SCENARIO}  >  ${SCENARIO}_1_09.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  10  32  ${SCENARIO}  >  ${SCENARIO}_1_10.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  11  32  ${SCENARIO}  >  ${SCENARIO}_1_11.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  12  32  ${SCENARIO}  >  ${SCENARIO}_1_12.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  13  32  ${SCENARIO}  >  ${SCENARIO}_1_13.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  14  32  ${SCENARIO}  >  ${SCENARIO}_1_14.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  15  32  ${SCENARIO}  >  ${SCENARIO}_1_15.txt  2>&1  &
elif [ $BATCH -eq 2 ]
then
  echo "launching batch 2..."
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  16  32  ${SCENARIO}  >  ${SCENARIO}_2_16.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  17  32  ${SCENARIO}  >  ${SCENARIO}_2_17.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  18  32  ${SCENARIO}  >  ${SCENARIO}_2_18.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  19  32  ${SCENARIO}  >  ${SCENARIO}_2_19.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  20  32  ${SCENARIO}  >  ${SCENARIO}_2_20.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  21  32  ${SCENARIO}  >  ${SCENARIO}_2_21.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  22  32  ${SCENARIO}  >  ${SCENARIO}_2_22.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  23  32  ${SCENARIO}  >  ${SCENARIO}_2_23.txt  2>&1  &
elif [ $BATCH -eq 3 ]
then
  echo "launching batch 3..."
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  24  32  ${SCENARIO}  >  ${SCENARIO}_3_24.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  25  32  ${SCENARIO}  >  ${SCENARIO}_3_25.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  26  32  ${SCENARIO}  >  ${SCENARIO}_3_26.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  27  32  ${SCENARIO}  >  ${SCENARIO}_3_27.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  28  32  ${SCENARIO}  >  ${SCENARIO}_3_28.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  29  32  ${SCENARIO}  >  ${SCENARIO}_3_29.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  30  32  ${SCENARIO}  >  ${SCENARIO}_3_30.txt  2>&1  &
  nohup  nice  cmsRun  vfpixAnalyzer_cfg.py  31  32  ${SCENARIO}  >  ${SCENARIO}_3_31.txt  2>&1  &
fi
