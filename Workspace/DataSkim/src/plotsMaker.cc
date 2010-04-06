// -*- C++ -*-
//
// Package:    MyTrigAna
// Class:      MyTrigAna
// 
/**\class MyTrigAna MyTrigAna.cc HLTrigger/MyTrigAna/src/MyTrigAna.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Emmanuelle Perez
//         Created:  Wed Dec  9 10:21:40 CET 2009
// $Id: plotsMaker.cc,v 1.1 2010/03/29 21:06:52 tdaniels Exp $
//
//


// system include files
#include <memory>
#include <map>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Framework/interface/TriggerNames.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetup.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetupFwd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "CondFormats/L1TObjects/interface/L1GtTriggerMenuFwd.h"
#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMapRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMap.h"

#include <iostream>
#include <fstream>


#include "TFile.h"
#include "TH1.h"
#include "TH2.h"

using namespace edm;
using namespace std;



//
// class decleration
//

class plotsMaker : public edm::EDAnalyzer {
   public:
      explicit plotsMaker(const edm::ParameterSet&);
      ~plotsMaker();


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      void MakeL1Histo(const edm::Event& iEvent, const edm::EventSetup& iSetup);


      // ----------member data ---------------------------

        std::string fOutputFileName ;
        TFile*      hOutputFile ;
	edm::InputTag ObjectMap_ ;
	edm::InputTag GtDigis_ ;
        int defineBX_;


	int npass_ ;
	bool first_ ;

	// -- L1 physics algorithms:
	TH2F* Timing_L1A_1;
        TH2F* Timing_L1A_2;
        TH2F* Timing_L1A_3;
        TH2F* Timing_L1A_4;

	// -- L1 technical bits:
	TH2F* Timing_L1T_1;
	TH2F* Timing_L1T_2;


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
plotsMaker::plotsMaker(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

        fOutputFileName = iConfig.getUntrackedParameter<string>("HistOutFile");

	ObjectMap_ = iConfig.getParameter<edm::InputTag>("ObjectMap");
	GtDigis_   = iConfig.getParameter<edm::InputTag>("GtDigis");
   
        defineBX_ = iConfig.getUntrackedParameter < int > ("defineBX", -1);


}


plotsMaker::~plotsMaker()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to for each event  ------------
void
plotsMaker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{


// -- Here code some selection:
  int ibx = iEvent.eventAuxiliary().bunchCrossing();
  if (defineBX_ != -1 && defineBX_ !=ibx ) return;

  npass_ ++ ;




  if (first_) {
    
    //Get the names of the L1 paths
    //for the moment the names are not included in L1GlobalTriggerReadoutRecord
    //we need to use L1GlobalTriggerObjectMapRecord
    edm::Handle<L1GlobalTriggerObjectMapRecord> gtObjectMapRecord;
    //    iEvent.getByLabel("hltL1GtObjectMap", gtObjectMapRecord);
    iEvent.getByLabel(ObjectMap_ , gtObjectMapRecord);
    const std::vector<L1GlobalTriggerObjectMap>& objMapVec =
      gtObjectMapRecord->gtObjectMap();
    
    for (std::vector<L1GlobalTriggerObjectMap>::const_iterator itMap = objMapVec.begin();
	 itMap != objMapVec.end(); ++itMap) {
      int algoBit = (*itMap).algoBitNumber();
      std::string algoNameStr = (*itMap).algoName();
      char* thename = (char*)(algoNameStr.c_str());
      
      if (algoBit < 32) Timing_L1A_1 -> GetYaxis() -> SetBinLabel(algoBit+1,thename);
      else if (algoBit < 64) Timing_L1A_2 -> GetYaxis() -> SetBinLabel(algoBit+1-32,thename);
      else if (algoBit < 96) Timing_L1A_3 -> GetYaxis() -> SetBinLabel(algoBit+1-64,thename);
      else if (algoBit < 128) Timing_L1A_4 -> GetYaxis() -> SetBinLabel(algoBit+1-96,thename);
      
    }
    
    edm::ESHandle<L1GtTriggerMenu> menuRcd;
    iSetup.get<L1GtTriggerMenuRcd>().get(menuRcd) ;
    const L1GtTriggerMenu* menu = menuRcd.product(); 
    std::cout << "How many bits are in this record?" << menu->gtTechnicalTriggerMap().size() << std::endl;
    for (CItAlgo techTrig = menu->gtTechnicalTriggerMap().begin(); techTrig != menu->gtTechnicalTriggerMap().end(); ++techTrig) {
      int techBit = (techTrig->second).algoBitNumber();
      std::cout << "counter = " << techBit << std::endl;
      std::string techNameStr = (techTrig->second).algoName();
      char* techName = (char*)(techNameStr.c_str());
      if (techBit < 32) Timing_L1T_1 -> GetYaxis() -> SetBinLabel(techBit +1, techName);
      else if (techBit < 64) Timing_L1T_2 -> GetYaxis() -> SetBinLabel(techBit+1-32, techName);
    }
    
    first_ = false;
    
  }
  
  
  
  
// -- Fill L1 histos
  MakeL1Histo(iEvent, iSetup);



}




// -----------------------------------------------------------------------------------------
void plotsMaker::MakeL1Histo(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
        edm::Handle<L1GlobalTriggerReadoutRecord> l1Handle;
        // iEvent.getByLabel("myGtDigis", l1Handle);
	iEvent.getByLabel(GtDigis_, l1Handle);

        // -- L1 algos :
        const DecisionWord dWord = l1Handle->decisionWord();

        // -- L1 technical bits:
        const TechnicalTriggerWord tWord = l1Handle->technicalTriggerWord();


	for (int ibx=-2; ibx <=2; ibx++) {

	 const TechnicalTriggerWord tWord = l1Handle->technicalTriggerWord(ibx);
	 for (int i=0; i < 64; i++) {
          bool ibit = tWord.at(i); 
	  if (ibit) {
            if (i < 32) Timing_L1T_1 -> Fill(ibx,i);
	    else Timing_L1T_2 -> Fill(ibx,i);
           }
	 }

	 const DecisionWord dWord = l1Handle->decisionWord(ibx);
	 for (int i=0; i< 128; i++) {
	  bool r=dWord.at(i);
	  if (r) { 
	   if (i < 32) Timing_L1A_1 -> Fill(ibx,i);
	   else if (i < 64) Timing_L1A_2 -> Fill(ibx,i);
           else if (i < 96) Timing_L1A_3 -> Fill(ibx,i);
           else if (i < 128) Timing_L1A_4 -> Fill(ibx,i);
	  }
	 }
	 
	}  // end loop on ibx


}



// --------------------------------------------------------------------------------------






// ------------ method called once each job just before starting event loop  ------------
void 
plotsMaker::beginJob()
{

   npass_ = 0;


   hOutputFile   = new TFile( fOutputFileName.c_str(), "RECREATE" ) ;

   first_ = true;

   Timing_L1A_1 = new TH2F("Timing_L1A_1","Timing_L1A_1",5,-2.5,2.5,32,-0.5,31.5);
   Timing_L1A_2 = new TH2F("Timing_L1A_2","Timing_L1A_2",5,-2.5,2.5,32,31.5,63.5);
   Timing_L1A_3 = new TH2F("Timing_L1A_3","Timing_L1A_3",5,-2.5,2.5,32,63.5,95.5);
   Timing_L1A_4 = new TH2F("Timing_L1A_4","Timing_L1A_4",5,-2.5,2.5,32,95.5,127.5);


   Timing_L1T_1 = new TH2F("Timing_L1T_1","Timing_L1T_1",5,-2.5,2.5,32,-0.5,31.5);
   Timing_L1T_2 = new TH2F("Timing_L1T_2","Timing_L1T_2",5,-2.5,2.5,32,31.5,63.5);

}


// ---------------------------------------------------------------------



// ------------ method called once each job just after ending the event loop  ------------
void 
plotsMaker::endJob() {

        hOutputFile->cd();


 std::cout << " Number of events passing the selection : " << npass_ << std::endl;

 // -- The timing histograms are normalized to the number of events which fullfill
 // -- the selection :

 int nbinsX = Timing_L1A_1->GetNbinsX();
 int nbinsY = Timing_L1A_1->GetNbinsY();

 for (int ix=1; ix <= nbinsX; ix ++) {
  for (int iy=1; iy <= nbinsY; iy ++) {
    Timing_L1A_1 -> SetBinContent(ix, iy, (Timing_L1A_1->GetBinContent(ix, iy)/npass_) );
    Timing_L1A_2 -> SetBinContent(ix, iy, (Timing_L1A_2->GetBinContent(ix, iy)/npass_) );
    Timing_L1A_3 -> SetBinContent(ix, iy, (Timing_L1A_3->GetBinContent(ix, iy)/npass_) );
    Timing_L1A_4 -> SetBinContent(ix, iy, (Timing_L1A_4->GetBinContent(ix, iy)/npass_) );

  }
 }

nbinsX = Timing_L1T_1 ->GetNbinsX();
nbinsY = Timing_L1T_2 ->GetNbinsY();
 for (int ix=1; ix <= nbinsX; ix ++) {
  for (int iy=1; iy <= nbinsY; iy ++) {
    Timing_L1T_1 -> SetBinContent(ix, iy, (Timing_L1T_1 ->GetBinContent(ix, iy)/npass_) );
    Timing_L1T_2 -> SetBinContent(ix, iy, (Timing_L1T_2 ->GetBinContent(ix, iy)/npass_) );
  }
 }



 Timing_L1A_1 -> Write();
 Timing_L1A_2 -> Write();
 Timing_L1A_3 -> Write();
 Timing_L1A_4 -> Write();

 Timing_L1T_1 -> Write();
 Timing_L1T_2 -> Write();

        hOutputFile->Write() ;
        hOutputFile->Close() ;

}

//define this as a plug-in
DEFINE_FWK_MODULE(plotsMaker);
