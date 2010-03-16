import FWCore.ParameterSet.Config as cms

process = cms.Process("mmm")

process.load('Workspace.data_skim.commonCuts_cff') 
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR10_E_V3::All'

# UNCOMMENT THIS LINE TO RUN ON SETTINGS FROM THE DATABASE
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource', 'GlobalTag')

#process.load("DQMServices.Core.DQM_cfg")
process.DQMStore = cms.Service("DQMStore")

#process.l1RCTParametersTest = cms.EDAnalyzer("L1RCTParametersTester")
#process.l1RCTChannelMaskTest = cms.EDAnalyzer("L1RCTChannelMaskTester")
 
# # paths to be run
 
 
#process.p = cms.Path(process.l1RCTParametersTest
#                      *process.l1RCTChannelMaskTest)
 

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring(
#        'file:jetSkim.root')
#,eventsToProcess = cms.untracked.VEventRange('124120:11240481-124120:11240481' )
#,eventsToProcess = cms.untracked.VEventRange('124120:15416287-124120:15416287' )
#)



process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'file:run130910_OFFLINE/res/muonPt05Skim_1.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_2.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_3.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_4.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_5.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_6.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_7.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_8.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_9.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_10.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_11.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_12.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_13.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_14.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_15.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_16.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_17.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_18.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_19.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_20.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_21.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_22.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_23.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_24.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_25.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_26.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_27.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_28.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_29.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_30.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_31.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_32.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_33.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_34.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_35.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_36.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_37.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_38.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_39.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_40.root',
    'file:run130910_OFFLINE/res/muonPt05Skim_41.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_1.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_2.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_3.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_4.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_5.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_6.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_7.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_8.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_9.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_10.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_11.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_12.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_13.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_14.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_15.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_16.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_17.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_18.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_19.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_20.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_21.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_22.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_23.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_24.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_25.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_26.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_27.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_28.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_29.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_30.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_31.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_32.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_33.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_34.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_35.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_36.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_37.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_38.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_39.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_40.root',
    'file:run130910_OFFLINE/res/photonPt5Skim_41.root',
    'file:run130910_OFFLINE/res/jetSkim_1.root',
    'file:run130910_OFFLINE/res/jetSkim_2.root',
    'file:run130910_OFFLINE/res/jetSkim_3.root',
    'file:run130910_OFFLINE/res/jetSkim_4.root',
    'file:run130910_OFFLINE/res/jetSkim_5.root',
    'file:run130910_OFFLINE/res/jetSkim_6.root',
    'file:run130910_OFFLINE/res/jetSkim_7.root',
    'file:run130910_OFFLINE/res/jetSkim_8.root',
    'file:run130910_OFFLINE/res/jetSkim_9.root',
    'file:run130910_OFFLINE/res/jetSkim_10.root',
    'file:run130910_OFFLINE/res/jetSkim_11.root',
    'file:run130910_OFFLINE/res/jetSkim_12.root',
    'file:run130910_OFFLINE/res/jetSkim_13.root',
    'file:run130910_OFFLINE/res/jetSkim_14.root',
    'file:run130910_OFFLINE/res/jetSkim_15.root',
    'file:run130910_OFFLINE/res/jetSkim_16.root',
    'file:run130910_OFFLINE/res/jetSkim_17.root',
    'file:run130910_OFFLINE/res/jetSkim_18.root',
    'file:run130910_OFFLINE/res/jetSkim_19.root',
    'file:run130910_OFFLINE/res/jetSkim_20.root',
    'file:run130910_OFFLINE/res/jetSkim_21.root',
    'file:run130910_OFFLINE/res/jetSkim_22.root',
    'file:run130910_OFFLINE/res/jetSkim_23.root',
    'file:run130910_OFFLINE/res/jetSkim_24.root',
    'file:run130910_OFFLINE/res/jetSkim_25.root',
    'file:run130910_OFFLINE/res/jetSkim_26.root',
    'file:run130910_OFFLINE/res/jetSkim_27.root',
    'file:run130910_OFFLINE/res/jetSkim_28.root',
    'file:run130910_OFFLINE/res/jetSkim_29.root',
    'file:run130910_OFFLINE/res/jetSkim_30.root',
    'file:run130910_OFFLINE/res/jetSkim_31.root',
    'file:run130910_OFFLINE/res/jetSkim_32.root',
    'file:run130910_OFFLINE/res/jetSkim_33.root',
    'file:run130910_OFFLINE/res/jetSkim_34.root',
    'file:run130910_OFFLINE/res/jetSkim_35.root',
    'file:run130910_OFFLINE/res/jetSkim_36.root',
    'file:run130910_OFFLINE/res/jetSkim_37.root',
    'file:run130910_OFFLINE/res/jetSkim_38.root',
    'file:run130910_OFFLINE/res/jetSkim_39.root',
    'file:run130910_OFFLINE/res/jetSkim_40.root',
    'file:run130910_OFFLINE/res/jetSkim_41.root',
    )
   )

#,eventsToProcess = cms.untracked.VEventRange('124120:6613074-124120:6613074' )
#,eventsToProcess = cms.untracked.VEventRange('124120:2161318-124120:2161318' )
#,eventsToProcess = cms.untracked.VEventRange('124120:8258900-124120:8258900' )

process.copyAll = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("goldenSample.root") )
process.printEventNumber = cms.EDAnalyzer("AsciiOutputModule")
process.out = cms.EndPath(process.printoutModule + process.copyAll)
