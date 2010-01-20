import FWCore.ParameterSet.Config as cms
from Configuration.EventContent.EventContent_cff import *

singleMuPt20OutputModule = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring("singleMuPt20SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
      ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('EXOMu'), #name a name you like.
        dataTier = cms.untracked.string('EXOGroup')
    ),
    fileName = cms.untracked.string('muonPt20Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory. 
  )

singleMuPt15OutputModule = cms.OutputModule("PoolOutputModule",
                                            outputCommands = cms.untracked.vstring(),
                                            SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("singleMuPt15SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                            dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('EXOMu'), #name a name you like.
    dataTier = cms.untracked.string('EXOGroup')
    ),
                                            fileName = cms.untracked.string('muonPt15Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory.
                                            )

singleMuPt10OutputModule = cms.OutputModule("PoolOutputModule",
                                            outputCommands = cms.untracked.vstring(),
                                            SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("singleMuPt10SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                            dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('EXOMu'), #name a name you like.
    dataTier = cms.untracked.string('EXOGroup')
    ),
                                            fileName = cms.untracked.string('muonPt10Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory.
                                            )

singleMuPt5OutputModule = cms.OutputModule("PoolOutputModule",
                                           outputCommands = cms.untracked.vstring(),
                                           SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("singleMuPt5SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                           dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('EXOMu'), #name a name you like.
    dataTier = cms.untracked.string('EXOGroup')
    ),
                                           fileName = cms.untracked.string('muonPt05Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory.
                                           )

#default output contentFEVTHLTALLEventContent
singleMuPt20OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
singleMuPt15OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
singleMuPt10OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
singleMuPt5OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)

#add specific content you need. 
#SpecifiedEvenetContent=cms.PSet(
#    outputCommands = cms.untracked.vstring(
#      "keep *_singleHLTMuonFilter_*_*",
#	  "keep *_singleRecoMuonFilter_*_*",
#      )
#    )
#singleMuPt20OutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)
#singleMuPt15OutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)
#singleMuPt10OutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)
#singleMuPt5OutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)


