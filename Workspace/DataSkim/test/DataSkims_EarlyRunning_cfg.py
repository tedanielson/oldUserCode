import FWCore.ParameterSet.Config as cms

process = cms.Process("TriggerSampleSkim")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)
#number of Events to be skimmed.
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

#replace fileNames  with the file you want to skim

process.source = cms.Source("PoolSource")

#load the EventContent and Skim cff/i files for EXOMu sub-skim.
process.load('Workspace.data_skim.singleMuonSkim_EventContent_cfi')
process.load('Workspace.data_skim.singleMuonSkim_cff')
#process.load('Workspace.data_skim.singleElectronSkim_EventContent_cfi')
#process.load('Workspace.data_skim.singleElectronSkim_cff')
process.load('Workspace.data_skim.muonTagProbe_EventContent_cfi')
process.load('Workspace.data_skim.muonTagProbeFilters_cff')
process.load('Workspace.data_skim.electronTagProbe_EventContent_cfi')
process.load('Workspace.data_skim.electronTagProbeFilters_cff')
process.load('Workspace.data_skim.singlePhotonSkim_EventContent_cfi')
process.load('Workspace.data_skim.singlePhotonSkim_cff')
process.load('Workspace.data_skim.jetSkim_EventContent_cfi')
process.load('Workspace.data_skim.jetSkim_cff')
process.load('Workspace.data_skim.METSkim_EventContent_cfi')
process.load('Workspace.data_skim.METSkim_cff')
process.load('Workspace.data_skim.commonCuts_cff')

#possible trigger modification by user, defualt HLT_Mu9 in EXOMuOct09_cff.py
#process.exoticaMuHLT.HLTPaths = ['HLT_Mu3']


#define output file name. 
#process.exoticaMuOutputModule.fileNames = cms.untracked.vstring('EXOMuOct09.root')#possible EventContent  modification by user

#AODSIMEventContent/AODEventContent/RECOSIMEventContent/RECOEventContent
#by uncommenting next lines.
#from Configuration.EventContent.EventContent_cff import *
#from SUSYBSMAnalysis.Skimming.EXOMuOct09_EventContent_cfi import *
#SpecifiedEvenetContent=cms.PSet(
#    outputCommands = cms.untracked.vstring(
#      "keep *_exoticaHLTMuonFilter_*_*",
#	  "keep *_exoticaRecoMuonFilter_*_*",
#      )
#    )
#process.exoticaMuOutputModule.outputCommands.extend(RECOSIMEventContent.outputCommands)
#process.exoticaMuOutputModule.outputCommands.extend(SpecifiedEvenetContent.outputCommands)

#possible cut modification by user
#process.exoticaHLTMuonFilter.cut=  cms.string('pt > 5.0')
#process.exoticaHLTMuonFilter.minN=   cms.int32(2) 
#process.exoticaRecoMuonFilter.cut=  cms.string('pt > 15.0')

#Possible exoticaMuHLTQualitySeq or exoticaMuRecoQualitySeq selection by user
#process.exoticaMuSkimPath=cms.Path(process.exoticaMuHLTQualitySeq)
process.singleMuPt5SkimPath=cms.Path(process.singleMuPt5RecoQualitySeq)
#process.superClusterPt5SkimPath=cms.Path(process.singleElectronSCRecoQualitySeq)
process.singlePhotonPt5SkimPath=cms.Path(process.singlePhotonPt5QualitySeq)
process.muonJPsiMMSkimPath=cms.Path(process.muonJPsiMMRecoQualitySeq)
process.jetSkimPath=cms.Path(process.jetRecoQualitySeq)
#process.METSkimPath=cms.Path(process.METQualitySeq)

process.load('HLTrigger.special.HLTTriggerTypeFilter_cfi')
#from HLTrigger.special.HLTTriggerTypeFilter_cfi import *
#hltTriggerTypeFilter.SelectedTriggerType = 1
process.hltTriggerTypeFilter.SelectedTriggerType = 1

process.endPath = cms.EndPath(process.hltTriggerTypeFilter*
                              process.primaryVertexFilter*
                              process.singleMuPt5OutputModule+
#                              process.superClusterPt5OutputModule+
                              process.singlePhotonPt5OutputModule+                              
                              process.muonJPsiMMOutputModule+
                              process.jetOutputModule)
#+process.METOutputModule)
#process.endPath = cms.EndPath(process.singleMuOutputModule+process.singlePhotonOutputModule+process.muonZMMOutputModule+process.jetOutputModule+process.METOutputModule)
