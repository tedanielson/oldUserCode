import FWCore.ParameterSet.Config as cms
from Configuration.EventContent.EventContent_cff import *


muonJPsiMMOutputModule = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring("muonJPsiMMSkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
      ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('muonJPsiMMSkim'), #name a name you like.
        dataTier = cms.untracked.string('TriggerTest')
    ),
    fileName = cms.untracked.string('muonJPsiMMSkim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory. 
                                          )


muonZMMOutputModule = cms.OutputModule("PoolOutputModule",
                                       outputCommands = cms.untracked.vstring(),
                                       SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("muonZMMSkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                       dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('muonZMMSkim'), #name a name you like.
    dataTier = cms.untracked.string('TriggerTest')
    ),
                                       fileName = cms.untracked.string('muonZMMSkim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory.
                                       )


#default output contentRECOSIMEventContent
muonJPsiMMOutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
muonZMMOutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
