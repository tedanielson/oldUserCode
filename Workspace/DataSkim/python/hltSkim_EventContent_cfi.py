import FWCore.ParameterSet.Config as cms
from Configuration.EventContent.EventContent_cff import *


hltOutputModule = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring("hltMu3SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
      ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('TpgHLTFilter'), #name a name you like.
        dataTier = cms.untracked.string('TriggerTest')
    ),
    fileName = cms.untracked.string('HLTSkim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory. 
  )



#default output contentFEVTHLTALLEventContent
hltOutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)

#add specific content you need. 
#SpecifiedEvenetContent=cms.PSet(
#    outputCommands = cms.untracked.vstring(
#      "keep *_exoticaHLTMuonFilter_*_*",
#	  "keep *_exoticaRecoMuonFilter_*_*",
#      )
#    )
#exoticaMuOutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)



