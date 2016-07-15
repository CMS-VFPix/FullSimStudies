#include <iostream>
#include <sstream>

#include "TFile.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TPaveText.h"

using namespace std;

void
plot (const string &file, const string &dir, const string &hist, const double low, const double high)
{
  gStyle->SetOptStat(0);
  TFile *fin = TFile::Open (file.c_str ());
  TH2D *errorVsTrackEta_0p7,
    *errorVsTrackEta_1p0,
    *errorVsTrackEta_10p0,
    *errorVsTrackEta_50p0,
    *errorVsTrackEta_100p0;
  errorVsTrackEta_0p7 = (TH2D *) fin->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_0p7").c_str ());
  errorVsTrackEta_1p0 = (TH2D *) fin->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_1p0").c_str ());
  errorVsTrackEta_10p0 = (TH2D *) fin->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_10p0").c_str ());
  errorVsTrackEta_50p0 = (TH2D *) fin->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_50p0").c_str ());
  errorVsTrackEta_100p0 = (TH2D *) fin->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_100p0").c_str ());

  errorVsTrackEta_0p7->SetDirectory (0);
  errorVsTrackEta_1p0->SetDirectory (0);
  errorVsTrackEta_10p0->SetDirectory (0);
  errorVsTrackEta_50p0->SetDirectory (0);
  errorVsTrackEta_100p0->SetDirectory (0);
  fin->Close ();

  errorVsTrackEta_0p7->Rebin2D ();
  errorVsTrackEta_1p0->Rebin2D ();
  errorVsTrackEta_10p0->Rebin2D ();
  errorVsTrackEta_50p0->Rebin2D ();
  errorVsTrackEta_100p0->Rebin2D ();

  errorVsTrackEta_0p7->Rebin2D ();
  errorVsTrackEta_1p0->Rebin2D ();
  errorVsTrackEta_10p0->Rebin2D ();
  errorVsTrackEta_50p0->Rebin2D ();
  errorVsTrackEta_100p0->Rebin2D ();

  errorVsTrackEta_0p7->Rebin2D ();
  errorVsTrackEta_1p0->Rebin2D ();
  errorVsTrackEta_10p0->Rebin2D ();
  errorVsTrackEta_50p0->Rebin2D ();
  errorVsTrackEta_100p0->Rebin2D ();

  errorVsTrackEta_0p7->Rebin2D ();
  errorVsTrackEta_1p0->Rebin2D ();
  errorVsTrackEta_10p0->Rebin2D ();
  errorVsTrackEta_50p0->Rebin2D ();
  errorVsTrackEta_100p0->Rebin2D ();

  errorVsTrackEta_0p7->Rebin2D ();
  errorVsTrackEta_1p0->Rebin2D ();
  errorVsTrackEta_10p0->Rebin2D ();
  errorVsTrackEta_50p0->Rebin2D ();
  errorVsTrackEta_100p0->Rebin2D ();

  TH1D *prof_0p7,
    *prof_1p0,
    *prof_10p0,
    *prof_50p0,
    *prof_100p0;
  prof_0p7 = (TH1D *) errorVsTrackEta_0p7->ProfileX ();
  prof_1p0 = (TH1D *) errorVsTrackEta_1p0->ProfileX ();
  prof_10p0 = (TH1D *) errorVsTrackEta_10p0->ProfileX ();
  prof_50p0 = (TH1D *) errorVsTrackEta_50p0->ProfileX ();
  prof_100p0 = (TH1D *) errorVsTrackEta_100p0->ProfileX ();

  prof_0p7->GetXaxis ()->SetLimits (0.0, 5.0);
  prof_1p0->GetXaxis ()->SetLimits (0.0, 5.0);
  prof_10p0->GetXaxis ()->SetLimits (0.0, 5.0);
  prof_50p0->GetXaxis ()->SetLimits (0.0, 5.0);
  prof_100p0->GetXaxis ()->SetLimits (0.0, 5.0);

  prof_0p7->GetXaxis ()->SetRangeUser (0.0, 5.0);
  prof_1p0->GetXaxis ()->SetRangeUser (0.0, 5.0);
  prof_10p0->GetXaxis ()->SetRangeUser (0.0, 5.0);
  prof_50p0->GetXaxis ()->SetRangeUser (0.0, 5.0);
  prof_100p0->GetXaxis ()->SetRangeUser (0.0, 5.0);

  prof_0p7->GetYaxis ()->SetLimits (low, high);
  prof_1p0->GetYaxis ()->SetLimits (low, high);
  prof_10p0->GetYaxis ()->SetLimits (low, high);
  prof_50p0->GetYaxis ()->SetLimits (low, high);
  prof_100p0->GetYaxis ()->SetLimits (low, high);

  prof_0p7->GetYaxis ()->SetRangeUser (low, high);
  prof_1p0->GetYaxis ()->SetRangeUser (low, high);
  prof_10p0->GetYaxis ()->SetRangeUser (low, high);
  prof_50p0->GetYaxis ()->SetRangeUser (low, high);
  prof_100p0->GetYaxis ()->SetRangeUser (low, high);

  string object = "track";
  if (dir == "electrons")
    object = "electron";
  else if (dir == "muons")
    object = "muon";
  else if (dir == "chargedHadrons")
    object = "charged hadron";
  else if (dir == "fakeTracks")
    object = "fake track";

  prof_0p7->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());
  prof_1p0->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());
  prof_10p0->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());
  prof_50p0->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());
  prof_100p0->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());

  if (hist == "pt")
    {
      prof_0p7->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
      prof_1p0->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
      prof_10p0->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
      prof_50p0->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
      prof_100p0->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
    }
  else if (hist == "d0")
    {
      prof_0p7->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
      prof_1p0->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
      prof_10p0->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
      prof_50p0->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
      prof_100p0->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
    }
  else if (hist == "dz")
    {
      prof_0p7->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
      prof_1p0->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
      prof_10p0->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
      prof_50p0->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
      prof_100p0->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
    }
  else
    {
      prof_0p7->GetYaxis ()->SetTitle ("#sigma");
      prof_1p0->GetYaxis ()->SetTitle ("#sigma");
      prof_10p0->GetYaxis ()->SetTitle ("#sigma");
      prof_50p0->GetYaxis ()->SetTitle ("#sigma");
      prof_100p0->GetYaxis ()->SetTitle ("#sigma");
    }


  prof_0p7->GetXaxis ()->SetLabelSize (0.04);
  prof_1p0->GetXaxis ()->SetLabelSize (0.04);
  prof_10p0->GetXaxis ()->SetLabelSize (0.04);
  prof_50p0->GetXaxis ()->SetLabelSize (0.04);
  prof_100p0->GetXaxis ()->SetLabelSize (0.04);

  prof_0p7->GetYaxis ()->SetLabelSize (0.04);
  prof_1p0->GetYaxis ()->SetLabelSize (0.04);
  prof_10p0->GetYaxis ()->SetLabelSize (0.04);
  prof_50p0->GetYaxis ()->SetLabelSize (0.04);
  prof_100p0->GetYaxis ()->SetLabelSize (0.04);

  prof_0p7->GetXaxis ()->SetLabelOffset (0.005);
  prof_1p0->GetXaxis ()->SetLabelOffset (0.005);
  prof_10p0->GetXaxis ()->SetLabelOffset (0.005);
  prof_50p0->GetXaxis ()->SetLabelOffset (0.005);
  prof_100p0->GetXaxis ()->SetLabelOffset (0.005);

  prof_0p7->GetYaxis ()->SetLabelOffset (0.005);
  prof_1p0->GetYaxis ()->SetLabelOffset (0.005);
  prof_10p0->GetYaxis ()->SetLabelOffset (0.005);
  prof_50p0->GetYaxis ()->SetLabelOffset (0.005);
  prof_100p0->GetYaxis ()->SetLabelOffset (0.005);

  prof_0p7->GetXaxis ()->SetTitleSize (0.04);
  prof_1p0->GetXaxis ()->SetTitleSize (0.04);
  prof_10p0->GetXaxis ()->SetTitleSize (0.04);
  prof_50p0->GetXaxis ()->SetTitleSize (0.04);
  prof_100p0->GetXaxis ()->SetTitleSize (0.04);

  prof_0p7->GetYaxis ()->SetTitleSize (0.04);
  prof_1p0->GetYaxis ()->SetTitleSize (0.04);
  prof_10p0->GetYaxis ()->SetTitleSize (0.04);
  prof_50p0->GetYaxis ()->SetTitleSize (0.04);
  prof_100p0->GetYaxis ()->SetTitleSize (0.04);

  prof_0p7->GetXaxis ()->SetTitleOffset (1.0);
  prof_1p0->GetXaxis ()->SetTitleOffset (1.0);
  prof_10p0->GetXaxis ()->SetTitleOffset (1.0);
  prof_50p0->GetXaxis ()->SetTitleOffset (1.0);
  prof_100p0->GetXaxis ()->SetTitleOffset (1.0);

  prof_0p7->GetYaxis ()->SetTitleOffset (1.2);
  prof_1p0->GetYaxis ()->SetTitleOffset (1.2);
  prof_10p0->GetYaxis ()->SetTitleOffset (1.2);
  prof_50p0->GetYaxis ()->SetTitleOffset (1.2);
  prof_100p0->GetYaxis ()->SetTitleOffset (1.2);

  prof_0p7->GetXaxis ()->SetNdivisions (505);
  prof_1p0->GetXaxis ()->SetNdivisions (505);
  prof_10p0->GetXaxis ()->SetNdivisions (505);
  prof_50p0->GetXaxis ()->SetNdivisions (505);
  prof_100p0->GetXaxis ()->SetNdivisions (505);

  prof_0p7->GetYaxis ()->SetNdivisions (505);
  prof_1p0->GetYaxis ()->SetNdivisions (505);
  prof_10p0->GetYaxis ()->SetNdivisions (505);
  prof_50p0->GetYaxis ()->SetNdivisions (505);
  prof_100p0->GetYaxis ()->SetNdivisions (505);

  prof_0p7->SetMarkerStyle (20);
  prof_1p0->SetMarkerStyle (20);
  prof_10p0->SetMarkerStyle (20);
  prof_50p0->SetMarkerStyle (20);
  prof_100p0->SetMarkerStyle (20);

  prof_0p7->SetMarkerSize (1.5);
  prof_1p0->SetMarkerSize (1.5);
  prof_10p0->SetMarkerSize (1.5);
  prof_50p0->SetMarkerSize (1.5);
  prof_100p0->SetMarkerSize (1.5);

  prof_0p7->SetMarkerColor (kBlack);
  prof_1p0->SetMarkerColor (kBlue);
  prof_10p0->SetMarkerColor (kRed);
  prof_50p0->SetMarkerColor (kGreen);
  prof_100p0->SetMarkerColor (kMagenta);

  prof_0p7->SetLineColor (kBlack);
  prof_1p0->SetLineColor (kBlue);
  prof_10p0->SetLineColor (kRed);
  prof_50p0->SetLineColor (kGreen);
  prof_100p0->SetLineColor (kMagenta);

  prof_0p7->SetLineWidth (3);
  prof_1p0->SetLineWidth (3);
  prof_10p0->SetLineWidth (3);
  prof_50p0->SetLineWidth (3);
  prof_100p0->SetLineWidth (3);

  TPaveText *pt0 = new TPaveText(0.123116,0.924823,0.214824,0.970958,"brNDC");
  pt0->SetBorderSize(0);
  pt0->SetFillStyle(0);
  pt0->SetTextSize(0.0388601);
  pt0->AddText("CMS");

  TPaveText *pt1 = new TPaveText(0.226131,0.920823,0.577889,0.966958,"brNDC");
  pt1->SetBorderSize(0);
  pt1->SetFillStyle(0);
  pt1->SetTextFont(52);
  pt1->SetTextSize(0.0388601);
  pt1->AddText("Simulation Preliminary");

  TPaveText *pt2 = new TPaveText(0.769672,0.919041,0.885643,0.966968,"brNDC");
  pt2->SetBorderSize(0);
  pt2->SetFillStyle(0);
  pt2->SetTextFont(42);
  pt2->SetTextSize(0.0388601);
  pt2->AddText("14 TeV");

  TLegend *leg = new TLegend (0.164573,0.695761,0.346734,0.887781,NULL,"brNDC");
  leg->SetBorderSize(0);
  leg->SetTextSize(0.03740648);
  leg->SetFillStyle(0);
  leg->AddEntry (prof_0p7, "p_{T} = 0.7 GeV", "p");
  leg->AddEntry (prof_1p0, "p_{T} = 1 GeV", "p");
  leg->AddEntry (prof_10p0, "p_{T} = 10 GeV", "p");
  leg->AddEntry (prof_50p0, "p_{T} = 50 GeV", "p");
  leg->AddEntry (prof_100p0, "p_{T} = 100 GeV", "p");

  TCanvas *c1 = new TCanvas("c1", "c1",514,55,800,830);
  c1->Range(-38.9644,-27.73994,321.6828,306.8731);
  c1->SetFillColor(0);
  c1->SetBorderMode(0);
  c1->SetBorderSize(2);
  c1->SetTickx(1);
  c1->SetTicky(1);
  c1->SetRightMargin(0.1155779);
  c1->SetTopMargin(0.08031088);
  c1->SetBottomMargin(0.08290155);
  c1->SetFrameFillStyle(0);
  c1->SetFrameBorderMode(0);
  c1->SetFrameFillStyle(0);
  c1->SetFrameBorderMode(0);

  c1->SetLogy ();
  c1->SetGridx ();
  c1->SetGridy ();

  c1->cd ();
  prof_0p7->Clone ()->Draw ();
  prof_1p0->Clone ()->Draw ("same");
  prof_10p0->Clone ()->Draw ("same");
  prof_50p0->Clone ()->Draw ("same");
  prof_100p0->Clone ()->Draw ("same");
  pt0->Clone ()->Draw ("same");
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  leg->Clone ()->Draw ("same");

  size_t position = file.find(".root");
  string fileName = file.substr(0,position);
  TString pdfName= fileName+"_"+hist + "ErrorVsTrackEta.pdf";
  c1->SaveAs(pdfName);
}
