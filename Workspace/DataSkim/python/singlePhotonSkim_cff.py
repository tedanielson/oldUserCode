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
singlePhotonPt20Filter = cms.EDFilter("PhotonSelector",
                                     src = cms.InputTag("photons"),
                                     cut = cms.string('pt > 20 && abs(eta) < 2.0' ),
                                     filter = cms.bool(True)                                                  
)
singlePhotonPt15Filter = cms.EDFilter("PhotonSelector",
                                                                           src = cms.InputTag("photons"),
                                                                           cut = cms.string('pt > 15 && abs(eta) < 2.0' ),
                                                                           filter = cms.bool(True)
                                      )
singlePhotonPt10Filter = cms.EDFilter("PhotonSelector",
                                                                           src = cms.InputTag("photons"),
                                                                           cut = cms.string('pt > 10 && abs(eta) < 2.0' ),
                                                                           filter = cms.bool(True)
                                      )
singlePhotonPt5Filter = cms.EDFilter("PhotonSelector",
                                                                           src = cms.InputTag("photons"),
                                                                           cut = cms.string('pt > 5 && abs(eta) < 2.0' ),
                                                                           filter = cms.bool(True)
                                      )



#Define group sequence, using HLT/Reco quality cut. 
#exoticaMuHLTQualitySeq = cms.Sequence()
singlePhotonPt20QualitySeq = cms.Sequence(
    #exoticaMuHLT+
    singlePhotonPt20Filter
)
singlePhotonPt15QualitySeq = cms.Sequence(
        #exoticaMuHLT+
        singlePhotonPt15Filter
        )
singlePhotonPt10QualitySeq = cms.Sequence(
        #exoticaMuHLT+
        singlePhotonPt10Filter
        )
singlePhotonPt5QualitySeq = cms.Sequence(
        #exoticaMuHLT+
        singlePhotonPt5Filter
        )

