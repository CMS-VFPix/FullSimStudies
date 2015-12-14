#!/usr/bin/env python                                                                                                                                                                 
import time
import sys
import copy
from array import *
from optparse import OptionParser
import os


#epitext = "This tool parses histograms from an input file and arranges them on a canvas,
#using some assumptions about stuff and things"

#parser = OptionParser(epilog = epitext)
parser = OptionParser()

parser.add_option("-l", "--localConfig", dest="localConfig", help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir", help="output directory")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.rstrip('.py') + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.outputDir:
    if not os.path.exists(arguments.outputDir):
        os.system("mkdir "+arguments.outputDir)
else:
    print "No output directory specified, shame on you"
    sys.exit(0)

########################################################################################

# root includes must come after the option parser configuration
from ROOT import gROOT,gStyle,gDirectory,gPad,TFile,TGraphErrors,TColor,TCanvas,TLegend,TPaveText,TLine

# setting ROOT options so our plots will look awesome and everyone will love us
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetCanvasDefH(300)
gStyle.SetCanvasDefW(400)
gStyle.SetCanvasDefX(0)
gStyle.SetCanvasDefY(0)
gStyle.SetGridStyle(3)
gStyle.SetNdivisions(510)
gROOT.ForceStyle()

########################################################################################

REBIN_FACTOR = 32

# defining color palette 
black_ = 1
red_ = 633
orange_ = 801
green_ = 417
cyan_ = 433
blue_ = 601
violet_ = 881

config_dictionary = {
    'pt' : {
        'title' : 'Transverse momentum error',
        'y_axis_title' : '#sigma(#deltap_{T}/p_{T}) [%]',
        'y_axis_min' : 0.08,
        'y_axis_max' : 1000,
    },
    'd0' : {
        'title' : 'Transverse impact parameter error',
        'y_axis_title' : '#sigma(#deltad_{0}) [cm]',
        'y_axis_min' : 0.0008,
        'y_axis_max' : 0.1,
    },
    'dz' : {
        'title' : 'Longitudinal impact parameter error',
        'y_axis_title' : '#sigma(#deltad_{z}) [cm]',
        'y_axis_min' : 0.0008,
        'y_axis_max' : 1,
    },
    'eff' : {
        'title' : 'Track reconstruction efficiency',
        'y_axis_title' : 'track reco. eff. [%]',
        'y_axis_min' : 0.000-8,
        'y_axis_max' : 1000,
    },

}

scalings_ = [1.0, 1.1, 1.5, 2.0, 4.0, 8.0, 10.0, 1.0/1.1, 1.0/1.5, 1.0/2.0, 1.0/4.0, 1.0/8.0, 1.0/10.0]

color_scheme = {
    '1.0' : black_,
    '1.1' : red_,
    '1.5' : orange_,
    '2.0' : green_,
    '4.0' : cyan_,
    '8.0' : blue_,
    '10.0': violet_
}

########################################################################################

def getHistogram(pt, variable, pitch):
    
    inputFile = TFile(inputFileFormat.replace('pitch',pitch))
    histogram = inputFile.Get("VFPixAnalyzer/tracks/" + variable + "ErrorVsTrackEta_" + pt)
    histogram.RebinX(REBIN_FACTOR)
    profile = histogram.ProfileX()
    projection = profile.ProjectionX()
    projection.SetDirectory(0)
    inputFile.Close()

    formatHistogram(projection, pitch)

    return projection

########################################################################################

def getScalings(pitch):
    baselineX = float(baseline.split('x')[0])
    baselineY = float(baseline.split('x')[1])
    x = float(pitch.split('x')[0])
    y = float(pitch.split('x')[1])
    xScale = -1.0
    minDiffX = 999.
    yScale = -1.0
    minDiffY = 999.
    # find closest scaling in each direction
    for scale in scalings_:
        xDiff = abs(x/baselineX - scale)
        if xDiff < minDiffX:
            xScale = scale
            minDiffX = xDiff
        xDiff = abs(x/baselineX - scale)
        if abs(y/baselineY - scale) < minDiffY:
            yScale = scale
            minDiffY = abs(y/baselineY - scale)

    return [xScale, yScale]


########################################################################################

# format histogram conditionally based on pitch change with respect to baseline
def formatHistogram(histogram, pitch):

    scalings = getScalings(pitch)
    xScale = scalings[0]
    yScale = scalings[1]
    if xScale != 1.0 and yScale != 1.0:
        print "scaling in both dimensions not yet supported"
        return
    if xScale != 1.0:
        scale = xScale
    else:
        scale = yScale
    # scaling to higher number of pixels, use filled circle marker
    if scale > 1.0:
        histogram.SetMarkerStyle(20)
    # scaling to lower number of pixels, use empty square marker
    elif scale < 1.0:
        histogram.SetMarkerStyle(25)
    # baseline, use filled triangle marker
    else:
        histogram.SetMarkerStyle(22)
    # set color based on amount of change wrt baseline
    for color_code in color_scheme:
        if abs(float(color_code) - scale) < 0.001 or abs(1.0/float(color_code) - scale) < 0.001:
            histogram.SetMarkerColor(color_scheme[color_code])
            histogram.SetLineColor(color_scheme[color_code])

    histogram.SetTitle(config_dictionary[variable]['title'])
    histogram.GetXaxis().SetTitle("")
    histogram.GetXaxis().SetRangeUser(0.0,4.0)
    histogram.GetYaxis().SetTitle(config_dictionary[variable]['y_axis_title'])
    histogram.GetYaxis().SetRangeUser(config_dictionary[variable]['y_axis_min'], config_dictionary[variable]['y_axis_max'])
    histogram.GetYaxis().SetTitleOffset(1.5)

    return

########################################################################################
########################################################################################
########################################################################################
########################################################################################

outputFile = TFile(arguments.outputDir + "/output.root","RECREATE")

for pt in pts_to_test:
    for variable in variables_to_test:
        for plot in plots:

            plot_name = plot['name']+"_"+variable+"_"+pt
            canvas = TCanvas(plot_name,"",0,0,700,800)

            canvas.Divide(1,2)

            canvas.cd(1)
            gPad.SetLogy()
            gPad.SetPad(0,0.25,1,1)
            gPad.SetMargin(0.15,0.05,0.0,0.07)
            gPad.SetFillStyle(0)
            gPad.SetTickx(1)
            gPad.SetTicky(1)
            gPad.Update()
            gPad.Draw()

            canvas.cd(2)
            gPad.SetPad(0,0,1,0.25)
            gPad.SetMargin(0.15,0.05,0.4,0.0)
            gPad.SetFillStyle(0)
            gPad.SetTickx(1)
            gPad.SetTicky(1)
            gPad.Update()
            gPad.Draw()
        
            canvas.cd(1)

            legend = TLegend(0.1783167,0.6399027,0.5249643,0.8459043)
            legend.SetBorderSize(0)
            legend.SetFillColor(0)
            legend.SetFillStyle(0)
            legend.SetTextAlign(12)

            # first get baseline histogram
            baselineHistogram = getHistogram(pt, variable, baseline)
            legend.AddEntry(baselineHistogram,"100 #times 150 #mum^{2} (#phi,#rho)","LEFP")

            # then get altered pitch histograms
            histograms = []
            ratios = []
            for pitch in plot['pitches']:
                currentHistogram = getHistogram(pt, variable, pitch)
                scalings = getScalings(pitch)
                sizeLabel = str(int(100.0/scalings[0]))+" #times "+str(int(150.0/scalings[1]))+" #mum^{2} (#phi,#rho)"
                currentHistogram.SetName(sizeLabel)
                histograms.append(currentHistogram)
                ratioHistogram = currentHistogram.Clone()
                ratioHistogram.Divide(baselineHistogram)
                ratios.append(ratioHistogram)

            for histogram in histograms:
                legend.AddEntry(histogram,histogram.GetName(),"LEFP")
                histogram.Draw("E0 same")

            baselineHistogram.Draw("E0 same")

            pt1 = TPaveText(0.1174497,0.8621291,0.5469799,0.9075044,"brNDC")
            pt1.SetBorderSize(0)
            pt1.SetFillStyle(0)
            pt1.SetTextFont(62)
            pt1.SetTextSize(0.0374065)
            pt1.SetTextAlign(32)
            pt1.AddText("CMS Phase II Simulation")
            pt1.Draw("same")

            pt2 = TPaveText(0.639087,0.8572587,0.9286733,0.9042985,"brNDC")
            pt2.SetBorderSize(0)
            pt2.SetFillStyle(0)
            pt2.SetTextFont(42)
            pt2.SetTextSize(0.0374065)
            pt2.SetTextAlign(32)
            pt2.AddText("14 TeV, PU = 140")
            pt2.Draw("same")

            pt3 = TPaveText(0.5035663,0.7875101,0.9400856,0.8572587,"brNDC")
            pt3.SetBorderSize(0)
            pt3.SetFillStyle(0)
            pt3.SetTextFont(42)
            pt3.SetTextSize(0.03664922)
            pt3.SetTextAlign(32)
            pt3.AddText("p_{T} = " + pt.replace('p','.') + " GeV (#pm10%)")
            pt3.Draw("same")

            legend.Draw("same")

            canvas.cd(2)
            for ratio in ratios:
                ratio.SetTitle("")
                ratio.SetTickLength(0.08)
                ratio.GetYaxis().SetTitle("ratio")
                ratio.GetXaxis().SetTitle("track |#eta|")
                ratio.GetYaxis().CenterTitle()
                ratio.GetYaxis().SetTitleSize(0.11)
                ratio.GetYaxis().SetTitleOffset(0.43)
                ratio.GetXaxis().SetTitleSize(0.11)
                ratio.GetYaxis().SetLabelSize(0.11)
                ratio.GetXaxis().SetLabelSize(0.11)
                ratio.GetYaxis().SetRangeUser(0.01,3.2)
                ratio.GetYaxis().SetNdivisions(304)
                ratio.Draw("E0 same")
            l1 = TLine(0,1,4,1)
            l1.SetLineStyle(3)
            l1.SetLineWidth(1)
            l1.Draw("same")


            outputFile.cd()
            canvas.Write()
            canvas.SaveAs(arguments.outputDir + "/" + plot_name + ".pdf")

#outputFile.Close()



########################################################################################
########################################################################################
########################################################################################
########################################################################################
