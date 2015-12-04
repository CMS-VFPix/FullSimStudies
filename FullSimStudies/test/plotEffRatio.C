#include <iostream>
#include <sstream>
#include <vector>

#include "TFile.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TStyle.h"
#include "TGraphAsymmErrors.h"
#include "TF1.h"
#include "TMath.h"

#define REBIN_FACTOR 50

using namespace std;

void
plot (const string &rowsOrCols)
{
  gStyle->SetOptStat (0);


  vector<string> resolutions, parameters;
  if (rowsOrCols == "rows")
    {
      resolutions.push_back ("40x52");
      resolutions.push_back ("53x52");
      resolutions.push_back ("73x52");
    }
  if (rowsOrCols == "cols")
    {
      resolutions.push_back ("80x26");
      resolutions.push_back ("80x35");
      resolutions.push_back ("80x47");
    }

  string baselineResolution = "80x52";

  TFile *fin;
  fin = TFile::Open (("ttbar_" + baselineResolution + ".root").c_str ());
  TH1D *baselineDen = (TH1D *) fin->Get ("VFPixAnalyzer/tracks/chargedHadronEta");
  baselineDen->SetDirectory (0);
  TH1D *baselineEff = (TH1D *) fin->Get ("VFPixAnalyzer/tracks/chargedHadronTrackEta");
  baselineEff->SetDirectory (0);
  fin->Close ();
  baselineDen->Rebin (REBIN_FACTOR);
  baselineEff->Rebin (REBIN_FACTOR);
  baselineEff->Divide(baselineDen);

  map<string, TGraphAsymmErrors *> hists;
  for (vector<string>::const_iterator res = resolutions.begin (); res != resolutions.end (); res++)
    {
      fin = TFile::Open (("ttbar_" + *res + ".root").c_str ());
      TH1D *den = (TH1D *) fin->Get ("VFPixAnalyzer/tracks/chargedHadronEta");
      den->SetDirectory (0);
      TH1D *num = (TH1D *) fin->Get ("VFPixAnalyzer/tracks/chargedHadronTrackEta");
      num->SetDirectory (0);
      fin->Close ();

      den->Rebin (REBIN_FACTOR);
      num->Rebin (REBIN_FACTOR);
      num->Divide(den);
      delete den;
      TGraphAsymmErrors *hist = new TGraphAsymmErrors (num, baselineEff, "pois");
      delete num;

      hist->SetMarkerStyle (20);
      hist->SetLineStyle (1);
      hist->SetMarkerSize (1.5);
      hist->SetLineWidth (1);

      if (*res == "40x52" || *res == "80x26")
        {
          hist->SetMarkerColor (kRed);
          hist->SetLineColor (kRed);
        }
      else if (*res == "53x52" || *res == "80x35")
        {
          hist->SetMarkerColor (kGreen);
          hist->SetLineColor (kGreen);
        }
      else if (*res == "73x52" || *res == "80x47")
        {
          hist->SetMarkerColor (kBlue);
          hist->SetLineColor (kBlue);
        }
      hists[*res] = hist;
    }

  TPaveText *pt1 = new TPaveText(0.214824,0.840399,0.565327,0.886534,"brNDC");
  pt1->SetBorderSize(0);
  pt1->SetFillStyle(0);
  pt1->SetTextFont(62);
  pt1->SetTextSize(0.0374065);
  pt1->AddText("CMS Phase II Simulation");

  TPaveText *pt2 = new TPaveText(0.729899,0.92394,0.845477,0.971322,"brNDC");
  pt2->SetBorderSize(0);
  pt2->SetFillStyle(0);
  pt2->SetTextFont(42);
  pt2->SetTextSize(0.0374065);
  pt2->AddText("14 TeV, PU = 140");

  TLegend *leg = new TLegend (0.161654,0.681592,0.348371,0.81592,NULL,"brNDC");
  leg->SetBorderSize(0);
  leg->SetTextSize(0.0349127);
  leg->SetFillStyle(0);
  for (vector<string>::const_iterator res = resolutions.begin (); res != resolutions.end (); res++)
    leg->AddEntry (hists.at (*res), ("FPix " + *res).c_str (), "p");

  TCanvas *c1 = new TCanvas("c1", "c1",522,103,800,830);
  gStyle->SetOptStat(0);
  c1->Range(-0.86955,-0.1495536,5.91635,1.640625);
  c1->SetFillColor(0);
  c1->SetBorderMode(0);
  c1->SetBorderSize(2);
  c1->SetTickx(1);
  c1->SetTicky(1);
  c1->SetLogx(0);
  c1->SetLogy(0);
  c1->SetLeftMargin(0.1281407);
  c1->SetRightMargin(0.0678392);
  c1->SetTopMargin(0.07855362);
  c1->SetBottomMargin(0.08354115);
  c1->SetFrameFillStyle(0);
  c1->SetFrameBorderMode(0);
  c1->SetFrameFillStyle(0);
  c1->SetFrameBorderMode(0);

  c1->cd ();

  bool firstPlot = true;
  for (map<string, TGraphAsymmErrors *>::const_iterator hist = hists.begin (); hist != hists.end (); hist++)
    {
      TGraphAsymmErrors *theClone = NULL;
      (theClone = (TGraphAsymmErrors *) hist->second->Clone ())->Draw (firstPlot ? "ap" : "p same");
      if (firstPlot)
        {
          theClone->GetXaxis ()->SetLabelSize (0.04);
          theClone->GetXaxis ()->SetTitleSize (0.04);
          theClone->GetXaxis ()->SetRangeUser (0.0, 4.0);

          theClone->GetYaxis ()->SetLabelSize (0.04);
          theClone->GetYaxis ()->SetTitleSize (0.04);
          theClone->GetYaxis ()->SetTitleOffset (1.5);
          //theClone->GetYaxis ()->SetRangeUser (0.0, 1.5);

          theClone->GetXaxis ()->SetTitle ("track |#eta|");
          theClone->GetYaxis ()->SetTitle ("tracking efficiency change wrt 80x52");
          theClone->GetYaxis ()->SetRangeUser (0.9, 1.1);
        }
      firstPlot = false;
    }
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  leg->Clone ()->Draw ("same");
  c1->Update();
  TLine *unityLine = new TLine(0,1,4,1);
  unityLine->SetLineStyle(3);
  unityLine->Draw("same");

  c1->Print("plot.pdf");
}
