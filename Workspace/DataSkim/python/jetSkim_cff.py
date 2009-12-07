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

Jet2 = cms.EDProducer("EtaPtMinCandViewSelector",
                      src = cms.InputTag("iterativeCone5CaloJets"),
                      ptMin   = cms.double(10),
                      etaMin = cms.double(-2),
                      etaMax = cms.double(2)
                      )

Jet1 = cms.EDProducer("EtaPtMinCandViewSelector",
                      src = cms.InputTag("Jet2"),
                      ptMin   = cms.double(20),
                      etaMin = cms.double(-2),
                      etaMax = cms.double(2)
                      )
#Define the Reco quality cut
#jetFilter = cms.EDFilter("CaloJetSelector",
#                               src = cms.InputTag("iterativeCone5CaloJets"),
#                               cut = cms.string('pt > 100 && abs(eta) < 2.0' ),
#                               filter = cms.bool(True),
#                              minNumber = cms.uint32(2)
#                                sizeSelector = cms.uint32(2)
#                               )
                               
dijetFilter = cms.EDFilter("CandViewCountFilter",
                           src = cms.InputTag("Jet2"),
                           minNumber = cms.uint32(2)
                           )

jetFilter = cms.EDFilter("CandViewCountFilter",
                               src = cms.InputTag("Jet1"),
                               minNumber = cms.uint32(1)
                               )

#Define group sequence, using HLT/Reco quality cut. 
#exoticaMuHLTQualitySeq = cms.Sequence()
jetRecoQualitySeq = cms.Sequence(
    #exoticaMuHLT+
    Jet2+Jet1+dijetFilter+jetFilter
)

