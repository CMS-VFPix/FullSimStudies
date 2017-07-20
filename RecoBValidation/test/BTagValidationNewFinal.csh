#!/bin/tcsh

#change release version : $1=release to validate, $2=reference release, $3=working directory (where is lacated yours CMSSW instances), $4=release name for DQM inputs to validate, $5=the same for reference DQM inputs
set valrel=$1
set refrel=$2
set workdir=$3
set valdir=$4
set refdir=$5

mkdir ${valrel}_vs_${refrel}

cd ${valrel}_vs_${refrel}
plotFactory.py -b -f ${workdir}/CMSSW_${valdir}/src/VFPix/RecoBValidation/test/${valrel}.root -F ${workdir}/CMSSW_${refdir}/src/VFPix/RecoBValidation/test/${refrel}.root -r ${valrel} -R ${refrel} -s TTbar_Startup -S TTbar_Startup
cp ../0_leg*.gif .
mv 0_leg1.gif 0_leg4.gif
cat ../index.html | sed -e s/REFREL/${refrel}/g | sed -e s/VALREL/${valrel}/g | sed -e s/VALDIR/${valdir}/g  > index.html
cd ..


mkdir CMSSW_${valdir}
mv ${valrel}_vs_${refrel}                 CMSSW_${valdir}/


