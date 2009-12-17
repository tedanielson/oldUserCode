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

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:jetSkim.root')
#,eventsToProcess = cms.untracked.VEventRange('124120:11240481-124120:11240481' )
,eventsToProcess = cms.untracked.VEventRange('124120:15416287-124120:15416287' )
)

process.copyAll = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("reco.root") )
process.printEventNumber = cms.EDAnalyzer("AsciiOutputModule")
process.out = cms.EndPath(process.copyAll + process.printEventNumber)


