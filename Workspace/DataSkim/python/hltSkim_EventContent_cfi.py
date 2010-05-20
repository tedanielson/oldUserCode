import FWCore.ParameterSet.Config as cms
from Configuration.EventContent.EventContent_cff import *


hltOutputModule = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring("HLT_Mu3SkimPath",
                                   "HLT_Mu5SkimPath",
                                   "HLT_Mu9SkimPath",
                                   "HLT_DoubleMu3SkimPath",
                                   "HLT_Jet15USkimPath",
                                   "HLT_Jet30USkimPath",
                                   "HLT_Jet50USkimPath",
                                   "HLT_DiJetAve30U_8E29SkimPath",
                                   "HLT_QuadJet15USkimPath",
                                   "HLT_MET45SkimPath",
                                   "HLT_MET100SkimPath",
                                   "HLT_HT100USkimPath",
                                   "HLT_Ele10_LW_EleId_L1RSkimPath",
                                   "HLT_Ele15_SiStrip_L1RSkimPath",
                                   "HLT_Ele20_LW_L1RSkimPath",
                                   "HLT_DoubleEle5_SW_L1RSkimPath",
                                   "HLT_Photon10_L1RSkimPath",
                                   "HLT_Photon15_L1RSkimPath",
                                   "HLT_Photon20_L1RSkimPath",
                                   "HLT_DoublePhoton10_L1RSkimPath",
                                   "HLT_SingleLooseIsoTau20SkimPath",
                                   "HLT_DoubleLooseIsoTau15SkimPath",
                                   "HLT_MinBiasBSCSkimPath",
                                   "HLT_BTagMu_Jet10USkimPath"
                                   ) #the selector name must be same as the path name in EXOMuOct09_cfg.py in test directory.
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



