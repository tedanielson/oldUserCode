{
  
#include "TCanvas.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile.h"
#include "THStack.h"
#include "TLegend.h"
#include "TFractionFitter.h"
#include "TObjArray.h"
#include "TAxis.h"
#include "histtools.C"
#include "Style.C"
#include "validation.h"
#include "trigger.C"
  //#include "b_tag_eff_estimation.h"  
  setTDRStyle();
  gStyle->SetPalette(1);
  gStyle->SetOptTitle(1);
  gStyle->SetStatY(0.87);
  gStyle->SetStatX(0.87);

  TCanvas *c1 = new TCanvas("c1","c1");
  TLegend *leg1 = new TLegend(.4,.20,.6,.40);
  TLegend *leg2 = new TLegend(.6,.64,.89,.89);
  TLegend *leg3 = new TLegend(.6,.64,.85,.89);
  TLegend *leg4 = new TLegend(.6,.74,.85,.89);
  TLegend *legg = new TLegend(.6,.64,.85,.89);
  
  home_dir = gDirectory;

  TFile f0("SingleMu_HT_MET_effs_2012D_Promptv1.root");
  eff1 = drawEff(Mu40_PFNoPUHT350_HT_num,Mu40_PFNoPUHT350_HT_denom,"HT (GeV)","HT Turn-On for Mu40_PFNoPUHT350",0,0.,600.,1,8,"");
  c1->Print("Mu40_PFNoPUHT350_HT_eff_2012D_Promptv1.eps");

  eff1 = drawEff(PFNoPUHT350_Mu15_PFMET45_MET_num,PFNoPUHT350_Mu15_PFMET45_MET_denom,"pfMET (GeV)","pfMET Turn-On for PFNoPUHT350_Mu15_PFMET45",0,0.,250.,1,8,"");
  c1->Print("PFNoPUHT350_Mu15_PFMET45_MET_eff_2012D_Promptv1.eps");
  
  eff1 = drawEff(PFNoPUHT400_Mu5_PFMET45_MET_num,PFNoPUHT400_Mu5_PFMET45_MET_denom,"pfMET (GeV)","pfMET Turn-On for PFNoPUHT400_Mu15_PFMET45",0,0.,250.,1,8,"");
  c1->Print("PFNoPUHT400_Mu5_PFMET45_MET_eff_2012D_Promptv1.eps");

  PFNoPUHT350_Mu15_PFMET45_HT_MET_eff->SetTitle("Eff map for (HT,MET,Mu pT) = (350,45,15)");
  PFNoPUHT350_Mu15_PFMET45_HT_MET_eff->SetXTitle("HT (GeV)");
  PFNoPUHT350_Mu15_PFMET45_HT_MET_eff->SetYTitle("pfMET (GeV)");
  PFNoPUHT350_Mu15_PFMET45_HT_MET_eff->SetMinimum(-1.0);
  PFNoPUHT350_Mu15_PFMET45_HT_MET_eff->SetMaximum(1.0);
  PFNoPUHT350_Mu15_PFMET45_HT_MET_eff->Draw("COLZ");
  c1->Print("PFNoPUHT350_Mu15_PFMET45_HT_MET_eff_2012D_Promptv1.eps");

}
