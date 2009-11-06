import FWCore.ParameterSet.Config as cms

process = cms.Process("EXOMuOct09Skim")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)
#number of Events to be skimmed.
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

#replace fileNames  with the file you want to skim
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#    '/store/relval/CMSSW_3_3_0/RelValZMM/GEN-SIM-RECO/STARTUP31X_V8-v1/0009/BE1D1CF5-2FB7-DE11-915E-001D09F290CE.root',
#    '/store/relval/CMSSW_3_3_0/RelValInclusiveppMuX/GEN-SIM-RECO/MC_31X_V9-v1/0002/BA1B9439-C4B7-DE11-93E3-001A92971B0C.root',
#    '/store/relval/CMSSW_3_3_0/RelValJpsiMM_Pt_0_20/GEN-SIM-RECO/STARTUP31X_V8-v1/0002/FE7BCA5A-73B7-DE11-8BFE-001A92810ADE.root',
    '/store/relval/CMSSW_3_3_0/RelValTTbar/GEN-SIM-RECO/STARTUP31X_V8-v1/0009/C8EF0A0D-75B7-DE11-A2E8-001D09F27003.root'
	    )
)

#load the EventContent and Skim cff/i files for EXOMu sub-skim.
process.load('Workspace.data_skim.EXOMuOct09_EventContent_cfi')
process.load('Workspace.data_skim.EXOMuOct09_cff')
process.load('Workspace.data_skim.Skim2AtOnceTest_EventContent_cfi')
process.load('Workspace.data_skim.Skim2AtOnceTest_cff')

#possible trigger modification by user, defualt HLT_Mu9 in EXOMuOct09_cff.py
#process.exoticaMuHLT.HLTPaths = ['HLT_Mu3']


#define output file name. 
process.exoticaMuOutputModule.fileNames = cms.untracked.vstring('EXOMuOct09.root')#possible EventContent  modification by user

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
process.exoticaMuSkimPath=cms.Path(process.exoticaMuRecoQualitySeq)
process.secondMuSkimPath=cms.Path(process.SecondMuRecoQualitySeq)

process.endPath = cms.EndPath(process.exoticaMuOutputModule+process.SecondOutputModule)
