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
#define SCALE_FACTOR 100000

using namespace std;

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
    }
  if (rowsOrCols == "cols")
    {
      resolutions.push_back ("80x26");
      resolutions.push_back ("80x35");
      resolutions.push_back ("80x47");
    }
  parameters.push_back ("pt");
  parameters.push_back ("d0");
  parameters.push_back ("dz");

  string baselineResolution = "80x52";

  TFile *fin;
  map<string, map<string, TGraphAsymmErrors *> > hists;
  for (vector<string>::const_iterator par = parameters.begin (); par != parameters.end (); par++)
    {
      fin = TFile::Open (("ttbar_" + baselineResolution + ".root").c_str ());
      TH2D *hist2DBaseline = (TH2D *) fin->Get (("VFPixAnalyzer/tracks/" + *par + "ErrorVsTrackEta_" + pt).c_str ());
      hist2DBaseline->SetDirectory (0);
      fin->Close ();
      
      TH1D *histBaseline = (TH1D *) hist2DBaseline->ProfileX ();
      histBaseline->SetDirectory (0);
      delete hist2DBaseline;
      
      histBaseline->Rebin (REBIN_FACTOR);
      histBaseline->Scale (SCALE_FACTOR);

      for (vector<string>::const_iterator res = resolutions.begin (); res != resolutions.end (); res++)
        {
          fin = TFile::Open (("ttbar_" + *res + ".root").c_str ());
          TH2D *hist2D = (TH2D *) fin->Get (("VFPixAnalyzer/tracks/" + *par + "ErrorVsTrackEta_" + pt).c_str ());
          hist2D->SetDirectory (0);
          fin->Close ();

          TH1D *hist1D = (TH1D *) hist2D->ProfileX ();
          hist1D->SetDirectory (0);
          delete hist2D;
          hist1D->Rebin (REBIN_FACTOR);
          hist1D->Scale (SCALE_FACTOR);
	  TGraphAsymmErrors *hist = new TGraphAsymmErrors (hist1D, histBaseline, "pois");
	  //	  TGraphAsymmErrors *hist = new TGraphAsymmErrors (hist1D);
	  //TGraphAsymmErrors *hist = new TGraphAsymmErrors (histBaseline);
	  delete hist1D;

          hist->SetMarkerStyle (20);
          hist->SetLineStyle (1);
          hist->SetMarkerSize (1.5);
          hist->SetLineWidth (1);

          hist->GetXaxis ()->SetLabelSize (0.04);
          hist->GetXaxis ()->SetTitleSize (0.04);
          hist->GetXaxis ()->SetRangeUser (0.0, 4.0);

          hist->GetYaxis ()->SetLabelSize (0.04);
          hist->GetYaxis ()->SetTitleSize (0.04);
          hist->GetYaxis ()->SetTitleOffset (1.5);
          //hist->GetYaxis ()->SetRangeUser (0.0, 1.5);

          hist->GetXaxis ()->SetTitle ("track |#eta|");

          if (*par == "pt")
            {
              hist->GetYaxis ()->SetRangeUser (0.1, 5.0);
              hist->GetYaxis ()->SetTitle ("change in #sigma(#deltap_{T}/p_{T}) wrt to 80x52");
            }
          if (*par == "d0")
            {
              hist->GetYaxis ()->SetRangeUser (0.1, 5.0);
              hist->GetYaxis ()->SetTitle ("change in #sigma(#deltad_{0}) wrt to 80x52");
            }
          if (*par == "dz")
            {
              hist->GetYaxis ()->SetRangeUser (0.1, 5.0);
              hist->GetYaxis ()->SetTitle ("change in #sigma(#deltaz_{0}) wrt to 80x52");
            }

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

          hists[*par][*res] = hist;
        }
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

  TPaveText *pt3 = new TPaveText(0.64787,0.763682,0.829574,0.833333,"brNDC");
  pt3->SetBorderSize(0);
  pt3->SetFillStyle(0);
  pt3->SetTextFont(42);
  pt3->SetTextSize(0.0349127);
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

  TLegend *leg = new TLegend (0.161654,0.681592,0.348371,0.81592,NULL,"brNDC");
  leg->SetBorderSize(0);
  leg->SetTextSize(0.0349127);
  leg->SetFillStyle(0);
  for (vector<string>::const_iterator res = resolutions.begin (); res != resolutions.end (); res++)
    leg->AddEntry (hists.at ("pt").at (*res), ("FPix " + *res).c_str (), "p");

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

  TCanvas *c2 = new TCanvas("c2", "c2",522,103,800,830);
  gStyle->SetOptStat(0);
  c2->Range(-0.86955,-0.1495536,5.91635,1.640625);
  c2->SetFillColor(0);
  c2->SetBorderMode(0);
  c2->SetBorderSize(2);
  c2->SetTickx(1);
  c2->SetTicky(1);
  c2->SetLogx(0);
  c2->SetLogy(0);
  c2->SetLeftMargin(0.1281407);
  c2->SetRightMargin(0.0678392);
  c2->SetTopMargin(0.07855362);
  c2->SetBottomMargin(0.08354115);
  c2->SetFrameFillStyle(0);
  c2->SetFrameBorderMode(0);
  c2->SetFrameFillStyle(0);
  c2->SetFrameBorderMode(0);

  TCanvas *c3 = new TCanvas("c3", "c3",522,103,800,830);
  gStyle->SetOptStat(0);
  c3->Range(-0.86955,-0.1495536,5.91635,1.640625);
  c3->SetFillColor(0);
  c3->SetBorderMode(0);
  c3->SetBorderSize(2);
  c3->SetTickx(1);
  c3->SetTicky(1);
  c3->SetLogx(0);
  c3->SetLogy(0);
  c3->SetLeftMargin(0.1281407);
  c3->SetRightMargin(0.0678392);
  c3->SetTopMargin(0.07855362);
  c3->SetBottomMargin(0.08354115);
  c3->SetFrameFillStyle(0);
  c3->SetFrameBorderMode(0);
  c3->SetFrameFillStyle(0);
  c3->SetFrameBorderMode(0);

  c1->cd ();
  bool firstPlot = true;
  for (map<string, TGraphAsymmErrors *>::const_iterator hist = hists.at ("pt").begin (); hist != hists.at ("pt").end (); hist++)
    {
      hist->second->Clone ()->Draw (firstPlot ? "ap" : "p same");
      firstPlot = false;
    }
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  pt3->Clone ()->Draw ("same");
  leg->Clone ()->Draw ("same");
  c1->Update();
  TLine *l1 = new TLine(0,1,4,1);
  l1->SetLineStyle(3);
  l1->Draw("same");
  c1->Print (("pt_" + rowsOrCols + "_" + pt + ".pdf").c_str (), "pdf");

  c2->cd ();
  firstPlot = true;
  for (map<string, TGraphAsymmErrors *>::const_iterator hist = hists.at ("d0").begin (); hist != hists.at ("d0").end (); hist++)
    {
      hist->second->Clone ()->Draw (firstPlot ? "ap" : "p same");
      firstPlot = false;
    }
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  pt3->Clone ()->Draw ("same");
  leg->Clone ()->Draw ("same");
  c2->Update();
  TLine *l2 = new TLine(0,1,4,1);
  l2->SetLineStyle(3);
  l2->Draw("same");
  c2->Print (("d0_" + rowsOrCols + "_" + pt + ".pdf").c_str (), "pdf");

  c3->cd ();
  firstPlot = true;
  for (map<string, TGraphAsymmErrors *>::const_iterator hist = hists.at ("dz").begin (); hist != hists.at ("dz").end (); hist++)
    {
      hist->second->Clone ()->Draw (firstPlot ? "ap" : "p same");
      firstPlot = false;
    }
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  pt3->Clone ()->Draw ("same");
  leg->Clone ()->Draw ("same");
  c3->Update();
  TLine *l3 = new TLine(0,1,4,1);
  l3->SetLineStyle(3);
  l3->Draw("same");
  c3->Print (("z0_" + rowsOrCols + "_" + pt + ".pdf").c_str (), "pdf");
}
