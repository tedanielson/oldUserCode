import FWCore.ParameterSet.Config as cms

process = cms.Process("mmm")

process.load('Workspace.data_skim.commonCuts_cff') 
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR09_R_35X_V3::All'

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
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123596_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123732_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123815_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123818_OFFLINE.root',
##    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123906_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123908_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123970_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123976_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123977_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123978_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123985_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123987_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124009_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124020_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124022_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124023_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124024_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124025_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124027_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124030_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124120_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124228_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124230_OFFLINE.root',
#    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124275_OFFLINE.root',
    'file:goldenSample_124230_OFFLINE.root'
    )
   )

#,eventsToProcess = cms.untracked.VEventRange('124120:6613074-124120:6613074' )
#,eventsToProcess = cms.untracked.VEventRange('124120:2161318-124120:2161318' )
#,eventsToProcess = cms.untracked.VEventRange('124120:8258900-124120:8258900' )

process.copyAll = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("goldenSample.root") )
process.printEventNumber = cms.EDAnalyzer("AsciiOutputModule")
process.out = cms.EndPath(process.printoutModule + process.copyAll)
