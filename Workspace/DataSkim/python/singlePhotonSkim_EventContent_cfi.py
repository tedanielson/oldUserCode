import FWCore.ParameterSet.Config as cms
from Configuration.EventContent.EventContent_cff import *


singlePhotonPt20OutputModule = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring("singlePhotonPt20SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
      ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('Photon'), #name a name you like.
        dataTier = cms.untracked.string('TriggerTest')
    ),
    fileName = cms.untracked.string('photonPt20Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory. 
                                                )
singlePhotonPt15OutputModule = cms.OutputModule("PoolOutputModule",
                                                outputCommands = cms.untracked.vstring(),
                                                SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("singlePhotonPt15SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                                dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('Photon'), #name a name you like.
    dataTier = cms.untracked.string('TriggerTest')
    ),
                                                fileName = cms.untracked.string('photonPt15Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory.
                                                )
singlePhotonPt10OutputModule = cms.OutputModule("PoolOutputModule",
                                                outputCommands = cms.untracked.vstring(),
                                                SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("singlePhotonPt10SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                                dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('Photon'), #name a name you like.
    dataTier = cms.untracked.string('TriggerTest')
    ),
                                                fileName = cms.untracked.string('photonPt10Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory.
                                                )

singlePhotonPt5OutputModule = cms.OutputModule("PoolOutputModule",
                                                outputCommands = cms.untracked.vstring(),
                                                SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("singlePhotonPt5SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                                dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('Photon'), #name a name you like.
    dataTier = cms.untracked.string('TriggerTest')
    ),
                                                fileName = cms.untracked.string('photonPt5Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test\ directory.
                                                )


#default output contentFEVTHLTALLEventContent
singlePhotonPt20OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
singlePhotonPt15OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
singlePhotonPt10OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
singlePhotonPt5OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)

#add specific content you need. 
#SpecifiedEvenetContent=cms.PSet(
#    outputCommands = cms.untracked.vstring(
#      "keep *_exoticaHLTMuonFilter_*_*",
#	  "keep *_exoticaRecoMuonFilter_*_*",
#      )
#    )
#singlePhotonPt20OutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)



