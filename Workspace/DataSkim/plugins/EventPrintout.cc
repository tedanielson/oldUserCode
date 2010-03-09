// -*- C++ -*-
//
// Package:    EventPrintout
// Class:      EventPrintout
// 
/**\class EventPrintout EventPrintout.cc Workspace/data_skim/plugins/EventPrintout.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  "Thomas Danielson"
//         Created:  Monday March 8 12:05:03 CDT 2010
//
//

#include <memory>

// user include files                                                                                                                                        
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

// basic things needed for running
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

// for trigger printout
#include "DataFormats/Common/interface/TriggerResults.h"

// Basic Data formats
// Muon:
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
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

class EventPrintout : public edm::EDAnalyzer {
public:
  explicit EventPrintout(const edm::ParameterSet&);
  ~EventPrintout();
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  FILE * outfile;
  edm::InputTag muonLabel;
  edm::InputTag electronLabel;
  edm::InputTag photonLabel;
  edm::InputTag jetLabel;

};

EventPrintout::EventPrintout(const edm::ParameterSet& iConfig)
{

  outfile = fopen("EventDump.txt","w");
  muonLabel = iConfig.getParameter<edm::InputTag>("muonLabel");
  electronLabel = iConfig.getParameter<edm::InputTag>("electronLabel");
  photonLabel = iConfig.getParameter<edm::InputTag>("photonLabel");
  jetLabel = iConfig.getParameter<edm::InputTag>("jetLabel");

}

EventPrintout::~EventPrintout()
{

}

void EventPrintout::beginJob() 
{

}

void EventPrintout::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  edm::Handle< reco::MuonCollection > muons;
  edm::Handle< reco::CaloJetCollection > jets;
  edm::Handle< reco::GsfElectronCollection> electrons;
  edm::Handle< reco::PhotonCollection> photons;

  iEvent.getByLabel(photonLabel,photons);
  iEvent.getByLabel(muonLabel,muons);
  iEvent.getByLabel(electronLabel,electrons);
  iEvent.getByLabel(jetLabel,jets); 

  int Run = iEvent.id().run();
  int Event = iEvent.id().event();
  int ls = iEvent.getLuminosityBlock().id().luminosityBlock();
  int bx = iEvent.bunchCrossing();
  fprintf(outfile,"Run %d, Event %d, Lumi %d, Bunch xing %d\n", Run, Event, ls, bx);

}

void EventPrintout::endJob()
{

  fclose(outfile);
  
}

DEFINE_FWK_MODULE(EventPrintout);
