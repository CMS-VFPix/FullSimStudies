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

#define REBIN_FACTOR 32

using namespace std;

void invert (TGraphAsymmErrors &);

void
plot (const string &rowsOrCols, const string &pt)
{
  gStyle->SetOptStat (0);

  vector<string> resolutions, parameters;
  if (rowsOrCols == "rows")
    {
      resolutions.push_back ("40x52");
      resolutions.push_back ("53x52");
      resolutions.push_back ("73x52");
      resolutions.push_back ("80x52");
    }
  if (rowsOrCols == "cols")
    {
      resolutions.push_back ("80x26");
      resolutions.push_back ("80x35");
      resolutions.push_back ("80x47");
      resolutions.push_back ("80x52");
    }

  TFile *fin;
  map<string, TGraphAsymmErrors *> hists;
  for (vector<string>::const_iterator res = resolutions.begin (); res != resolutions.end (); res++)
    {
      fin = TFile::Open (("ttbar_" + *res + ".root").c_str ());
      TH1D *den = (TH1D *) fin->Get (("VFPixAnalyzer/tracks/chargedHadronTrackEta" + (pt == "" ? "" : "_" + pt)).c_str ());
      den->SetDirectory (0);
      TH1D *num = (TH1D *) fin->Get (("VFPixAnalyzer/tracks/matchedChargedHadronEta" + (pt == "" ? "" : "_" + pt)).c_str ());
      num->SetDirectory (0);
      fin->Close ();

      den->Rebin (REBIN_FACTOR);
      num->Rebin (REBIN_FACTOR);
      TGraphAsymmErrors *hist = new TGraphAsymmErrors (num, den);
      delete num;
      delete den;

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
      else if (*res == "80x52")
        {
          hist->SetMarkerColor (kBlack);
          hist->SetLineColor (kBlack);
        }

      invert (*hist);

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

  TPaveText *pt3 = new TPaveText(0.637845,0.771144,0.819549,0.839552,"brNDC");
  pt3->SetBorderSize(0);
  pt3->SetFillStyle(0);
  pt3->SetTextFont(42);
  pt3->SetTextSize(0.0373134);
  pt3->SetTextAlign(12);
  if (pt == "0p7")
    pt3->AddText("p_{T} = 0.7 GeV");
  else if (pt == "1p0")
    pt3->AddText("p_{T} = 1 GeV");
  else if (pt == "10p0")
    pt3->AddText("p_{T} = 10 GeV");
  else if (pt == "50p0")
    pt3->AddText("p_{T} = 50 GeV");
  else if (pt == "100p0")
    pt3->AddText("p_{T} = 100 GeV");
  else if (pt == "")
    pt3->AddText("p_{T} > 0.7 GeV");

  TLegend *leg = new TLegend (0.171679,0.643035,0.408521,0.828358,"FPix pixel size","brNDC");
  leg->SetBorderSize(0);
  leg->SetTextSize(0.0373134);
  leg->SetTextAlign(22);
  leg->SetFillStyle(0);
  for (vector<string>::const_iterator res = resolutions.begin (); res != resolutions.end (); res++)
    {
      int x = res->find ('x');
      string rows = res->substr (0, x), cols = res->substr (x + 1, res->length () - x - 1);
      int xSize = 100.0 * (80.0 / atof (rows.c_str ())), ySize = 150.0 * (52.0 / atof (cols.c_str ()));

      stringstream pixelSize;
      pixelSize.str ("");
      pixelSize << xSize << "#times" << ySize << " #mum^{2}";

      leg->AddEntry (hists.at (*res), pixelSize.str ().c_str (), "p");
    }

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
          theClone->GetXaxis ()->SetRangeUser (0.0, 5.0);

          theClone->GetYaxis ()->SetLabelSize (0.04);
          theClone->GetYaxis ()->SetTitleSize (0.04);
          theClone->GetYaxis ()->SetTitleOffset (1.5);
          //theClone->GetYaxis ()->SetRangeUser (0.0, 1.5);

          theClone->GetXaxis ()->SetTitle ("track |#eta|");
          theClone->GetYaxis ()->SetTitle ("tracking fake rate");
          theClone->GetYaxis ()->SetRangeUser (0.0, 1.6);
        }
      firstPlot = false;
    }
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  pt3->Clone ()->Draw ("same");
  leg->Clone ()->Draw ("same");
  c1->Print (("trackingFakeRate_" + rowsOrCols + (pt == "" ? "_allPt" : "_" + pt) + ".pdf").c_str (), "pdf");
}

void
invert (TGraphAsymmErrors &graph)
{
  for (int i = 0; i < graph.GetN (); i++)
    {
      double x, y, eyHigh, eyLow;

      graph.GetPoint (i, x, y);
      eyHigh = graph.GetErrorYhigh (i);
      eyLow = graph.GetErrorYlow (i);

      graph.SetPoint (i, x, 1.0 - y);
      graph.SetPointEYhigh (i, eyLow);
      graph.SetPointEYlow (i, eyHigh);
    }
}
