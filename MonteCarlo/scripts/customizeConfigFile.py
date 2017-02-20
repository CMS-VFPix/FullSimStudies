#!/usr/bin/env python

import argparse
import sys
import shutil
import glob
import os

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input",
                  help="path to the input config file")
parser.add_argument("-d", "--dir",
                  help="name of directory holding customized xml files")
args = parser.parse_args()

if not args.dir or not args.input:
    print "please provide -i and -d arguments"
    sys.exit()

appendix = args.dir.rstrip("/")

outputFile =  args.input.split(".")[0]+"_"+appendix+".py"
# create new config file
shutil.copyfile(args.input, args.input.split(".")[0]+"_"+appendix+".py")


# add lines at the end of file to redirect CMSSW to the custom xml files in the "dir" directory
baseDir = os.environ['CMSSW_BASE']
xmlList = [os.path.basename(path) for path in glob.glob(baseDir + "/src/VFPix/MonteCarlo/data/"+appendix+"/*xml")]

fileNames = [xml.split("/")[-1] for xml in xmlList]
fileList = '['
for file in fileNames:
    fileList = fileList + '"' + file + '",'
fileList = fileList.rstrip(',') + ']'

with open(outputFile, 'a') as f:
    f.write('inputDir = "VFPix/MonteCarlo/data/' + appendix + '/"\n')
    f.write('fileNames =' +  fileList + '\n')
    f.write('for i in range (0, len (process.XMLIdealGeometryESSource.geomXMLFiles)):\n')
    f.write('\txmlFile = process.XMLIdealGeometryESSource.geomXMLFiles[i]\n')
    f.write('\tfileName = xmlFile.split("/")[-1]\n')
    f.write('\tif fileName in fileNames:\n')
    f.write('\t\tprocess.XMLIdealGeometryESSource.geomXMLFiles[i] = inputDir + fileName\n')
