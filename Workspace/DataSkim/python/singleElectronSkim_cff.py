import FWCore.ParameterSet.Config as cms

#from HLTrigger.HLTfilters.hltHighLevel_cfi import *
#exoticaMuHLT = hltHighLevel
#Define the HLT path to be used.
#exoticaMuHLT.HLTPaths =['HLT_L1MuOpen']
#exoticaMuHLT.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT8E29")

#Define the HLT quality cut 
#exoticaHLTMuonFilter = cms.EDFilter("HLTSummaryFilter",
#    summary = cms.InputTag("hltTriggerSummaryAOD","","HLT8E29"), # trigger summary
#    member  = cms.InputTag("hltL3MuonCandidates","","HLT8E29"),      # filter or collection									
#    cut     = cms.string("pt>0"),                     # cut on trigger object
#    minN    = cms.int32(0)                  # min. # of passing objects needed
# )
                               

#Define the Reco quality cut
singleRecoElectronPt20Filter = cms.EDFilter("GsfElectronRefSelector",
                                        src = cms.InputTag("gsfElectrons"),
                                        cut = cms.string('pt > 20.0 && abs(eta) < 2.1 ' ),
                                        filter = cms.bool(True),
                                        minN    = cms.int32(1) 
                                        )

singleRecoElectronPt15Filter = cms.EDFilter("GsfElectronRefSelector",
                                        src = cms.InputTag("gsfElectrons"),
                                        cut = cms.string('pt > 15.0 && abs(eta) < 2.1 ' ),
                                        filter = cms.bool(True),
                                        minN    = cms.int32(1)
                                        )

singleRecoElectronPt10Filter = cms.EDFilter("GsfElectronRefSelector",
                                        src = cms.InputTag("gsfElectrons"),
                                        cut = cms.string('pt > 10.0 && abs(eta) < 2.1 ' ),
                                        filter = cms.bool(True),
                                        minN    = cms.int32(1)
                                        )

singleRecoElectronPt5Filter = cms.EDFilter("GsfElectronRefSelector",
                                        src = cms.InputTag("gsfElectrons"),
                                        cut = cms.string('pt > 5.0 && abs(eta) < 2.1 ' ),
                                        filter = cms.bool(True),
                                        minN    = cms.int32(1)
                                        )

#Define group sequence, using HLT/Reco quality cut. 
#singleMuHLTQualitySeq = cms.Sequence()
singleElectronPt20RecoQualitySeq = cms.Sequence(
    #singleElectronHLT+
    singleRecoElectronPt20Filter
)

singleElectronPt15RecoQualitySeq = cms.Sequence(
    #singleElectronHLT+
    singleRecoElectronPt15Filter
)

singleElectronPt10RecoQualitySeq = cms.Sequence(
    #singleElectronHLT+
    singleRecoElectronPt10Filter
)

singleElectronPt5RecoQualitySeq = cms.Sequence(
        #singleElectronHLT+
        singleRecoElectronPt5Filter
        )
