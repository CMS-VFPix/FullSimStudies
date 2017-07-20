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
cd ..


mkdir CMSSW_${valdir}
mv ${valrel}_vs_${refrel}                 CMSSW_${valdir}/

echo '<a href="https://cernbox.cern.ch/index.php/s/68hk5uG5sy9Hqvn/index_'${valrel}_vs_${refrel}'.html">'${valrel}_vs_${refrel}'</a><br>' >> index.html

scp 'index.html' $USER'@lxplus6.cern.ch:/eos/user/j/jalimena/www/plots/Phase2BTagValidation/index_'${valrel}_vs_${refrel}'.html'
scp -r CMSSW_${valdir} $USER'@lxplus6.cern.ch:/eos/user/j/jalimena/www/plots/Phase2BTagValidation/'

#echo 'https://cernbox.cern.ch/index.php/s/68hk5uG5sy9Hqvn/index_'${valrel}_vs_${refrel}'.html' >& webpage.txt
