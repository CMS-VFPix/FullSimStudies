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
plot (const string &dir, const string &hist, const string& ptRange, const double low, const double high)
{
  gStyle->SetOptStat(0);

  string file[5] = {"VBF_HTo4L_FPix800x52.root",
		    "VBF_HTo4L_FPix80x5.root",
		    "VBF_HTo4L_FPix80x52.root",
		    "VBF_HTo4L_FPix80x520.root",
		    "VBF_HTo4L_FPix8x52.root"};
  TFile *fin0 = TFile::Open (file[0].c_str ());
  TFile *fin1 = TFile::Open (file[1].c_str ());
  TFile *fin2 = TFile::Open (file[2].c_str ());
  TFile *fin3 = TFile::Open (file[3].c_str ());
  TFile *fin4 = TFile::Open (file[4].c_str ());

  TH2D *errorVsTrackEta0,
    *errorVsTrackEta1,
    *errorVsTrackEta2,
    *errorVsTrackEta3,
    *errorVsTrackEta4;
  errorVsTrackEta0 = (TH2D *) fin0->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_"+ptRange).c_str ());
  errorVsTrackEta0->SetName("h1");
  errorVsTrackEta1 = (TH2D *) fin1->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_"+ptRange).c_str ());
  errorVsTrackEta1->SetName("h2");
  errorVsTrackEta2 = (TH2D *) fin2->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_"+ptRange).c_str ());
  errorVsTrackEta2->SetName("h3");
  errorVsTrackEta3 = (TH2D *) fin3->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_"+ptRange).c_str ());
  errorVsTrackEta3->SetName("h4");
  errorVsTrackEta4 = (TH2D *) fin4->Get (("VFPixAnalyzer/" + dir + "/" + hist + "ErrorVsTrackEta_"+ptRange).c_str ());
  errorVsTrackEta4->SetName("h5");

  errorVsTrackEta0->SetDirectory (0);
  errorVsTrackEta1->SetDirectory (0);
  errorVsTrackEta2->SetDirectory (0);
  errorVsTrackEta3->SetDirectory (0);
  errorVsTrackEta4->SetDirectory (0);

  /*
  fin0->Close ();
  fin1->Close ();
  fin2->Close ();
  fin3->Close ();
  fin4->Close ();
  */
  
  errorVsTrackEta0->Rebin2D ();
  errorVsTrackEta1->Rebin2D ();
  errorVsTrackEta2->Rebin2D ();
  errorVsTrackEta3->Rebin2D ();
  errorVsTrackEta4->Rebin2D ();

  errorVsTrackEta0->Rebin2D ();
  errorVsTrackEta1->Rebin2D ();
  errorVsTrackEta2->Rebin2D ();
  errorVsTrackEta3->Rebin2D ();
  errorVsTrackEta4->Rebin2D ();

  errorVsTrackEta0->Rebin2D ();
  errorVsTrackEta1->Rebin2D ();
  errorVsTrackEta2->Rebin2D ();
  errorVsTrackEta3->Rebin2D ();
  errorVsTrackEta4->Rebin2D ();

  errorVsTrackEta0->Rebin2D ();
  errorVsTrackEta1->Rebin2D ();
  errorVsTrackEta2->Rebin2D ();
  errorVsTrackEta3->Rebin2D ();
  errorVsTrackEta4->Rebin2D ();

  errorVsTrackEta0->Rebin2D ();
  errorVsTrackEta1->Rebin2D ();
  errorVsTrackEta2->Rebin2D ();
  errorVsTrackEta3->Rebin2D ();
  errorVsTrackEta4->Rebin2D ();

  TH1D *prof0,
    *prof1,
    *prof2,
    *prof3,
    *prof4;
  prof0 = (TH1D *) errorVsTrackEta0->ProfileX ();
  prof1 = (TH1D *) errorVsTrackEta1->ProfileX ();
  prof2 = (TH1D *) errorVsTrackEta2->ProfileX ();
  prof3 = (TH1D *) errorVsTrackEta3->ProfileX ();
  prof4 = (TH1D *) errorVsTrackEta4->ProfileX ();

  prof0->GetXaxis ()->SetLimits (0.0, 5.0);
  prof1->GetXaxis ()->SetLimits (0.0, 5.0);
  prof2->GetXaxis ()->SetLimits (0.0, 5.0);
  prof3->GetXaxis ()->SetLimits (0.0, 5.0);
  prof4->GetXaxis ()->SetLimits (0.0, 5.0);

  prof0->GetXaxis ()->SetRangeUser (0.0, 5.0);
  prof1->GetXaxis ()->SetRangeUser (0.0, 5.0);
  prof2->GetXaxis ()->SetRangeUser (0.0, 5.0);
  prof3->GetXaxis ()->SetRangeUser (0.0, 5.0);
  prof4->GetXaxis ()->SetRangeUser (0.0, 5.0);

  prof0->GetYaxis ()->SetLimits (low, high);
  prof1->GetYaxis ()->SetLimits (low, high);
  prof2->GetYaxis ()->SetLimits (low, high);
  prof3->GetYaxis ()->SetLimits (low, high);
  prof4->GetYaxis ()->SetLimits (low, high);

  prof0->GetYaxis ()->SetRangeUser (low, high);
  prof1->GetYaxis ()->SetRangeUser (low, high); 
  prof2->GetYaxis ()->SetRangeUser (low, high);
  prof3->GetYaxis ()->SetRangeUser (low, high);
  prof4->GetYaxis ()->SetRangeUser (low, high);

  string object = "track";
  if (dir == "electrons")
    object = "electron";
  else if (dir == "muons")
    object = "muon";
  else if (dir == "chargedHadrons")
    object = "charged hadron";
  else if (dir == "fakeTracks")
    object = "fake track";

  prof0->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());
  prof1->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());
  prof2->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());
  prof3->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());
  prof4->GetXaxis ()->SetTitle ((object + " |#eta|").c_str ());

  if (hist == "pt")
    {
      prof0->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
      prof1->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
      prof2->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
      prof3->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
      prof4->GetYaxis ()->SetTitle ("#sigma(#deltap_{T}/p_{T}) [%]");
    }
  else if (hist == "d0")
    {
      prof0->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
      prof1->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
      prof2->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
      prof3->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
      prof4->GetYaxis ()->SetTitle ("#sigma(#deltad_{0}) [cm]");
    }
  else if (hist == "dz")
    {
      prof0->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
      prof1->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
      prof2->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
      prof3->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
      prof4->GetYaxis ()->SetTitle ("#sigma(#deltad_{z}) [cm]");
    }
  else
    {
      prof0->GetYaxis ()->SetTitle ("#sigma");
      prof1->GetYaxis ()->SetTitle ("#sigma");
      prof2->GetYaxis ()->SetTitle ("#sigma");
      prof3->GetYaxis ()->SetTitle ("#sigma");
      prof4->GetYaxis ()->SetTitle ("#sigma");
    }


  prof0->GetXaxis ()->SetLabelSize (0.04);
  prof1->GetXaxis ()->SetLabelSize (0.04);
  prof2->GetXaxis ()->SetLabelSize (0.04);
  prof3->GetXaxis ()->SetLabelSize (0.04);
  prof4->GetXaxis ()->SetLabelSize (0.04);

  prof0->GetYaxis ()->SetLabelSize (0.04);
  prof1->GetYaxis ()->SetLabelSize (0.04);
  prof2->GetYaxis ()->SetLabelSize (0.04);
  prof3->GetYaxis ()->SetLabelSize (0.04);
  prof4->GetYaxis ()->SetLabelSize (0.04);

  prof0->GetXaxis ()->SetLabelOffset (0.005);
  prof1->GetXaxis ()->SetLabelOffset (0.005);
  prof2->GetXaxis ()->SetLabelOffset (0.005);
  prof3->GetXaxis ()->SetLabelOffset (0.005);
  prof4->GetXaxis ()->SetLabelOffset (0.005);

  prof0->GetYaxis ()->SetLabelOffset (0.005);
  prof1->GetYaxis ()->SetLabelOffset (0.005);
  prof2->GetYaxis ()->SetLabelOffset (0.005);
  prof3->GetYaxis ()->SetLabelOffset (0.005);
  prof4->GetYaxis ()->SetLabelOffset (0.005);

  prof0->GetXaxis ()->SetTitleSize (0.04);
  prof1->GetXaxis ()->SetTitleSize (0.04);
  prof2->GetXaxis ()->SetTitleSize (0.04);
  prof3->GetXaxis ()->SetTitleSize (0.04);
  prof4->GetXaxis ()->SetTitleSize (0.04);

  prof0->GetYaxis ()->SetTitleSize (0.04);
  prof1->GetYaxis ()->SetTitleSize (0.04);
  prof2->GetYaxis ()->SetTitleSize (0.04);
  prof3->GetYaxis ()->SetTitleSize (0.04);
  prof4->GetYaxis ()->SetTitleSize (0.04);

  prof0->GetXaxis ()->SetTitleOffset (1.0);
  prof1->GetXaxis ()->SetTitleOffset (1.0);
  prof2->GetXaxis ()->SetTitleOffset (1.0);
  prof3->GetXaxis ()->SetTitleOffset (1.0);
  prof4->GetXaxis ()->SetTitleOffset (1.0);

  prof0->GetYaxis ()->SetTitleOffset (1.2);
  prof1->GetYaxis ()->SetTitleOffset (1.2);
  prof2->GetYaxis ()->SetTitleOffset (1.2);
  prof3->GetYaxis ()->SetTitleOffset (1.2);
  prof4->GetYaxis ()->SetTitleOffset (1.2);

  prof0->GetXaxis ()->SetNdivisions (505);
  prof1->GetXaxis ()->SetNdivisions (505);
  prof2->GetXaxis ()->SetNdivisions (505);
  prof3->GetXaxis ()->SetNdivisions (505);
  prof4->GetXaxis ()->SetNdivisions (505);

  prof0->GetYaxis ()->SetNdivisions (505);
  prof1->GetYaxis ()->SetNdivisions (505);
  prof2->GetYaxis ()->SetNdivisions (505);
  prof3->GetYaxis ()->SetNdivisions (505);
  prof4->GetYaxis ()->SetNdivisions (505);

  prof0->SetMarkerStyle (20);
  prof1->SetMarkerStyle (20);
  prof2->SetMarkerStyle (20);
  prof3->SetMarkerStyle (20);
  prof4->SetMarkerStyle (20);

  prof0->SetMarkerSize (1.5);
  prof1->SetMarkerSize (1.5);
  prof2->SetMarkerSize (1.5);
  prof3->SetMarkerSize (1.5);
  prof4->SetMarkerSize (1.5);

  prof0->SetMarkerColor (kBlack);
  prof1->SetMarkerColor (kBlue);
  prof2->SetMarkerColor (kRed);
  prof3->SetMarkerColor (kGreen);
  prof4->SetMarkerColor (kMagenta);

  prof0->SetLineColor (kBlack);
  prof1->SetLineColor (kBlue);
  prof2->SetLineColor (kRed);
  prof3->SetLineColor (kGreen);
  prof4->SetLineColor (kMagenta);

  prof0->SetLineWidth (3);
  prof1->SetLineWidth (3);
  prof2->SetLineWidth (3);
  prof3->SetLineWidth (3);
  prof4->SetLineWidth (3);

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

  size_t startPosition = file[0].find("VBF_HTo4L_FPix") + 14;

  size_t endPosition0 = file[0].find(".root")-14;
  size_t endPosition1 = file[1].find(".root")-14;
  size_t endPosition2 = file[2].find(".root")-14;
  size_t endPosition3 = file[3].find(".root")-14;
  size_t endPosition4 = file[4].find(".root")-14;

  TLegend *leg = new TLegend (0.164573,0.695761,0.346734,0.887781,NULL,"brNDC");
  leg->SetBorderSize(0);
  leg->SetTextSize(0.03740648);
  leg->SetFillStyle(0);

  const char *pixelSize0 = ("Pixel size = "+file[0].substr(startPosition,endPosition0)).c_str();
  leg->AddEntry (prof0, pixelSize0, "p");
  const char *pixelSize1 = ("Pixel size = "+file[1].substr(startPosition,endPosition1)).c_str();
  leg->AddEntry (prof1, pixelSize1, "p");
  const char *pixelSize2 = ("Pixel size = "+file[2].substr(startPosition,endPosition2)).c_str();
  leg->AddEntry (prof2, pixelSize2, "p");
  const char *pixelSize3 = ("Pixel size = "+file[3].substr(startPosition,endPosition3)).c_str();
  leg->AddEntry (prof3, pixelSize3, "p");
  const char *pixelSize4 = ("Pixel size = "+file[4].substr(startPosition,endPosition4)).c_str();
  leg->AddEntry (prof4, pixelSize4, "p");

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
  prof0->Clone ()->Draw ();
  prof1->Clone ()->Draw ("same");
  prof2->Clone ()->Draw ("same");
  prof3->Clone ()->Draw ("same");
  prof4->Clone ()->Draw ("same");
  pt0->Clone ()->Draw ("same");
  pt1->Clone ()->Draw ("same");
  pt2->Clone ()->Draw ("same");
  leg->Clone ()->Draw ("same");

  TString pdfName= hist + "ErrorVsTrackEta_"+ptRange+".pdf";
  c1->SaveAs(pdfName);


}
