#ifndef SelectionCfaSynchMay10_h
#define SelectionCfaSynchMay10_h

#include "TMath.h"
#include "TLorentzVector.h"
#include "TRandom3.h"
#include "TMatrixD.h"
#include "TVectorD.h"
#include "Math/Point3D.h"
#include "Math/Vector3D.h"
#include "Math/Vector4D.h"
#include "Math/Rotation3D.h"
#include "Math/EulerAngles.h"
#include "Math/AxisAngle.h"
#include "Math/Quaternion.h"
#include "Math/RotationX.h"
#include "Math/RotationY.h"
#include "Math/RotationZ.h"
#include "Math/LorentzRotation.h"
#include "Math/Boost.h"
#include "Math/BoostX.h"
#include "Math/BoostY.h"
#include "Math/BoostZ.h"
#include "Math/Transform3D.h"
#include "Math/Plane3D.h"
#include "Math/VectorUtil.h"
#include "ObjectSelector.h"

using namespace ROOT::Math;

int bestPVIndex = 0;

const float MuonPTThreshold      =  20;
const float MuonVetoPTThreshold  =  15;

const float ElectronPTThreshold      =  20;
const float ElectronVetoPTThreshold  = 15;

const float LeptonPTThreshold        = 15;


bool hasGoodVtx()
{
   
   bool result = false;
   
   for(int ai = 0;ai<pv_x->size();ai++)
   {      
      result |=  
	 ( pv_isFake->at(ai)    <    1 && 
	   fabs( pv_z->at(ai) ) <=  24 && 
	   pv_ndof->at(ai)      >    4 && 
	   sqrt( pow(pv_x->at(ai),2)+pow(pv_y->at(ai),2) ) <= 2 ) ;
      
   }
   
   return result;
}

bool isFirstVertexGood()
{
   
   //for(int ai = 0;ai<pv_x->size();ai++)
   //{      
   // if( pv_isFake->at(ai) < 1 && 
   //  fabs( pv_z->at(ai) ) <= 24 && 
   //  pv_ndof->at(ai) > 4 && 
   //  sqrt( pow(pv_x->at(ai),2)+pow(pv_y->at(ai),2) ) <=2 )
   //  {
   // //this is a good vertex
   // }
   //}

   return ( pv_isFake->at(0) < 1 && 
	    fabs( pv_z->at(0) ) <= 24 && 
	    pv_ndof->at(0) > 4 && 
	    sqrt( pow( pv_x->at(0),2 ) + pow( pv_y->at(0),2 ) ) <= 2 );
}



bool isBeamGasEvent()
{
   
  /*
   double frac_highpurity=0;
   double num_highpurity=0;
   double num_NOThighpurity=0;
   
   int Ntracks = tracks_highPurity->size();
   
   for(uint att=0; att < tracks_highPurity->size(); att++)
   {
      if(tracks_highPurity->at(att)>0){num_highpurity++;}
      if(tracks_highPurity->at(att)<1){num_NOThighpurity++;}
   }
   
   frac_highpurity=num_highpurity/(num_highpurity+num_NOThighpurity);
   
   return !( Ntracks<11 || (Ntracks>10 && frac_highpurity>=0.25 ) );
  */
  return false;
}

bool passedMuonSelection(int cit)
{
   
  float d0PV, relIso;
  d0PV = mus_tk_d0dum->at(cit)-pv_x->at(0)*sin(mus_tk_phi->at(cit))+pv_y->at(0)*cos(mus_tk_phi->at(cit));
  double max = mus_pfIsolationR03_sumNeutralHadronEt->at(cit) + mus_pfIsolationR03_sumPhotonEt->at(cit) - 0.5*mus_pfIsolationR03_sumPUPt->at(cit);
  if(max<0.0) max=0.0;
  relIso = (mus_pfIsolationR03_sumChargedHadronPt->at(cit) + max)/mus_pt->at(cit);
  int pfIdx=-1;
  
  return (mus_isGlobalMuon->at(cit) > 0
	  && mus_isPFMuon->at(cit) > 0
	  && mus_id_GlobalMuonPromptTight->at(cit)> 0 
	  // included in GlobalMuonPromptTight
	  /*  	     && mus_tk_chi2->at(cit)/mus_tk_ndof->at(cit) < 10 */
	  /* 	     && mus_cm_numvalMuonhits->at(cit) > 0 */
	  && mus_tk_LayersWithMeasurement->at(cit) > 5
	  && mus_tk_numvalPixelhits->at(cit) > 0
	  && mus_numberOfMatchedStations->at(cit) > 1
	  && fabs(mus_dB->at(cit)) < 0.02
	  && fabs(getDZ(mus_tk_vx->at(cit), mus_tk_vy->at(cit), mus_tk_vz->at(cit), mus_tk_px->at(cit), mus_tk_py->at(cit), mus_tk_pz->at(cit), 0)) < 0.5
	  && mus_pt->at(cit) >= MuonPTThreshold
	  && fabs(mus_eta->at(cit)) <= 2.4
	  && relIso < 0.12
	  && hasPFMatch(cit, particleId::muon, pfIdx)); 
  
}


bool passedMuonVetoSelection(int cit)
{
  
  float d0PV, relIso;
  d0PV = mus_tk_d0dum->at(cit)-pv_x->at(0)*sin(mus_tk_phi->at(cit))+pv_y->at(0)*cos(mus_tk_phi->at(cit));
  double max = mus_pfIsolationR03_sumNeutralHadronEt->at(cit) + mus_pfIsolationR03_sumPhotonEt->at(cit) - 0.5*mus_pfIsolationR03_sumPUPt->at(cit);
  if(max<0.0) max=0.0;
  relIso = (mus_pfIsolationR03_sumChargedHadronPt->at(cit) + max)/mus_pt->at(cit);
  int pfIdx=-1;
  
  
  return ((mus_isGlobalMuon->at(cit) >0 || mus_isTrackerMuon->at(cit) >0)
	  && mus_isPFMuon->at(cit) > 0
	  && fabs(getDZ(mus_tk_vx->at(cit), mus_tk_vy->at(cit), mus_tk_vz->at(cit), mus_tk_px->at(cit), mus_tk_py->at(cit), mus_tk_pz->at(cit), 0)) < 0.5 
	  && mus_pt->at(cit) >= MuonVetoPTThreshold
	  && fabs(mus_eta->at(cit)) <= 2.5
	  && relIso < 0.2
	  && hasPFMatch(cit, particleId::muon, pfIdx)); 
     
}

bool passedElectronSelection(int cit )
{
  
  float d0PV = els_d0dum->at(cit)-pv_x->at(0)*sin(els_tk_phi->at(cit))
    +pv_y->at(0)*cos(els_tk_phi->at(cit));
  double max = els_PFphotonIsoR03->at(cit) + els_PFneutralHadronIsoR03->at(cit) - rho_kt6PFJetsForIsolation2011 * GetEffectiveArea(els_scEta->at(cit));
  if(max<0.0) max=0;
  double relIso = (els_PFchargedHadronIsoR03->at(cit) + max)/els_pt->at(cit);
  int pfIdx=-1;
  
  return (els_pt->at(cit) > ElectronPTThreshold
	  && fabs(els_scEta->at(cit)) < 2.5
	  && relIso < 0.15
	  && !els_hasMatchedConversion->at(cit)
	  && els_n_inner_layer->at(cit) <= 1
	  && fabs(getDZ(els_vx->at(cit), els_vy->at(cit), els_vz->at(cit), cos(els_tk_phi->at(cit))*els_tk_pt->at(cit), sin(els_tk_phi->at(cit))*els_tk_pt->at(cit), els_tk_pz->at(cit), 0)) < 0.1
	  && fabs(1./els_caloEnergy->at(cit) - els_eOverPIn->at(cit)/els_caloEnergy->at(cit)) < 0.05 
	  && hasPFMatch(cit, particleId::electron, pfIdx) 
	  && fabs(d0PV) < 0.02 
	  && ((els_isEB->at(cit)
	       && fabs(els_dEtaIn->at(cit)) < 0.004
	       && fabs(els_dPhiIn->at(cit)) < 0.06
	       && els_sigmaIEtaIEta->at(cit) < 0.01
	       && els_hadOverEm->at(cit) < 0.12 )
	      || (els_isEE->at(cit)
		  && fabs(els_dEtaIn->at(cit)) < 0.007
		  && fabs(els_dPhiIn->at(cit)) < 0.03
		  && els_sigmaIEtaIEta->at(cit) < 0.03
		  && els_hadOverEm->at(cit) < 0.10 ))
	  );
}

bool passedElectronVetoSelection(int cit )
{

  float d0PV = els_d0dum->at(cit)-pv_x->at(0)*sin(els_tk_phi->at(cit))
    +pv_y->at(0)*cos(els_tk_phi->at(cit));
  double max = els_PFphotonIsoR03->at(cit) + els_PFneutralHadronIsoR03->at(cit) - rho_kt6PFJetsForIsolation2011 * GetEffectiveArea(els_scEta->at(cit));
  if(max<0.0) max=0;
  double relIso = (els_PFchargedHadronIsoR03->at(cit) + max)/els_pt->at(cit);
  int pfIdx=-1;
  
  return (els_pt->at(cit) > ElectronVetoPTThreshold
	  && fabs(els_scEta->at(cit)) < 2.5
	  && relIso < 0.15
	  && fabs(getDZ(els_vx->at(cit), els_vy->at(cit), els_vz->at(cit), cos(els_tk_phi->at(cit))*els_tk_pt->at(cit), sin(els_tk_phi->at(cit))*els_tk_pt->at(cit), els_tk_pz->at(cit), 0)) < 0.2
	  && fabs(d0PV) < 0.04 
	  && ((els_isEB->at(cit)
	       && fabs(els_dEtaIn->at(cit)) < 0.007
	       && fabs(els_dPhiIn->at(cit)) < 0.8
	       && els_sigmaIEtaIEta->at(cit) < 0.01
	       && els_hadOverEm->at(cit) < 0.15)
	      || (els_isEE->at(cit)
		  && fabs(els_dEtaIn->at(cit)) < 0.01
		  && fabs(els_dPhiIn->at(cit)) < 0.7
		  && els_sigmaIEtaIEta->at(cit) < 0.03))
	  );
  
}


bool passedPFJetSelection(int it)
{

   double NEF = -999.;
   double CEF = -999.;
   double NHF=-999.;
   double CHF=-999.;
   double chgMult=-999.;
   double numConst=-999.;
   
   if( jets_AK5PFclean_energy->at(it) > 0 )
   {
      NEF = jets_AK5PFclean_neutralEmE->at(it)/jets_AK5PFclean_energy->at(it);
      CEF = jets_AK5PFclean_chgEmE->at(it)/jets_AK5PFclean_energy->at(it);
      NHF = jets_AK5PFclean_neutralHadE->at(it)/jets_AK5PFclean_energy->at(it);
      CHF = jets_AK5PFclean_chgHadE->at(it)/jets_AK5PFclean_energy->at(it);   
      chgMult  = jets_AK5PFclean_chg_Mult->at(it);
      numConst = 
	 jets_AK5PFclean_mu_Mult->at(it)+
	 jets_AK5PFclean_neutral_Mult->at(it)+
	 jets_AK5PFclean_chg_Mult->at(it);
   }
   
   return 
      ( fabs(jets_AK5PFclean_eta->at(it)) <= 2.4 &&
	jets_AK5PFclean_neutralEmE->at(it)/jets_AK5PFclean_energy->at(it) < 0.99 &&
	jets_AK5PFclean_chgEmE->at(it)/jets_AK5PFclean_energy->at(it) < 0.99 &&
	jets_AK5PFclean_neutralHadE->at(it)/jets_AK5PFclean_energy->at(it) < 0.99 &&
	jets_AK5PFclean_chgHadE->at(it)/jets_AK5PFclean_energy->at(it) > 0 &&
	jets_AK5PFclean_chg_Mult->at(it) > 0 &&
	jets_AK5PFclean_mu_Mult->at(it) + 
	jets_AK5PFclean_neutral_Mult->at(it) + 
	jets_AK5PFclean_chg_Mult->at(it) > 1 );
   
}

#endif
