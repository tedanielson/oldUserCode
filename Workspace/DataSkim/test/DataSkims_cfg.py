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
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#    '/store/relval/CMSSW_3_3_0/RelValZMM/GEN-SIM-RECO/STARTUP31X_V8-v1/0009/BE1D1CF5-2FB7-DE11-915E-001D09F290CE.root',
#    '/store/relval/CMSSW_3_3_0/RelValInclusiveppMuX/GEN-SIM-RECO/MC_31X_V9-v1/0002/BA1B9439-C4B7-DE11-93E3-001A92971B0C.root',
#    '/store/relval/CMSSW_3_3_0/RelValJpsiMM_Pt_0_20/GEN-SIM-RECO/STARTUP31X_V8-v1/0002/FE7BCA5A-73B7-DE11-8BFE-001A92810ADE.root',
    '/store/relval/CMSSW_3_3_4/RelValTTbar/GEN-SIM-RECO/STARTUP3X_V8A-v1/0001/4C6D127D-B0D5-DE11-A6C9-002618943939.root',
#    '/store/relval/CMSSW_3_3_0/RelValZEE/GEN-SIM-RECO/MC_31X_V9-v2/0002/AA25E184-4ABD-DE11-AC55-0017312B5E1D.root',
    '/store/relval/CMSSW_3_3_4/RelValMinBias/GEN-SIM-RECO/STARTUP3X_V8A-v1/0001/F24C0338-6BD5-DE11-A9D4-001A9281170A.root',
    '/store/relval/CMSSW_3_3_4/RelValMinBias/GEN-SIM-RECO/STARTUP3X_V8A-v1/0000/A0425179-3DD5-DE11-A4F9-001731A2832D.root'
#    'file:00E91114-65D8-DE11-A993-000423D951D4.root',
#    'file:0AB77EB4-61D8-DE11-B504-001617C3B65A.root',
#    'file:12DB83CF-60D8-DE11-8468-0019B9F72D71.root',
#    'file:143804D2-60D8-DE11-B798-001D09F27067.root',
#    'file:1451D2A3-61D8-DE11-AF0E-000423D6C8EE.root',
#    'file:1844B2D2-60D8-DE11-B104-001D09F2462D.root',
#    'file:18A4F61A-60D8-DE11-8808-001D09F2932B.root',
#    'file:1A6386DB-67D8-DE11-9F4E-000423D9517C.root',
#    'file:1C721E8E-61D8-DE11-AAF9-001617C3B70E.root',
#    'file:22BD49ED-62D8-DE11-9E72-000423D985B0.root',
#    'file:3016EE8D-61D8-DE11-B672-000423D9939C.root',
#    'file:4E8FCAAE-5ED8-DE11-9DB7-001D09F295A1.root',
#    'file:54BB61A9-63D8-DE11-B671-001D09F28D4A.root',
#    'file:568E4F1C-60D8-DE11-B794-001D09F29597.root',
#    'file:62910B34-6ED8-DE11-8749-0019B9F707D8.root',
#    'file:62F6B6A1-63D8-DE11-AAD0-001D09F2905B.root',
#    'file:64FC961C-60D8-DE11-8214-001D09F24D4E.root',
#    'file:6CDDE7B4-65D8-DE11-8870-001D09F2447F.root',
#    'file:6CE09919-65D8-DE11-92D3-001617C3B5F4.root',
#    'file:6EE2829C-63D8-DE11-9F8F-001D09F27003.root',
#    'file:86222D39-65D8-DE11-8E2E-000423D98B6C.root',
#    'file:8CAEB23D-62D8-DE11-89B8-000423D6B48C.root',
#    'file:90DACCD6-60D8-DE11-83EE-001D09F2A49C.root',
#    'file:965D853E-62D8-DE11-88EF-001D09F28F0C.root',
#    'file:9A24DE3D-62D8-DE11-B5DB-001617E30D4A.root',
#    'file:A27F46CE-60D8-DE11-B370-001D09F25217.root',
#    'file:B04DE53D-62D8-DE11-8729-001D09F25208.root',
#    'file:B0F750D9-60D8-DE11-9199-000423D98EC4.root',
#    'file:B222E0D6-60D8-DE11-8014-001D09F24691.root',
#    'file:C69D0841-62D8-DE11-BC12-000423D98634.root',
#    'file:CAF62820-60D8-DE11-BA5A-001D09F23F2A.root',
#    'file:DCB300D3-60D8-DE11-BFFF-001D09F231B0.root',
#    'file:DCF54250-64D8-DE11-8C0E-001D09F24EE3.root',
#    'file:E254FDB3-5ED8-DE11-82CB-001D09F24691.root',
#    'file:EA227846-62D8-DE11-8EFF-001D09F2906A.root',
#    'file:F8F49C1B-60D8-DE11-AB34-001D09F28F0C.root'
#    'file:bit40or41skim.root'
    )
                            )

#load the EventContent and Skim cff/i files for EXOMu sub-skim.
process.load('Workspace.data_skim.singleMuonSkim_EventContent_cfi')
process.load('Workspace.data_skim.singleMuonSkim_cff')
process.load('Workspace.data_skim.singleElectronSkim_EventContent_cfi')
process.load('Workspace.data_skim.singleElectronSkim_cff')
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
process.singleMuPt20SkimPath=cms.Path(process.singleMuPt20RecoQualitySeq)
process.singleMuPt15SkimPath=cms.Path(process.singleMuPt15RecoQualitySeq)
process.singleMuPt10SkimPath=cms.Path(process.singleMuPt10RecoQualitySeq)
process.singleMuPt5SkimPath=cms.Path(process.singleMuPt5RecoQualitySeq)
process.singleElectronPt20SkimPath=cms.Path(process.singleElectronPt20RecoQualitySeq)
process.singleElectronPt15SkimPath=cms.Path(process.singleElectronPt15RecoQualitySeq)
process.singleElectronPt10SkimPath=cms.Path(process.singleElectronPt10RecoQualitySeq)
process.singleElectronPt5SkimPath=cms.Path(process.singleElectronPt5RecoQualitySeq)
process.singlePhotonPt20SkimPath=cms.Path(process.singlePhotonPt20QualitySeq)
process.singlePhotonPt15SkimPath=cms.Path(process.singlePhotonPt15QualitySeq)
process.singlePhotonPt10SkimPath=cms.Path(process.singlePhotonPt10QualitySeq)
process.singlePhotonPt5SkimPath=cms.Path(process.singlePhotonPt5QualitySeq)
process.muonZMMSkimPath=cms.Path(process.muonZMMRecoQualitySeq)
process.muonJPsiMMSkimPath=cms.Path(process.muonJPsiMMRecoQualitySeq)
process.electronZEESkimPath=cms.Path(process.electronZEERecoQualitySeq)
process.jetSkimPath=cms.Path(process.jetRecoQualitySeq)
process.METSkimPath=cms.Path(process.METQualitySeq)

process.endPath = cms.EndPath(process.singleMuPt20OutputModule+process.singleMuPt15OutputModule+process.singleMuPt10OutputModule+
                              process.singleMuPt5OutputModule+
                              process.singleElectronPt20OutputModule+process.singleElectronPt15OutputModule+process.singleElectronPt10OutputModule+
                              process.singleElectronPt5OutputModule+
                              process.singlePhotonPt20OutputModule+process.singlePhotonPt15OutputModule+process.singlePhotonPt10OutputModule+
                              process.singlePhotonPt5OutputModule+                              
                              process.muonZMMOutputModule+process.muonJPsiMMOutputModule+
                              process.electronZEEOutputModule+
                              process.jetOutputModule+process.METOutputModule)
#process.endPath = cms.EndPath(process.singleMuOutputModule+process.singlePhotonOutputModule+process.muonZMMOutputModule+process.jetOutputModule+process.METOutputModule)
