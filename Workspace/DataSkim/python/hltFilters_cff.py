import FWCore.ParameterSet.Config as cms

HLT_Mu3Filter =cms.EDFilter(
         "HLTHighLevel",
              TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
              HLTPaths = cms.vstring('HLT_Mu3'),           # provide list of HLT paths (or patterns) you want
              eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
              andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
              throw = cms.bool(False)    # throw exception on unknown path names
              )

HLT_Mu3Filter =cms.EDFilter(
             "HLTHighLevel",
                           TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                           HLTPaths = cms.vstring('HLT_Mu3'),           # provide list of HLT paths (or patterns) you want
                           eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                           andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                           throw = cms.bool(False)    # throw exception on unknown path names
                           )

trigCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(100)
                               )

HLT_Mu3TrigSeq = cms.Sequence(HLT_Mu3Filter+trigCountFilter)
HLT_Mu3TrigSeq = cms.Sequence(HLT_Mu3Filter+trigCountFilter)
