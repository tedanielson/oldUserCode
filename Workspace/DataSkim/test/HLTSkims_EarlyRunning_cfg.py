import FWCore.ParameterSet.Config as cms

process = cms.Process("BigHairyPenis")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.GeometryExtended_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.EventContent.EventContent_cff')
process.GlobalTag.globaltag = "GR10_E_V5::All"

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )
#number of Events to be skimmed.
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

#replace fileNames  with the file you want to skim

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:goldenSample_run135528_EXPRESS_noVertexCut_8.root')
    )

#load the EventContent and Skim cff/i files for EXOMu sub-skim.
#process.load('Workspace.data_skim.singleMuonSkim_EventContent_cfi')
#process.load('Workspace.data_skim.singleMuonSkim_cff')
#process.load('Workspace.data_skim.singleElectronSkim_EventContent_cfi')
#process.load('Workspace.data_skim.singleElectronSkim_cff')
#process.load('Workspace.data_skim.muonTagProbe_EventContent_cfi')
#process.load('Workspace.data_skim.muonTagProbeFilters_cff')
#process.load('Workspace.data_skim.electronTagProbe_EventContent_cfi')
#process.load('Workspace.data_skim.electronTagProbeFilters_cff')
#process.load('Workspace.data_skim.singlePhotonSkim_EventContent_cfi')
#process.load('Workspace.data_skim.singlePhotonSkim_cff')
#process.load('Workspace.data_skim.singlePfTauSkim_EventContent_cfi')
#process.load('Workspace.data_skim.singlePfTauSkim_cff')
#process.load('Workspace.data_skim.jetSkim_EventContent_cfi')
#process.load('Workspace.data_skim.jetSkim_cff')
#process.load('Workspace.data_skim.METSkim_EventContent_cfi')
#process.load('Workspace.data_skim.METSkim_cff')
#process.load('Workspace.data_skim.commonCuts_cff')
process.load('Workspace.data_skim.hltFilters_cff')
process.load('Workspace.data_skim.hltSkim_EventContent_cfi')

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
#process.singleMuPt5SkimPath=cms.Path(process.singleMuPt5RecoQualitySeq)
#process.singleElectronPt5SkimPath=cms.Path(process.singleElectronPt5RecoQualitySeq)
#process.superClusterPt5SkimPath=cms.Path(process.singleElectronSCRecoQualitySeq)
#process.singlePfTauPt15SkimPath=cms.Path(process.singlePfTauPt15QualitySeq)
#process.singlePhotonPt5SkimPath=cms.Path(process.singlePhotonPt5QualitySeq)
#process.muonJPsiMMSkimPath=cms.Path(process.muonJPsiMMRecoQualitySeq)
#process.jetSkimPath=cms.Path(process.jetRecoQualitySeq)
#process.METSkimPath=cms.Path(process.METQualitySeq)

process.HLT_Mu3SkimPath=cms.Path(process.HLT_Mu3TrigSeq)
process.HLT_Mu5SkimPath=cms.Path(process.HLT_Mu5TrigSeq)
process.HLT_Mu9SkimPath=cms.Path(process.HLT_Mu9TrigSeq)
process.HLT_DoubleMu3SkimPath=cms.Path(process.HLT_DoubleMu3TrigSeq)
process.HLT_Jet15USkimPath=cms.Path(process.HLT_Jet15UTrigSeq)
process.HLT_Jet30USkimPath=cms.Path(process.HLT_Jet30UTrigSeq)
process.HLT_Jet50USkimPath=cms.Path(process.HLT_Jet50UTrigSeq)
process.HLT_DiJetAve30U_8E29SkimPath=cms.Path(process.HLT_DiJetAve30U_8E29TrigSeq)
process.HLT_QuadJet15USkimPath=cms.Path(process.HLT_QuadJet15UTrigSeq)
process.HLT_MET45SkimPath=cms.Path(process.HLT_MET45TrigSeq)
process.HLT_MET100SkimPath=cms.Path(process.HLT_MET100TrigSeq)
process.HLT_HT100USkimPath=cms.Path(process.HLT_HT100UTrigSeq)
process.HLT_Ele10_LW_EleId_L1RSkimPath=cms.Path(process.HLT_Ele10_LW_EleId_L1RTrigSeq)
process.HLT_Ele15_SiStrip_L1RSkimPath=cms.Path(process.HLT_Ele15_SiStrip_L1RTrigSeq)
process.HLT_Ele20_LW_L1RSkimPath=cms.Path(process.HLT_Ele20_LW_L1RTrigSeq)
process.HLT_DoubleEle5_SW_L1RSkimPath=cms.Path(process.HLT_DoubleEle5_SW_L1RTrigSeq)
process.HLT_Photon10_L1RSkimPath=cms.Path(process.HLT_Photon10_L1RTrigSeq)
process.HLT_Photon15_L1RSkimPath=cms.Path(process.HLT_Photon15_L1RTrigSeq)
process.HLT_Photon20_L1RSkimPath=cms.Path(process.HLT_Photon20_L1RTrigSeq)
process.HLT_DoublePhoton10_L1RSkimPath=cms.Path(process.HLT_DoublePhoton10_L1RTrigSeq)
process.HLT_SingleLooseIsoTau20SkimPath=cms.Path(process.HLT_SingleLooseIsoTau20TrigSeq)
process.HLT_DoubleLooseIsoTau15SkimPath=cms.Path(process.HLT_DoubleLooseIsoTau15TrigSeq)
process.HLT_MinBiasBSCSkimPath=cms.Path(process.HLT_MinBiasBSCTrigSeq)
process.HLT_BTagMu_Jet10USkimPath=cms.Path(process.HLT_BTagMu_Jet10UTrigSeq)

process.load('HLTrigger.special.HLTTriggerTypeFilter_cfi')
#from HLTrigger.special.HLTTriggerTypeFilter_cfi import *
#hltTriggerTypeFilter.SelectedTriggerType = 1
process.hltTriggerTypeFilter.SelectedTriggerType = 1

#process.singleMuPt5OutputModule.fileName = cms.untracked.string('rfio:/castor/cern.ch/user/t/tdaniels/2010_TPG_SKIMS/ExpressPhysics/run133511/muonPt05Skim_1.root')
#process.singleElectronPt5OutputModule.fileName = cms.untracked.string('rfio:/castor/cern.ch/user/t/tdaniels/2010_TPG_SKIMS/ExpressPhysics/run133511/ElectronPt5Skim_1.root')
#process.jetOutputModule.fileName = cms.untracked.string('rfio:/castor/cern.ch/user/t/tdaniels/2010_TPG_SKIMS/ExpressPhysics/run133511/jetSkim_1.root')
#process.singlePhotonPt5OutputModule.fileName = cms.untracked.string('rfio:/castor/cern.ch/user/t/tdaniels/2010_TPG_SKIMS/ExpressPhysics/run133511/photonPt5Skim_1.root')
#process.singlePfTauPt15OutputModule.fileName = cms.untracked.string('rfio:/castor/cern.ch/user/t/tdaniels/2010_TPG_SKIMS/ExpressPhysics/run133511/pfTauPt15Skim_1.root')
#process.muonJPsiMMOutputModule.fileName = cms.untracked.string('rfio:/castor/cern.ch/user/t/tdaniels/2010_TPG_SKIMS/ExpressPhysics/run133511/muonJPsiMMSkim_1.root')

process.endPath = cms.EndPath(process.hltTriggerTypeFilter*
#                              process.primaryVertexFilter*
#                              process.singleMuPt5OutputModule+
#                              process.singleElectronPt5OutputModule+
#                              process.singlePfTauPt15OutputModule+
#                              process.singlePhotonPt5OutputModule+                              
#                              process.muonJPsiMMOutputModule+
#                              process.jetOutputModule)
                              process.hltOutputModule)
#+process.METOutputModule)
#process.endPath = cms.EndPath(process.singleMuOutputModule+process.singlePhotonOutputModule+process.muonZMMOutputModule+process.jetOutputModule+process.METOutputModule)
