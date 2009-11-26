import FWCore.ParameterSet.Config as cms
from Configuration.EventContent.EventContent_cff import *


singleMuOutputModule = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring("singleMuSkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
      ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('EXOMu'), #name a name you like.
        dataTier = cms.untracked.string('EXOGroup')
    ),
    fileName = cms.untracked.string('muonSkim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory. 
  )


#default output contentRECOSIMEventContent
singleMuOutputModule.outputCommands.extend(RECOSIMEventContent.outputCommands)

#add specific content you need. 
SpecifiedEvenetContent=cms.PSet(
    outputCommands = cms.untracked.vstring(
      "keep *_singleHLTMuonFilter_*_*",
	  "keep *_singleRecoMuonFilter_*_*",
      )
    )
singleMuOutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)



