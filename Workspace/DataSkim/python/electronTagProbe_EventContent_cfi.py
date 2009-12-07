import FWCore.ParameterSet.Config as cms
from Configuration.EventContent.EventContent_cff import *


electronZEEOutputModule = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring("electronZEESkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
      ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('electronZEESkim'), #name a name you like.
        dataTier = cms.untracked.string('TriggerTest')
    ),
    fileName = cms.untracked.string('electronZEESkim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory. 
  )


#default output contentFEVTHLTALLEventContent
electronZEEOutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)

#add specific content you need. 
#SpecifiedEvenetContent=cms.PSet(
#    outputCommands = cms.untracked.vstring(
#      "keep *_exoticaHLTElectronFilter_*_*",
#	  "keep *_exoticaRecoElectronFilter_*_*",
#      )
#    )
#SecondOutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)


