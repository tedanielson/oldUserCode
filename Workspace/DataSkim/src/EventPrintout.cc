// -*- C++ -*-
//
// Package:    EventPrintout
// Class:      EventPrintout
// 
/**\class EventPrintout EventPrintout.cc Workspace/EventPrintout/src/EventPrintout.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Thomas Erik Danielson,40 1-A11,+41227671646,
//         Created:  Fri Mar 12 00:22:32 CET 2010
// $Id: EventPrintout.cc,v 1.3 2010/03/12 22:50:38 tdaniels Exp $
//
//


// system include files
#include <memory>
#include <string>
#include <cstdlib>
#include <utility>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Framework/interface/TriggerNames.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetup.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetupFwd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMapRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMap.h"

// Basic Data formats                                                                                                                                        
// Muon:                                                                                                                                                     
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
// Electron:                                                                                                                                                 
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronCore.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronCoreFwd.h"
// Photon:                                                                                                                                                   
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonCore.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/EgammaCandidates/interface/PhotonCoreFwd.h"
// Jet:                                                                                                                                                      
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"

using namespace edm;
using namespace std;


//
// class declaration
//

class EventPrintout : public edm::EDAnalyzer {
   public:
      explicit EventPrintout(const edm::ParameterSet&);
      ~EventPrintout();


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      // ----------member data ---------------------------

  FILE * outfile;
  edm::InputTag muonLabel;
  edm::InputTag electronLabel;
  edm::InputTag photonLabel;
  edm::InputTag jetLabel;
  edm::InputTag triggerResults_;

  edm::InputTag ObjectMap_ ;
  edm::InputTag GtDigis_ ;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
EventPrintout::EventPrintout(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

  outfile = fopen("EventDump.txt","w");
  muonLabel = iConfig.getParameter<edm::InputTag>("muonLabel");
  electronLabel = iConfig.getParameter<edm::InputTag>("electronLabel");
  photonLabel = iConfig.getParameter<edm::InputTag>("photonLabel");
  jetLabel = iConfig.getParameter<edm::InputTag>("jetLabel");
  triggerResults_ = iConfig.getParameter<edm::InputTag>("triggerResults_");

  ObjectMap_ = iConfig.getParameter<edm::InputTag>("ObjectMap");
  GtDigis_   = iConfig.getParameter<edm::InputTag>("GtDigis");

}


EventPrintout::~EventPrintout()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
EventPrintout::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  edm::Handle< reco::MuonCollection > muons;
  edm::Handle< reco::CaloJetCollection > jets;
  edm::Handle< reco::GsfElectronCollection> electrons;
  edm::Handle< reco::PhotonCollection> photons;
  edm::Handle< edm::TriggerResults> triggerResults;

  edm::Handle<L1GlobalTriggerReadoutRecord> l1Handle;
  iEvent.getByLabel(GtDigis_, l1Handle);

  iEvent.getByLabel(photonLabel,photons);
  iEvent.getByLabel(muonLabel,muons);
  iEvent.getByLabel(electronLabel,electrons);
  iEvent.getByLabel(jetLabel,jets);
  iEvent.getByLabel(triggerResults_,triggerResults);

  int Run = iEvent.id().run();
  int Event = iEvent.id().event();
  int ls = iEvent.getLuminosityBlock().id().luminosityBlock();
  int bx = iEvent.bunchCrossing();

  int nMuons = muons->size();
  int nJets = jets->size();
  int nElectrons = electrons->size();
  int nPhotons = photons->size();

  fprintf(outfile,"Run %d, Event %d, Lumi %d, Bunch xing %d\n", Run, Event, ls, bx);
  fprintf(outfile,"Number of muons, photons, jets, electrons: %d, %d, %d, %d\n", nMuons, nPhotons, nJets, nElectrons);

  //==============================MUONS========================                                                                                              

  if (nMuons > 0)  fprintf(outfile,"Muon information\n");
  for (int iMuon = 0; iMuon < nMuons; iMuon++) {
    reco::MuonRef refMu(muons,iMuon);
    double muonPt = refMu->pt(); double muonEta = refMu->eta(); double muonPhi = refMu->phi(); bool isGlobal = refMu->isGlobalMuon();
    int global = 0;
    if (isGlobal) {
      global = 1;
      const reco::TrackRef glbTrack = ( refMu->isGlobalMuon()) ?
        refMu->combinedMuon() : reco::TrackRef();
      if(glbTrack.isAvailable()) {
        const reco::TrackRef refTk(glbTrack);
        double muonD0 = refTk->d0();
        double muonNormChi2 = refTk->normalizedChi2();
        fprintf(outfile,"   pt, eta, phi, global, d0, norm Chi2: %f %f %f %d %f %f\n",muonPt,muonEta,muonPhi,global,muonD0,muonNormChi2);
      } // global available                                                                                                                                  
      else fprintf(outfile,"   pt, eta, phi, global, d0, norm Chi2: %f %f %f %d. Something wrong with glb trk\n",muonPt,muonEta,muonPhi,global);
    } // global?                                                                                                                                             
    else fprintf(outfile,"   pt, eta, phi, global: %f %f %f %d\n",muonPt,muonEta,muonPhi,global);
  } // Loop over muons                                                                                                                                       

    //============================PHOTONS=======================                                                                                             

  if (nPhotons > 0) fprintf(outfile,"Photon information\n");
  for (int iPhoton = 0; iPhoton < nPhotons; iPhoton++) {
    reco::PhotonRef refGam(photons,iPhoton);
    double photonPt = refGam->pt(); double photonEta = refGam->eta(); double photonPhi = refGam->phi(); double photonE5x5 = (double)refGam->e5x5();
    double photonHOverE = (double)refGam->hadronicOverEm();
    fprintf(outfile,"   pt, eta, phi, e5x5: %f %f %f %f %f\n",photonPt,photonEta,photonPhi,photonE5x5,photonHOverE);
  }

  //============================JETS=========================                                                                                                

  if (nJets > 0) fprintf(outfile,"Jet information\n");
  for (int iJet = 0; iJet < nJets; iJet++) {
    reco::CaloJetRef refJet(jets,iJet);
    double jetEt = refJet->et(); double jetEta = refJet->eta(); double jetPhi = refJet->phi(); double jetHadFrac = (double)refJet->energyFractionHadronic();
    fprintf(outfile,"   Et, eta, phi, energyFractionHadronic: %f %f %f %f\n",jetEt,jetEta,jetPhi,jetHadFrac);
  }

  //==========================ELECTRONS=====================                                                                                                 

  if (nElectrons > 0) fprintf(outfile,"Electron information\n");
  for (int iElec = 0; iElec < nElectrons; iElec++) {
    reco::GsfElectronRef refElec(electrons,iElec);
    double electronPt = refElec->pt(); double electronEta = refElec->eta(); double electronPhi = refElec->phi(); double electronE5x5 = (double)refElec->e5x5\
														   ();
    double electronHOverE = (double)refElec->hadronicOverEm();
    fprintf(outfile,"   Et, eta, phi, e5x5, hadronicOverEm: %f %f %f %f %f\n",electronPt,electronEta,electronPhi,electronE5x5,electronHOverE);
  }

  //=========================L1+L1TECH======================                                                                                                 

  fprintf(outfile,"Technical trigger information\n");

  const DecisionWord dWord = l1Handle->decisionWord();
  const TechnicalTriggerWord tWord = l1Handle->technicalTriggerWord();

  int techDecisionMap[5][64];;
  int l1DecisionMap[5][128];

  for (int ibx=-2; ibx <=2; ibx++) {
    TechnicalTriggerWord tWord = l1Handle->technicalTriggerWord(ibx);
    DecisionWord dWord = l1Handle->decisionWord(ibx);
     //======================TECHNICAL BITS================  
    for (int i=0; i < 64; i++) {
      bool ibit = tWord.at(i);
      int pass = 0;
      if (ibit) pass = 1;
      techDecisionMap[ibx+2][i] = pass;
    }
     //=====================L1 BITS========================
    for (int i=0; i < 128; i++) {
      bool r=dWord.at(i);
      int pass = 0;
      if (r) pass = 1;
      //      std::cout << "pass = " << pass <<std::endl;
      l1DecisionMap[ibx+2][i] = pass;
    }
  }
     //=======================L1 TECHNICAL PRINTOUT========
  fprintf(outfile,"bx:      -2 -1  0  1  2\n");
  for (int i = 0; i < 64; i++) {
    bool passone = false; // did a bit fire?
    for (int j = 0; j < 5; j++) {
      if (techDecisionMap[j][i] == 1) passone = true;
    }
    if (passone) {
      if (i < 10) fprintf(outfile,"bit %d : ",i);
      else fprintf(outfile,"bit %d: ",i);    
      for (int j = 0; j < 5; j++) {
	fprintf(outfile,"  %d",techDecisionMap[j][i]);
      }
      fprintf(outfile,"\n");
    }
  }

  fprintf(outfile,"L1 trigger information\n");

    //=====================GET L1 PATH NAMES==============

  edm::Handle<L1GlobalTriggerObjectMapRecord> gtObjectMapRecord;
  iEvent.getByLabel(ObjectMap_ , gtObjectMapRecord);
  const std::vector<L1GlobalTriggerObjectMap>& objMapVec =  gtObjectMapRecord->gtObjectMap();

  std::vector<std::string> *l1Names = new std::vector<std::string>;
  std::vector<int> *l1Bits = new std::vector<int>;

  for (std::vector<L1GlobalTriggerObjectMap>::const_iterator itMap = objMapVec.begin();
       itMap != objMapVec.end(); ++itMap) 
    {
      int algoBit = (*itMap).algoBitNumber();
      (*l1Bits).push_back(algoBit);
      std::string algoNameStr = (*itMap).algoName();
      (*l1Names).push_back(algoNameStr);
    }
  
  //  int namesLen = (int) (*l1Names).size();
  
  for (int i = 0; i < (*l1Names).size(); i++) {
    bool passone = false;
    for (int j = 0; j < 5; j++) {
      int index = (*l1Bits).at(i);
      if (l1DecisionMap[j][index] == 1) passone = true;
    }
    if (passone) {
      fprintf(outfile,"%s",(*l1Names).at(i).c_str());
      for (int j = 0; j < 5; j++) {
	int index = (*l1Bits).at(i);
	fprintf(outfile,"  %d",l1DecisionMap[j][index]);
      }
      fprintf(outfile,"\n");
    }
  }

  
  
  //==========================HLT===========================                                                                                                 
  
  edm::TriggerNames namesOfTriggers(*triggerResults);
  fprintf(outfile,"Trigger information: paths firing\n");
  for (unsigned int i = 0; i < triggerResults->size(); i++) {
    //    std::cout << namesOfTriggers.triggerName(i) << std::endl;                                                                                          
    std::string pathName = namesOfTriggers.triggerName(i);
    if (triggerResults->state(i) == 1) {
      fprintf(outfile,"   %s\n",pathName.c_str());
    }
  }
  fprintf(outfile,"\n"); // new line to separate events                                                                                                      
  
}


// ------------ method called once each job just before starting event loop  ------------
void 
EventPrintout::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
EventPrintout::endJob() {
  fclose(outfile);
}

//define this as a plug-in
DEFINE_FWK_MODULE(EventPrintout);
