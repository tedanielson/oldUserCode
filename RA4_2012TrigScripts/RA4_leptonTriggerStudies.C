//#include "METzCalculator.C"
//#include "JetCombinatorics.C"
#include "PublicScript.h"
#include "TMath.h"
#include "TFile.h"
#include "TChain.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TROOT.h"
#include "TH1F.h"
#include "TH2F.h"
#include <iostream>
#include <fstream>
#include "TString.h"
#include "TVector3.h"
#include "TGraphAsymmErrors.h"
#include "TMatrixDSym.h"
#include "TMatrixDSymEigen.h"
#include "SelectionCfaSynchJul15.h"
#include "inJSON2012.h"

using namespace std;

const float JetPTThresholdNJ = 40;
const float JetPTThresholdHT = 40;

double deltaphi(double phi1, double phi2)
{
  double result = fabs(phi1-phi2);
  if (result>TMath::Pi()) result = 2*TMath::Pi() - result;
  return result;
}
float dR(float eta1, float phi1, float eta2, float phi2) {
  return sqrt(pow(eta1-eta2, 2) + pow(fabs(deltaphi(phi1,phi2)), 2)) ;
}
void divide_TH2_histos_and_errors(TH2F* HIS1, TH2F* HIS2, TH2F* HIS3) {
  // HIS1 = numerator
  // HIS2 = denominator
  // HIS3 = ratio
  Int_t nbinsX = HIS1->GetNbinsX(); // find out nr of bins to loop over.
  Int_t nbinsY = HIS1->GetNbinsY();
  for(Int_t ibinsX=1; ibinsX <= nbinsX; ibinsX ++) {
    for (Int_t ibinsY=1; ibinsY <= nbinsY; ibinsY ++) {
      Float_t content_1 = HIS1->GetBinContent(ibinsX, ibinsY);
      Float_t content_2 = HIS2->GetBinContent(ibinsX, ibinsY);
      Float_t error_1 = HIS1->GetBinError(ibinsX, ibinsY);
      Float_t error_2 = HIS2->GetBinError(ibinsX, ibinsY);

      if (content_2 != 0) {
        HIS3->SetBinContent(ibinsX, ibinsY, content_1/content_2);
        HIS3->SetBinError(ibinsX, ibinsY, error_1/content_2);
      }
      else {
        HIS3->SetBinContent(ibinsX, ibinsY, -1);
        HIS3->SetBinError(ibinsX, ibinsY, -1);
      }
    }
  }
}

void divide_histos_and_errors(TH1F* HIS1, TH1F* HIS2, TH1F* HIS3) {
  // HIS1 = numerator
  // HIS2 = denominator
  // HIS3 = ratio
  Int_t nbins1 = HIS1->GetNbinsX(); // find out nr of bins to loop over.
  for(Int_t ibins1=1 ; ibins1 <= nbins1 ; ibins1 ++) {
    Float_t content_1 = HIS1->GetBinContent(ibins1);
    Float_t content_2 = HIS2->GetBinContent(ibins1);
    Float_t error_1 = HIS1->GetBinError(ibins1);
    Float_t error_2 = HIS2->GetBinError(ibins1);

    if (content_2 != 0) {
      HIS3->SetBinContent(ibins1, content_1/content_2);
      HIS3->SetBinError(ibins1, error_1/content_2);
    }
  }
}

bool passedMuonCleaning( int imuon ) {
  float mydR = 999;
  float pfMuonPt = 99999;
  
  for(uint jmuon = 0; jmuon < mus_pt->size(); jmuon++) {
    float mydR_tmp = dR( mus_eta->at(imuon),mus_phi->at(imuon),mus_eta->at(jmuon),mus_phi->at(jmuon) );
    
    if( mydR > mydR_tmp ) { mydR = mydR_tmp ; pfMuonPt = mus_pt->at(jmuon); }
  }
  
  if( mydR < 0.5 ) {
    return 
      ( fabs(mus_pt->at(imuon)-pfMuonPt)/mus_pt->at(imuon) < 0.2 ) && 
      ( mus_cm_ptErr->at(imuon)/pow(mus_pt->at(imuon),2) < 0.001 );
  }
  
  return false;
}

void tree1r(TChain *chainB,TChain *chainA,TString output_filename,double cross_section_pb)
{

  
  int maxRun = 0;

  //----------------------------------------------------------  
  //This initializes both Trees, meaning it sets all the branch addresses, etc. This Initialize function is defined in PublicScript.h
  //----------------------------------------------------------
  InitializeB(chainB);
  InitializeA(chainA);

 
  //----------------------------------------------------------
  //Define output file
  //----------------------------------------------------------
  TString root_name = output_filename+".root";
  TString text_name = output_filename+".txt";
  TFile *test = new TFile(root_name.Data(),"RECREATE");
  test->cd();
  
  ofstream bleeper;
  bleeper.open("failedEvents.txt");
  //  out2.open("GeneratingParticles.txt",ios::out | ios::app)
  

  /*
    Ok...Let's try and figure this bleep out again.
    
    There's a T&P efficiency for the single lepton trigger.  That's going to be handled by the fecking Vienna code.
    
    Right, then for this bit of code, we just want to tackle the HT_MHT legs for the Mu_HT(_MHT) and Ele_HT(_MHT) triggers.

    This means applying a baseline trigger selection (e.g. Mu15 etc) then checking the eff of the cross triggers w.r.t. HT, MHT
  
    As far as purity goes, I'm not sure...Let's start with what we know and go from there

    The grand list of triggers
    MuHad                     Mu(Ref)          ElectronHad                                                       Electron(Ref)

    Mu40_PFHT350              Mu40             CleanPFHT300_Ele40_CaloIdVT_TrkIdT                                Ele80_CaloIdVT_TrkIdT
    Mu40_PFNoPUHT350          Mu40             CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT                            Ele80_CaloIdVT_GsfTrkIdT
                                               
    PFHT350_Mu15_PFMET45      Mu40             CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45      Ele27_WP80
    PFHT400_Mu5_PFMET45       Mu40             CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45       Ele27_WP80
    PFNoPUHT350_Mu15_PFMET45  Mu40             CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45  Ele27_WP80
    PFNoPUHT400_Mu5_PFMET45   Mu40             CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45   Ele27_WP80
    
    For the 3-leg trigger, we have to do a bit more homework.  We want to isolate the performance of the individual legs

    I think the easiest thing to do is this:
    1) Get HT plateau values from the lep_HT triggers

    Results:
       Mu_Had: 
           HT200 is fully efficient at 350 offline
	   HT300 is fully efficient at (400?)
       Electron_Had: 
           HT200 is fully efficient near 300 offline
	   Same with HT250
	   HT350 is fully efficient at 350 offline
	   HT400 is fully efficient at 400 offline

    2) Apply plateau + ref trigger to lep_HT_MHT triggers to get PFMHT turn-on
    3) Get MET plateau for lep_HT_MHT paths, apply for HT legs of lep_HT_MHT paths

    OR (you muppet!) we can do something smarter (like we've done before)
    Let's do 2 and 3 to factorize each leg AND, in addition, do some TH2's for the HT and MET legs simultaneously.

  */

  //----------------------------------------------------------
  //Histogram Declarations
  //----------------------------------------------------------

  TH1F *IsoMu24_pT_num = new TH1F("IsoMu24_pT_num","",25,0,100);
  TH1F *IsoMu24_pT_denom = new TH1F("IsoMu24_pT_denom","",25,0,100);
  TH1F *IsoMu24_pT_eff = new TH1F("IsoMu24_pT_eff","",25,0,100);
  
  TH1F *Mu40_PFHT350_HT_num = new TH1F("Mu40_PFHT350_HT_num","",30,0,600);
  TH1F *Mu40_PFHT350_HT_denom = new TH1F("Mu40_PFHT350_HT_denom","",30,0,600);
  TH1F *Mu40_PFHT350_HT_eff = new TH1F("Mu40_PFHT350_HT_eff","",30,0,600);

  TH1F *Mu40_PFNoPUHT350_HT_num = new TH1F("Mu40_PFNoPUHT350_HT_num","",30,0,600);
  TH1F *Mu40_PFNoPUHT350_HT_denom = new TH1F("Mu40_PFNoPUHT350_HT_denom","",30,0,600);
  TH1F *Mu40_PFNoPUHT350_HT_eff = new TH1F("Mu40_PFNoPUHT350_HT_eff","",30,0,600);

  TH1F *PFHT350_Mu15_PFMET45_MET_num = new TH1F("PFHT350_Mu15_PFMET45_MET_num","",25,0,250);
  TH1F *PFHT350_Mu15_PFMET45_MET_denom = new TH1F("PFHT350_Mu15_PFMET45_MET_denom","",25,0,250);
  TH1F *PFHT350_Mu15_PFMET45_MET_eff = new TH1F("PFHT350_Mu15_PFMET45_MET_eff","",25,0,250);

  TH1F *PFHT400_Mu5_PFMET45_MET_num = new TH1F("PFHT400_Mu5_PFMET45_MET_num","",25,0,250);
  TH1F *PFHT400_Mu5_PFMET45_MET_denom = new TH1F("PFHT400_Mu5_PFMET45_MET_denom","",25,0,250);
  TH1F *PFHT400_Mu5_PFMET45_MET_eff = new TH1F("PFHT400_Mu5_PFMET45_MET_eff","",25,0,250);

  TH1F *PFNoPUHT350_Mu15_PFMET45_MET_num = new TH1F("PFNoPUHT350_Mu15_PFMET45_MET_num","",25,0,250);
  TH1F *PFNoPUHT350_Mu15_PFMET45_MET_denom = new TH1F("PFNoPUHT350_Mu15_PFMET45_MET_denom","",25,0,250);
  TH1F *PFNoPUHT350_Mu15_PFMET45_MET_eff = new TH1F("PFNoPUHT350_Mu15_PFMET45_MET_eff","",25,0,250);
  
  TH1F *PFNoPUHT400_Mu5_PFMET45_MET_num = new TH1F("PFNoPUHT400_Mu5_PFMET45_MET_num","",25,0,250);
  TH1F *PFNoPUHT400_Mu5_PFMET45_MET_denom = new TH1F("PFNoPUHT400_Mu5_PFMET45_MET_denom","",25,0,250);
  TH1F *PFNoPUHT400_Mu5_PFMET45_MET_eff = new TH1F("PFNoPUHT400_Mu5_PFMET45_MET_eff","",25,0,250);
  
  TH2F *PFHT350_Mu15_PFMET45_HT_MET_num = new TH2F("PFHT350_Mu15_PFMET45_HT_MET_num","",30,0,600,25,0,250);
  TH2F *PFHT350_Mu15_PFMET45_HT_MET_denom = new TH2F("PFHT350_Mu15_PFMET45_HT_MET_denom","",30,0,600,25,0,250);
  TH2F *PFHT350_Mu15_PFMET45_HT_MET_eff = new TH2F("PFHT350_Mu15_PFMET45_HT_MET_eff","",30,0,600,25,0,250);

  TH2F *PFHT400_Mu5_PFMET45_HT_MET_num = new TH2F("PFHT400_Mu5_PFMET45_HT_MET_num","",30,0,600,25,0,250);
  TH2F *PFHT400_Mu5_PFMET45_HT_MET_denom = new TH2F("PFHT400_Mu5_PFMET45_HT_MET_denom","",30,0,600,25,0,250);
  TH2F *PFHT400_Mu5_PFMET45_HT_MET_eff = new TH2F("PFHT400_Mu5_PFMET45_HT_MET_eff","",30,0,600,25,0,250);

  TH2F *PFNoPUHT350_Mu15_PFMET45_HT_MET_num = new TH2F("PFNoPUHT350_Mu15_PFMET45_HT_MET_num","",30,0,600,25,0,250);
  TH2F *PFNoPUHT350_Mu15_PFMET45_HT_MET_denom = new TH2F("PFNoPUHT350_Mu15_PFMET45_HT_MET_denom","",30,0,600,25,0,250);
  TH2F *PFNoPUHT350_Mu15_PFMET45_HT_MET_eff = new TH2F("PFNoPUHT350_Mu15_PFMET45_HT_MET_eff","",30,0,600,25,0,250);

  TH2F *PFNoPUHT400_Mu5_PFMET45_HT_MET_num = new TH2F("PFNoPUHT400_Mu5_PFMET45_HT_MET_num","",30,0,600,25,0,250);
  TH2F *PFNoPUHT400_Mu5_PFMET45_HT_MET_denom = new TH2F("PFNoPUHT400_Mu5_PFMET45_HT_MET_denom","",30,0,600,25,0,250);
  TH2F *PFNoPUHT400_Mu5_PFMET45_HT_MET_eff = new TH2F("PFNoPUHT400_Mu5_PFMET45_HT_MET_eff","",30,0,600,25,0,250);

  TH1F *CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_num = new TH1F("CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_num","",25,0,1000);
  TH1F *CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_denom = new TH1F("CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_denom","",25,0,1000);
  TH1F *CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_eff = new TH1F("CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_eff","",25,0,1000);

  TH1F *CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_num = new TH1F("CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_num","",25,0,1000);
  TH1F *CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_denom = new TH1F("CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_denom","",25,0,1000);
  TH1F *CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_eff = new TH1F("CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_eff","",25,0,1000);

  TH1F *HT_dist_fail_Ele_HT = new TH1F("HT_dist_fail_Ele_HT","",10,400,600);

  TH1F *CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num = new TH1F("CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num","",25,0,250);
  TH1F *CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom = new TH1F("CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom","",25,0,250);
  TH1F *CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff = new TH1F("CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff","",25,0,250);
  
  TH1F *CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num = new TH1F("CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num","",25,0,250);
  TH1F *CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom = new TH1F("CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom","",25,0,250);
  TH1F *CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff = new TH1F("CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff","",25,0,250);

  TH1F *CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num = new TH1F("CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num","",25,0,250);
  TH1F *CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom = new TH1F("CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom","",25,0,250);
  TH1F *CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff = new TH1F("CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff","",25,0,250);
 
  TH1F *CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num = new TH1F("CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num","",25,0,250);
  TH1F *CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom = new TH1F("CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom","",25,0,250);
  TH1F *CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff = new TH1F("CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff","",25,0,250);

  TH2F *CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num = new TH2F("CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num","",25,0,1000,25,0,250);
  TH2F *CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom = new TH2F("CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom","",25,0,1000,25,0,250);
  TH2F *CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff = new TH2F("CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff","",25,0,1000,25,0,250);

  TH2F *CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num = new TH2F("CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num","",25,0,1000,25,0,250);
  TH2F *CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom = new TH2F("CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom","",25,0,1000,25,0,250);
  TH2F *CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff = new TH2F("CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff","",25,0,1000,25,0,250);

  TH2F *CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num = new TH2F("CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num","",25,0,1000,25,0,250);
  TH2F *CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom = new TH2F("CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom","",25,0,1000,25,0,250);
  TH2F *CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff = new TH2F("CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff","",25,0,1000,25,0,250);

  TH2F *CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num = new TH2F("CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num","",25,0,1000,25,0,250);
  TH2F *CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom = new TH2F("CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom","",25,0,1000,25,0,250);
  TH2F *CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff = new TH2F("CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff","",25,0,1000,25,0,250);

  //----------------------------------------------------------
  //Initializing variables to count events passing certain requirements
  //----------------------------------------------------------
  
  int num_events_in_mu_ht_signal_region = 0;
  int num_events_in_mu_ht_signal_region_triggered = 0;
  int num_events_in_el_ht_signal_region = 0;  
  int num_events_in_el_ht_signal_region_triggered = 0;
  int num_events_in_el_tightID_ht_signal_region = 0;  
  int num_events_in_el_tightID_ht_signal_region_triggered = 0;
  
  double signal_region_eff_mu_ht = 0;
  double signal_region_eff_el_ht = 0;
  double signal_region_eff_el_tightID_ht = 0;

  //----------------------------------------------------------     
  //Number of events to loop over
  //----------------------------------------------------------
  Int_t nentries = (Int_t)chainB->GetEntries();
  //  Int_t nentries = (Int_t)t1->GetEntries();
  //  out<<"The number of entries is: "<<nentries<<endl;
  cout<<"The number of entries is: "<<nentries<<endl;
  double Nentries = chainB->GetEntries();
  //  double weight_1fb=Nentries/(cross_section_pb*1000.);
  
  
  //----------------------------------------------------------
  //Main Event loop
  //----------------------------------------------------------
  vector< vector<int> > VRunLumi = MakeVRunLumi("Golden");

  //    for(int ia = 100; ia<200;ia++){
  //  int num_in_process = 0;
  int npass_2chan = 0;
  int nfail_2chan = 0;
  int npass_3chan = 0;
  int nfail_3chan = 0;
  for(int ia = 0; ia<nentries;ia++){
    if (ia%100 == 0)   cout << "event " << ia << endl;
    //  for(int ia = 0; ia<1000000;ia++){
    //for(int ia = 0; ia<200;ia++){
    
    //    if (ia >= 20000) continue;
    
    double weight = 1.;
    
    chainB->GetEntry(ia);
    chainA->GetEntry(ia);

    //    if (run >= 175877) continue;
    //    if(event==44284){
    if(!inJSON(VRunLumi,run,lumiblock)) continue;        
    
    double beamspot_x=-999.;
    double beamspot_y=-999.;

    if (run > maxRun) maxRun = run;
    
    //    cout<<"I get here 000"<<endl;    
    if(beamSpot_x->size()>0){
      beamspot_x=beamSpot_x->at(0);
      beamspot_y=beamSpot_y->at(0);
    }
    else{cout<<"The beamspot vector is empty"<<endl;}

  //----------------------------------------------------------
  //Initialize global variables
  //----------------------------------------------------------
  bool pass_mu_criteria = false;
  double mu_pt = 0;

  double mu_px = 0;
  double mu_py = 0;  
  double mu_eta = -999.;  
  double mu_phi = -999.;  
  double mu_px_leading = 0;
  double mu_py_leading = 0;  


  int num_jets_after_eta_cut = 0;      
  int num_jets_after_eta_cut_50 = 0;	  
  double met_et = 0; 
  double met_phi = 0;
  double pt_mu_high = 0;
  uint mu_highest_it = 0;
  double M_T = -999.;
  double met_x = -999.;
  double met_y = -999.;
  int mu_sign = 0;
  double genMet = -999.;
  double genMet_phi = -999.;
  double highest_pt_2nd_lepton = -1;      
  double met_over_sumEt=0;
  double met_sumEt=-999.;


    //----------------------------------------------------------
    //Calculate met quantities
    //----------------------------------------------------------

  /*  
      if(pfTypeImets_et->size()>0){
      met_et = pfTypeImets_et->at(0);
      met_phi = pfTypeImets_phi->at(0);
      met_x = pfTypeImets_ex->at(0);
      met_y = pfTypeImets_ey->at(0);
      genMet = pfTypeImets_gen_et->at(0);
      genMet_phi = pfTypeImets_gen_phi->at(0);
      met_sumEt=pfTypeImets_sumEt->at(0);
      }
  */
  
  if(pfTypeImets_et->size()>0){
    met_et = pfTypeImets_et->at(0);
    met_phi = pfTypeImets_phi->at(0);
    met_x = pfTypeImets_ex->at(0);
    met_y = pfTypeImets_ey->at(0);
    genMet = pfTypeImets_gen_et->at(0);
    genMet_phi = pfTypeImets_gen_phi->at(0);
    met_sumEt=pfTypeImets_sumEt->at(0);
  }
  
  if(met_sumEt>0){ met_over_sumEt=met_et/(met_sumEt+met_et);}
  
  //  cout<<"I get here 0"<<endl;
  
  
  //----------------------------------------------------------
  //Calculations for muon identification and acceptance
  //----------------------------------------------------------
  
  //    bool pass_pv_requirement = false;
  bool pass_pv_requirement = false;
  
  
  double pvx= -999.;
  double pvy= -999.;
  double pvz= -999.;
  double pvz_best= -999.;
  double pvrho = -999.;
  //    double pvnumtracks= -999.;
  double pvndof= -999.;
  double pvisFake= -999.;
  
  //  cout<<"I get here 1.01"<<endl;          
  
  int num_good_pv = 0;

  for(int ai = 0;ai<pv_x->size();ai++){
    //      if(pv_x->size()>0){                                                                                                                                                          
    pvx= pv_x->at(ai);
    pvy= pv_y->at(ai);
    pvz= pv_z->at(ai);
    pvrho = sqrt(pvx*pvx + pvy*pvy);
    //    pvnumtracks=pv_tracksSize->at(0);                                                                                                                                              
    pvndof=pv_ndof->at(ai);
    pvisFake=pv_isFake->at(ai);
    if(pvisFake<1&&fabs(pvz)<=24&&pvndof>4&&pvrho<=2){if(ai==0){pass_pv_requirement=true;}
      if(num_good_pv==0){ pvz_best = pv_z->at(ai);}
      num_good_pv++;
    }
    //	if(pvisFake<1&&fabs(pvz)<=24&&pvndof>4&&pvrho<=2){pass_pv_requirement=true;}
    //	if(fabs(pvz)<15&&pvndof>4&&pvrho<2){pass_pv_requirement=true;}
  }
  
  pass_pv_requirement = pass_pv_requirement && (hbhefilter_decision && scrapingVeto_decision && trackingfailurefilter_decision &&
						cschalofilter_decision && ecalTPfilter_decision && eebadscfilter_decision && 
						hcallaserfilter_decision);

  // hcallaserfilter_decision needs to be put back in...
  // eebadscfilter_decision needs to be put back in..

  //  cout<<"I get here 1.011"<<endl;          
  
  /*
    
  if(pv_x->size()>0){
  pvx= pv_x->at(0);
  pvy= pv_y->at(0);
  pvz= pv_z->at(0);
  pvrho = sqrt(pvx*pvx + pvy*pvy);
  //    pvnumtracks=pv_tracksSize->at(0);
  pvndof=pv_ndof->at(0);
  //	pvisFake=pv_isFake->at(0);
  }
  else{cout<<"primary vertex vector is empty"<<endl;}
  
  //if(pvisFake<1&&fabs(pvz)<24&&pvndof>4&&pvrho<2){pass_pv_requirement=true;}
  if(fabs(pvz)<15&&pvndof>4&&pvrho<2){pass_pv_requirement=true;}
  */
  //      if(HLT_Mu9>0&&pass_pv_requirement&&run<140400){
  //      if(HLT_Mu9>0&&pass_pv_requirement&&run>135058&&run<140400){
  //      if(HLT_Mu9>0&&pass_pv_requirement&&run>135058){

  // monster event stuff comes a bit later.  right now, I don't know how v51 works with this.  
  
  //      cout<<"The run number is: "<<run<<endl;
  bool have_Mu40_PFHT350 = false;
  bool have_Mu40_PFNoPUHT350 = false;
  
  bool have_PFHT350_Mu15_PFMET45 = false;
  bool have_PFHT400_Mu5_PFMET45 = false;
  bool have_PFNoPUHT350_Mu15_PFMET45 = false;
  bool have_PFNoPUHT400_Mu5_PFMET45 = false;

  bool have_CleanPFHT300_Ele40_CaloIdVT_TrkIdT = false;
  bool have_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT = false;
  bool have_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = false;
  bool have_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = false;
  bool have_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = false;

  bool have_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = false;
  
  bool pass_Mu40_PFHT350 = false;
  bool pass_Mu40_PFNoPUHT350 = false;
  
  bool pass_PFHT350_Mu15_PFMET45 = false;
  bool pass_PFHT400_Mu5_PFMET45 = false;
  bool pass_PFNoPUHT350_Mu15_PFMET45 = false;
  bool pass_PFNoPUHT400_Mu5_PFMET45 = false;

  bool pass_CleanPFHT300_Ele40_CaloIdVT_TrkIdT = false;
  bool pass_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT = false;
  bool pass_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = false;
  bool pass_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = false;
  bool pass_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = false;

  bool pass_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = false;

  bool pass_Mu40_ref = false;

  bool pass_Ele80_1_ref = false;
  bool pass_Ele80_2_ref = false;
  bool pass_Ele27_WP80_ref = false;
  
  bool pass_a_Ele_Ref = false;

  // Lepton trigger emergency test
  bool have_IsoMu24 = false;
  bool have_unPrescaled_IsoMu24 = false;
  bool pass_IsoMu24 = false;

  int L1size = L1trigger_name->size();
  bool have_HTT150 = false;
  bool pass_HTT150 = false;
  bool have_HTT175 = false;
  bool pass_HTT175 = false;
  int size = trigger_decision->size();  
  //      cout<<"Size of trigger names is: "<<size<<endl;                                                                                                                              
  //  cout<<"I get here 1.012"<<endl;          


  for(int iSuck = 0; iSuck < L1size; iSuck++) {
    if (L1trigger_name->at(iSuck) == "L1_HTT150") {
      if (L1trigger_prescalevalue->at(iSuck) == 1) have_HTT150 = true;
      if (L1trigger_decision->at(iSuck) == 1) pass_HTT150 = true;
    }
    if (L1trigger_name->at(iSuck) == "L1_HTT175") {
      if (L1trigger_prescalevalue->at(iSuck) == 1) have_HTT175 = true;
      if (L1trigger_decision->at(iSuck) == 1) pass_HTT175 = true;
    }    
  }
  for(int iu = 0;iu<size;iu++){ // Make sure we have our triggers
    
    //    cout << "we can do an empty check without bleeping the dog, right? " << triggerobject_pt->at(iu).empty() << endl;
    TString trigname = trigger_name->at(iu);
    
    if (trigname.BeginsWith("HLT_IsoMu24_eta2p1_v")) {
      have_IsoMu24 = true;
      if (trigger_prescalevalue->at(iu) == 1) have_unPrescaled_IsoMu24 = true;
      if (trigger_decision->at(iu) == 1) pass_IsoMu24 = true;
    }
    if (trigname.BeginsWith("HLT_Mu40_PFHT350_v")) {
      have_Mu40_PFHT350 = true;
      if (trigger_decision->at(iu) == 1) pass_Mu40_PFHT350 = true;
    }
    if (trigname.BeginsWith("HLT_Mu40_PFNoPUHT350_v")) {
      have_Mu40_PFNoPUHT350 = true;
      if (trigger_decision->at(iu) == 1) pass_Mu40_PFNoPUHT350 = true;
    }
    if (trigname.BeginsWith("HLT_PFHT350_Mu15_PFMET45_v")) {
      have_PFHT350_Mu15_PFMET45 = true;
      if (trigger_decision->at(iu) == 1) pass_PFHT350_Mu15_PFMET45 = true;
    }
    if (trigname.BeginsWith("HLT_PFHT400_Mu5_PFMET45_v")) {
      have_PFHT400_Mu5_PFMET45 = true;
      if (trigger_decision->at(iu) == 1) pass_PFHT400_Mu5_PFMET45 = true;
    }
    if (trigname.BeginsWith("HLT_PFNoPUHT350_Mu15_PFMET45_v")) {
      have_PFNoPUHT350_Mu15_PFMET45 = true;
      if (trigger_decision->at(iu) == 1) pass_PFNoPUHT350_Mu15_PFMET45 = true;
    }
    if (trigname.BeginsWith("HLT_PFNoPUHT400_Mu5_PFMET45_v")) {
      have_PFNoPUHT400_Mu5_PFMET45 = true;
      if (trigger_decision->at(iu) == 1) pass_PFNoPUHT400_Mu5_PFMET45 = true;
    }
    if ((trigname.BeginsWith("HLT_Mu40_v") || trigname.BeginsWith("HLT_Mu40_eta2p1_v")) && trigger_decision->at(iu) == 1) {
      pass_Mu40_ref = true;
    }
    if (trigname.BeginsWith("HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v")) {
      have_CleanPFHT300_Ele40_CaloIdVT_TrkIdT=true;
      if (trigger_decision->at(iu) == 1) pass_CleanPFHT300_Ele40_CaloIdVT_TrkIdT=true;
    }
    if (trigname.BeginsWith("HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_v")) {
      have_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT=true;
      if (trigger_decision->at(iu) == 1) pass_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT=true;
    }
    if (trigname.BeginsWith("HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v")) {
      have_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45=true;
      if (trigger_decision->at(iu) == 1) pass_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45=true;
    }
    if (trigname.BeginsWith("HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v")) {
      have_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45=true;
      if (trigger_decision->at(iu) == 1) pass_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45=true;
    }
    if (trigname.BeginsWith("HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v")) {
      have_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45=true;
      if (trigger_decision->at(iu) == 1) pass_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45=true;
    }
    if (trigname.BeginsWith("HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v")) {
      have_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = true;
      if (trigger_decision->at(iu) == 1) pass_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 = true;
    }
    if (trigname.BeginsWith("HLT_Ele80_CaloIdVT_TrkIdT_v") && trigger_decision->at(iu) == 1){
      pass_Ele80_1_ref = true;
    }
    if (trigname.BeginsWith("HLT_Ele80_CaloIdVT_GsfTrkIdT_v") && trigger_decision->at(iu) == 1){
      pass_Ele80_2_ref = true;
    }
    if (trigname.BeginsWith("HLT_Ele27_WP80_v") && trigger_decision->at(iu) == 1) {
      pass_Ele27_WP80_ref = true;
    }
  }


  if (!have_IsoMu24) cout << "missing isomu 24" << endl;
  if (have_IsoMu24 && !have_unPrescaled_IsoMu24) cout << "missing unprescaled isomu 24" << endl;

  if (have_Mu40_PFHT350 == false && have_Mu40_PFNoPUHT350 == false && 
      have_CleanPFHT300_Ele40_CaloIdVT_TrkIdT == false && 
      have_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT == false && have_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 == false && 
      have_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 == false && have_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45 == false) {
    cout << "missing a signal trigger ! " << endl;
  }

  pass_a_Ele_Ref = pass_Ele80_1_ref || pass_Ele80_2_ref || pass_Ele27_WP80_ref;

  //  cout<<"I get here 1.013"<<endl;          
  if(pass_pv_requirement){ // remove hbhefilter_decision for fastsim, trigger for Mu||El
    
    vector<int> good_muons_jet_cleaning;
    vector<int> veto_muons_jet_cleaning;
    vector<int> good_elecs_jet_cleaning;
    vector<int> veto_elecs_jet_cleaning; 
    
    bool eventVeto = false;
    
    for( uint cit = 0; cit<mus_pt->size(); cit++ ) {
      if( passedMuonSelection (cit) ) {
	eventVeto |= ! passedMuonCleaning(cit);
	
	good_muons_jet_cleaning.push_back(cit);
      }
	 
      if( passedMuonVetoSelection(cit) ) { 
	veto_muons_jet_cleaning.push_back(cit); 
      }           
    }
    //   cout<<"I get here 1.02"<<endl;             
    
    for(uint cit = 0;cit<els_et->size();cit++) {
      
      //if(true||int(runNumber_) == 1 && int(evtNumber_) == 10410670 ) cout<<"elecPt: "<<els_pt->at(cit)<<endl;
      
      if( passedElectronSelection(cit) ) {
	good_elecs_jet_cleaning.push_back(cit);
      }
      
      if ( passedElectronVetoSelection(cit) ) {
	veto_elecs_jet_cleaning.push_back(cit);
      }	 
    }    
    
    //----------------------------------------------------------
    //Calculations for V+jets and RA4 second lepton veto
    //----------------------------------------------------------
    
    //   cout<<"I get here 1.03"<<endl;      
   
    //----------------------------------------------------------
    //Compute number of jets before jet cuts
    //----------------------------------------------------------
    
    double htPF    = 0;
    double pxMHtPF = 0;
    double pyMHtPF = 0; 
    float leadJetPt = -1;
    
    vector<int> good_jets;

    for(uint it = 0; it<jets_AK5PFclean_pt->size(); it++) {
      
      if( ! passedPFJetSelection(it)  ) continue;
      
      bool isElectron = false;
      
      for(uint cit = 0; cit < good_elecs_jet_cleaning.size(); cit++) {
	double tmpdR = dR( jets_AK5PFclean_eta->at(it),
			   jets_AK5PFclean_phi->at(it),
			   els_eta->at(good_elecs_jet_cleaning[cit]),
			   els_phi->at(good_elecs_jet_cleaning[cit]));
	
	if( tmpdR < 0.3 ) {  isElectron = true; }
      }
      
      bool isMuon = false;
      
      for(uint cit = 0; cit < good_muons_jet_cleaning.size();cit++) {
	double tmpdR = dR( jets_AK5PFclean_eta->at(it),
			   jets_AK5PFclean_phi->at(it),
			   mus_eta->at(good_muons_jet_cleaning[cit]),
			   mus_phi->at(good_muons_jet_cleaning[cit]));
	
	if( tmpdR < 0.1 ) { isMuon = true; }
      }
      
      if( ! isMuon && ! isElectron ) {	    
	if(  jets_AK5PFclean_pt->at(it) > JetPTThresholdHT ) {
	  htPF    += jets_AK5PFclean_pt->at(it);
	  pxMHtPF -= jets_AK5PFclean_px->at(it);
	  pyMHtPF -= jets_AK5PFclean_py->at(it);
	}
	
	if(  jets_AK5PFclean_pt->at(it)> JetPTThresholdNJ ) {
	  good_jets.push_back(it);
	  
	  if( leadJetPt < jets_AK5PFclean_pt->at(it) ) leadJetPt = jets_AK5PFclean_pt->at(it);
	  
	}
      }	 
    }	    
    
    //cout<<4<<endl;
      
    vector<int> signal_muons;
    vector<int>   veto_muons;
    
    for(uint cit = 0; cit < good_muons_jet_cleaning.size(); cit++) {	    
      bool close_to_jet = false;
      
      for(uint iit = 0; iit < good_jets.size(); iit++) {
	double tmpdR = dR( jets_AK5PFclean_eta->at(good_jets[iit]),
			   jets_AK5PFclean_phi->at(good_jets[iit]),
			   mus_eta->at(good_muons_jet_cleaning[cit]),
			   mus_phi->at(good_muons_jet_cleaning[cit]));
	
	if( tmpdR < 0.3 ) {close_to_jet = true;}
      }
      
      if( !close_to_jet ) signal_muons.push_back(good_muons_jet_cleaning.at(cit));
    }
    //do the same for veto muons
    for(uint cit = 0; cit < veto_muons_jet_cleaning.size(); cit++) {	    
      bool close_to_jet = false;
      
      for(uint iit = 0; iit < good_jets.size(); iit++) {
	double tmpdR = dR( jets_AK5PFclean_eta->at(good_jets[iit]),
			   jets_AK5PFclean_phi->at(good_jets[iit]),
			   mus_eta->at(veto_muons_jet_cleaning[cit]),
			   mus_phi->at(veto_muons_jet_cleaning[cit]));
	
	if( tmpdR < 0.3 ) {close_to_jet = true;}
      }
      
      if( !close_to_jet ) veto_muons.push_back(veto_muons_jet_cleaning[cit]);
    }
    
    vector<int> signal_elecs;
    vector<int>   veto_elecs;
    
    for(int ielec = 0; ielec < good_elecs_jet_cleaning.size(); ielec++) {	 
      bool isCloseToJet = false;      
      if( !isCloseToJet ) signal_elecs.push_back(good_elecs_jet_cleaning[ielec]);
    }
    
      //same for veto electrons
    for(int ielec = 0; ielec < veto_elecs_jet_cleaning.size(); ielec++) {	 
      bool isCloseToJet = false;      
      if( !isCloseToJet ) veto_elecs.push_back(veto_elecs_jet_cleaning.at(ielec));
    }      
    
    double lep_pt = 0.0;
    if (signal_muons.size() == 1 && signal_elecs.size() == 0) lep_pt = mus_pt->at(signal_muons.at(0));
    if (signal_muons.size() == 0 && signal_elecs.size() == 1) lep_pt = els_pt->at(signal_elecs.at(0));


    if (( signal_muons.size() == 0 && veto_muons.size() == 0 && signal_elecs.size() == 1 && veto_elecs.size() == 1) || 
	( signal_muons.size() == 1 && veto_muons.size() == 1 && signal_elecs.size() == 0 && veto_elecs.size() == 0) && 
	good_jets.size() >= 3) {

      if (signal_muons.size() == 1 && (pass_PFHT400_Mu5_PFMET45 || pass_PFHT350_Mu15_PFMET45) && 
	  have_unPrescaled_IsoMu24 && htPF > 450 &&  met_et > 150) { // select for muons only.
	IsoMu24_pT_denom->Fill(mus_pt->at(signal_muons.at(0)));
	if (pass_IsoMu24) IsoMu24_pT_num->Fill(mus_pt->at(signal_muons.at(0)));
      }

      if (pass_Mu40_ref) {
	if ( have_Mu40_PFHT350) {	  
	  Mu40_PFHT350_HT_denom->Fill(htPF);
	  if (pass_Mu40_PFHT350) Mu40_PFHT350_HT_num->Fill(htPF);
	}
	if ( have_Mu40_PFNoPUHT350) {
	  Mu40_PFNoPUHT350_HT_denom->Fill(htPF);
	  if (pass_Mu40_PFNoPUHT350) Mu40_PFNoPUHT350_HT_num->Fill(htPF);
	}	
	if ( have_PFHT350_Mu15_PFMET45) {
	  PFHT350_Mu15_PFMET45_HT_MET_denom->Fill(htPF,met_et);
	  if (htPF > 450) PFHT350_Mu15_PFMET45_MET_denom->Fill(met_et);	
	  if (pass_PFHT350_Mu15_PFMET45) {
	    PFHT350_Mu15_PFMET45_HT_MET_num->Fill(htPF,met_et);      
	    if (htPF > 450) PFHT350_Mu15_PFMET45_MET_num->Fill(met_et);
	  }
	}
	if ( have_PFHT400_Mu5_PFMET45) {
	  PFHT400_Mu5_PFMET45_HT_MET_denom->Fill(htPF,met_et);
	  if (htPF > 475) PFHT400_Mu5_PFMET45_MET_denom->Fill(met_et); // htPF in both cases to be determined by HT turn-on curve either from above plots or 2-D maps
	  if (pass_PFHT400_Mu5_PFMET45) {
	    PFHT400_Mu5_PFMET45_HT_MET_num->Fill(htPF,met_et);
	    if (htPF > 475) PFHT400_Mu5_PFMET45_MET_num->Fill(met_et);
	  }
	}
	if ( have_PFNoPUHT350_Mu15_PFMET45) {
	  PFNoPUHT350_Mu15_PFMET45_HT_MET_denom->Fill(htPF,met_et);
	  if (htPF > 450) PFNoPUHT350_Mu15_PFMET45_MET_denom->Fill(met_et);
	  if (pass_PFNoPUHT350_Mu15_PFMET45) {
	    if (htPF > 450) PFNoPUHT350_Mu15_PFMET45_MET_num->Fill(met_et);
	    PFNoPUHT350_Mu15_PFMET45_HT_MET_num->Fill(htPF,met_et);
	  }
	}
	if ( have_PFNoPUHT400_Mu5_PFMET45) {
	  PFNoPUHT400_Mu5_PFMET45_HT_MET_denom->Fill(htPF,met_et);
	  if (htPF > 475) PFNoPUHT400_Mu5_PFMET45_MET_denom->Fill(met_et);
	  if (pass_PFNoPUHT400_Mu5_PFMET45) {
	    if (htPF > 475) PFNoPUHT400_Mu5_PFMET45_MET_num->Fill(met_et);
	    PFNoPUHT400_Mu5_PFMET45_HT_MET_num->Fill(htPF,met_et);
	  }
	}
      }
      
      if (pass_Ele80_1_ref || pass_Ele80_2_ref) {
	if (have_CleanPFHT300_Ele40_CaloIdVT_TrkIdT) {
	  CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_denom->Fill(htPF);
	  if (pass_CleanPFHT300_Ele40_CaloIdVT_TrkIdT) {
	    CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_num->Fill(htPF);
	  }
	}
	if (have_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT) {
	  CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_denom->Fill(htPF);
	  if (pass_CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT) {
	    if (htPF > 450) npass_2chan++;
	    CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_num->Fill(htPF);	  
	  }
	  //	  else if (htPF > 450) nfail_2chan++;
	  else HT_dist_fail_Ele_HT->Fill(htPF);
	}	
      }
      
      if (pass_Ele27_WP80_ref) {

	if (have_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45) {	  
	  CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom->Fill(htPF,met_et);
	  if (htPF > 450) CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom->Fill(met_et);
	  if (pass_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45) {
	    if (htPF > 450) CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num->Fill(met_et);	      
	    CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num->Fill(htPF,met_et);
	  }
	}	
	if (have_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45) {	  
	  CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom->Fill(htPF,met_et);
	  if (htPF > 475) CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom->Fill(met_et);
	  if (pass_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45) {
	    if (htPF > 475) CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num->Fill(met_et);	      
	    CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num->Fill(htPF,met_et);
	  }
	}
	if (have_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45) {	  
	  CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom->Fill(htPF,met_et);
	  if (htPF > 450) CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom->Fill(met_et);
	  if (pass_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45) {	    
	    if (htPF > 450) CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num->Fill(met_et);  
	    if (htPF > 450 && met_et > 150) npass_3chan++;
	    CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num->Fill(htPF,met_et);
	  }
	  else if (htPF > 450 && met_et > 150) {bleeper << "run, lumi, event,  HT, MET = " << run << " " << lumiblock << " " << event << " " << htPF << " " << met_et << endl; nfail_3chan++;}
	}	
	if (have_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45) {	  
	  CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom->Fill(htPF,met_et);
	  if (htPF > 475) CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom->Fill(met_et);
	  if (pass_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45) {
	    if (htPF > 475) CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num->Fill(met_et);
	    CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num->Fill(htPF,met_et);
	  }
	}
      }
    }
  }//require pass pv
  
  }//end over loop over all the events
  
  cout << "nUntriggered 3chan = " << nfail_3chan << endl;
  cout << "nTriggered 3chan = " << npass_3chan << endl;
  
  cout << "nUntriggered 2chan = " << nfail_2chan << endl;
  cout << "nTriggered 2chan = " << npass_2chan << endl;

  cout << "maxRun = " << maxRun << endl;

  divide_histos_and_errors(IsoMu24_pT_num,IsoMu24_pT_denom,IsoMu24_pT_eff);

  divide_histos_and_errors(Mu40_PFHT350_HT_num,Mu40_PFHT350_HT_denom,Mu40_PFHT350_HT_eff);
  divide_histos_and_errors(Mu40_PFNoPUHT350_HT_num,Mu40_PFNoPUHT350_HT_denom,Mu40_PFNoPUHT350_HT_eff);

  divide_histos_and_errors(PFHT350_Mu15_PFMET45_MET_num,PFHT350_Mu15_PFMET45_MET_denom,PFHT350_Mu15_PFMET45_MET_eff);
  divide_histos_and_errors(PFHT400_Mu5_PFMET45_MET_num,PFHT400_Mu5_PFMET45_MET_denom,PFHT400_Mu5_PFMET45_MET_eff);
  divide_histos_and_errors(PFNoPUHT350_Mu15_PFMET45_MET_num,PFNoPUHT350_Mu15_PFMET45_MET_denom,PFNoPUHT350_Mu15_PFMET45_MET_eff); 
  divide_histos_and_errors(PFNoPUHT400_Mu5_PFMET45_MET_num,PFNoPUHT400_Mu5_PFMET45_MET_denom,PFNoPUHT400_Mu5_PFMET45_MET_eff); 

  divide_TH2_histos_and_errors(PFHT350_Mu15_PFMET45_HT_MET_num,PFHT350_Mu15_PFMET45_HT_MET_denom,PFHT350_Mu15_PFMET45_HT_MET_eff);
  divide_TH2_histos_and_errors(PFHT400_Mu5_PFMET45_HT_MET_num,PFHT400_Mu5_PFMET45_HT_MET_denom,PFHT400_Mu5_PFMET45_HT_MET_eff);
  divide_TH2_histos_and_errors(PFNoPUHT350_Mu15_PFMET45_HT_MET_num,PFNoPUHT350_Mu15_PFMET45_HT_MET_denom,PFNoPUHT350_Mu15_PFMET45_HT_MET_eff);
  divide_TH2_histos_and_errors(PFNoPUHT400_Mu5_PFMET45_HT_MET_num,PFNoPUHT400_Mu5_PFMET45_HT_MET_denom,PFNoPUHT400_Mu5_PFMET45_HT_MET_eff);
  
  divide_histos_and_errors(CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_num,CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_denom,CleanPFHT300_Ele40_CaloIdVT_TrkIdT_HT_eff);
  divide_histos_and_errors(CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_num,CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_denom,CleanPFNoPUHT300_Ele40_CaloIdVT_TrkIdT_HT_eff);

  divide_histos_and_errors(CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num,CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom,CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff);
  divide_histos_and_errors(CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num,CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom,CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff);
  divide_histos_and_errors(CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num,CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom,CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff);
  divide_histos_and_errors(CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_num,CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_denom,CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_MET_eff);
  
  divide_TH2_histos_and_errors(CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num,CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom,CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff);
  divide_TH2_histos_and_errors(CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num,CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom,CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff);
  divide_TH2_histos_and_errors(CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num,CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom,CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff);
  divide_TH2_histos_and_errors(CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_num,CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_denom,CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_HT_MET_eff);

  test->Write();
  test->Close();
  
}
