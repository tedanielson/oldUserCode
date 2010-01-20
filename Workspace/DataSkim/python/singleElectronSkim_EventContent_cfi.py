import FWCore.ParameterSet.Config as cms
from Configuration.EventContent.EventContent_cff import *

singleElectronPt20OutputModule = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring("singleElectronPt20SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
      ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('EXOMu'), #name a name you like.
        dataTier = cms.untracked.string('EXOGroup')
    ),
    fileName = cms.untracked.string('ElectronPt20Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory. 
  )

singleElectronPt15OutputModule = cms.OutputModule("PoolOutputModule",
                                            outputCommands = cms.untracked.vstring(),
                                            SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("singleElectronPt15SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                            dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('EXOMu'), #name a name you like.
    dataTier = cms.untracked.string('EXOGroup')
    ),
                                            fileName = cms.untracked.string('ElectronPt15Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory.
                                            )

singleElectronPt10OutputModule = cms.OutputModule("PoolOutputModule",
                                            outputCommands = cms.untracked.vstring(),
                                            SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("singleElectronPt10SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                            dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('EXOMu'), #name a name you like.
    dataTier = cms.untracked.string('EXOGroup')
    ),
                                            fileName = cms.untracked.string('ElectronPt10Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory.
                                            )

singleElectronPt5OutputModule = cms.OutputModule("PoolOutputModule",
                                           outputCommands = cms.untracked.vstring(),
                                           SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("singleElectronPt5SkimPath") #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
    ),
                                           dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('EXOMu'), #name a name you like.
    dataTier = cms.untracked.string('EXOGroup')
    ),
                                           fileName = cms.untracked.string('ElectronPt5Skim.root') # can be modified later in EXOMuOct09_cfg.py in  test directory.
                                           )

superClusterPt5OutputModule = cms.OutputModule("PoolOutputModule",
                                               outputCommands = cms.untracked.vstring(),
                                               SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("superClusterPt5SkimPath")
    ),
                                               dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('EXOMu'), #name a name you like.
    dataTier = cms.untracked.string('EXOGroup')
    ),
                                               fileName = cms.untracked.string('electronPt1_ecalSCPt1Skim.root')
                                                 )


#default output contentFEVTHLTALLEventContent
singleElectronPt20OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
singleElectronPt15OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
singleElectronPt10OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
singleElectronPt5OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
superClusterPt5OutputModule.outputCommands.extend(FEVTHLTALLEventContent.outputCommands)
#add specific content you need. 
#SpecifiedEvenetContent=cms.PSet(
#    outputCommands = cms.untracked.vstring(
#      "keep *_singleHLTElectrononFilter_*_*",
#	  "keep *_singleRecoElectrononFilter_*_*",
#      )
#    )
#singleElectronPt20OutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)
#singleElectronPt15OutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)
#singleElectronPt10OutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)
#singleElectronPt5OutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)


