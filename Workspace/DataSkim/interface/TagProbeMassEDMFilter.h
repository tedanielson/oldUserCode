#ifndef Workspace_DataSkim_TagProbeMassEDMFilter_h
#define Workspace_DataSkim_TagProbeMassEDMFilter_h
// -*- C++ -*-
//
// Package:     TagAndProbe
// Class  :     TagProbeMassEDMFilter
// 
/**\class TagProbeMassEDMFilter TagProbeMassEDMFilter.h PhysicsTools/TagAndProbe/interface/TagProbeMassEDMFilter.h

 Description: <one line class summary>

 Usage:
    <usage>

*/
//
// Original Author: Nadia Adam (Princeton) 
//         Created:  Fri Jun  6 09:13:10 CDT 2008
// $Id: TagProbeMassEDMFilter.h,v 1.3 2009/03/24 19:32:37 ahunt Exp $
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

class TagProbeMassEDMFilter : public edm::EDFilter 
{
   public:
      explicit TagProbeMassEDMFilter(const edm::ParameterSet&);
      ~TagProbeMassEDMFilter();

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      // ----------member data ---------------------------
      std::string tpMapName;

};
#endif
