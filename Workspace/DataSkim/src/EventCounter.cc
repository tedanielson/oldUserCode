// -*- C++ -*-
//
// Package:    EventCounter
// Class:      EventCounter
// 
/**\class EventCounter EventCounter.cc Workspace/EventCounter/src/EventCounter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Thomas Erik Danielson,,,
//         Created:  Thu May 20 09:58:29 CEST 2010
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//
// class declaration
//

class EventCounter : public edm::EDFilter {
   public:
      explicit EventCounter(const edm::ParameterSet&);
      ~EventCounter();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
  int maxEvents_;
  int counter;
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
EventCounter::EventCounter(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed  
  maxEvents_ = iConfig.getParameter < int > ("maxEvents");
  counter = 0;
}


EventCounter::~EventCounter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
EventCounter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  if (counter < maxEvents_) {
    counter++;
    return true;
  }
  return false;
}

// ------------ method called once each job just before starting event loop  ------------
void 
EventCounter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
EventCounter::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(EventCounter);
