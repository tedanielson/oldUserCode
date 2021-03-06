import FWCore.ParameterSet.Config as cms

process = cms.Process("mmm")

process.load('Workspace.data_skim.commonCuts_cff') 
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR10_E_V4::All'

#UNCOMMENT THIS TO USE REAL MASKING FOR L1T
#process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource', 'GlobalTag')

process.DQMStore = cms.Service("DQMStore")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123596_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123615_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123732_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123815_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123818_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123906_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123908_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123970_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123976_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123977_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123978_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123985_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_123987_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124009_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124020_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124022_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124023_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124024_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124025_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124027_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124030_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124120_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124228_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124230_OFFLINE.root',
    'rfio:/castor/cern.ch/user/t/tdaniels/2009_TPG_SKIMS/OfflineMonitor/goldenSample_124275_OFFLINE.root',
    )
                            )

#UNCOMMENT THIS TO DEFINE A PARTICUALR BX FOR THE L1 PLOTS
#process.plotsMakerModule.defineBX= cms.untracked.int32(51)

#UNCOMMENT THIS IN THE PATH TO CUT ON THE TECH TRIGGER
process.load ('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
#KEEP THIS TO RESET L1T PRESCALES
process.es_prefer_l1GtTriggerMaskTechTrig = cms.ESPrefer("L1GtTriggerMaskTechTrigTrivialProducer","l1GtTriggerMaskTechTrig")
process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')
process.L1T1=process.hltLevel1GTSeed.clone()
process.L1T1.L1TechTriggerSeeding = cms.bool(True)
process.L1T1.L1SeedsLogicalExpression = cms.string('(40 OR 41) AND NOT (36 OR 37 OR 38 OR 39)')

#UNCOMMENT THIS IN THE PATH TO SELECT A PARTICULAR HLT PATH 
process.HLTFilter =cms.EDFilter(
     "HLTHighLevel",
     TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
     HLTPaths = cms.vstring('HLT_L1Jet6U'),           # provide list of HLT paths (or patterns) you want
     eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
     andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
     throw = cms.bool(False)    # throw exception on unknown path names
     )                   

process.copyAll = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("goldenSample.root") )
process.printEventNumber = cms.EDAnalyzer("AsciiOutputModule")
#UNCOMMENT THE FIRST ENTRY TO CUT ON THE PRIMARY VERTEX 
process.out = cms.EndPath(#process.primaryVertexFilter* 
                          #process.L1T1 * # TURN ON/OFF FOR L1 TECH FILTER
                          #process.HLTFilter * #TURN ON/OFF FOR HLT FILTER
                          process.printoutModule + # TURN ON/OFF FOR EventDump.txt
                          process.plotsMakerModule + # TURN ON/OFF FOR l1Plots.root
                          process.copyAll # OUTPUT FOR GOLDEN SAMPLE
                          )
