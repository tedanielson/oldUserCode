import FWCore.ParameterSet.Config as cms

process = cms.Process("mmm")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR09_H_V6OFF::All'

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
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_1.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_2.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_3.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_4.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_5.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_6.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_7.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_8.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_9.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_10.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_11.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_12.root',
   #     'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/muonPt5Skim_13.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_1.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_2.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_3.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_4.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_5.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_6.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_7.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_8.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_9.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_10.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_11.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/photonPt5Skim_12.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_1.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_2.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_3.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_4.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_5.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_6.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_7.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_8.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_9.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_10.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_11.root',
        'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/PhysicsExpress/r124120/jetSkim_12.root'
   )

#,eventsToProcess = cms.untracked.VEventRange('124120:6613074-124120:6613074' )
#,eventsToProcess = cms.untracked.VEventRange('124120:2161318-124120:2161318' )
#,eventsToProcess = cms.untracked.VEventRange('124120:8258900-124120:8258900' )
)

process.copyAll = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("goldenSample.root") )
process.printEventNumber = cms.EDAnalyzer("AsciiOutputModule")
process.out = cms.EndPath(process.copyAll + process.printEventNumber)
