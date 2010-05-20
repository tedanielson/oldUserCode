import FWCore.ParameterSet.Config as cms

HLT_Mu3Filter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Mu3'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Mu5Filter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Mu5'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Mu9Filter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Mu9'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_DoubleMu3Filter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_DoubleMu3'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )


HLT_Jet15UFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Jet15U'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Jet30UFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Jet30U'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Jet50UFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Jet50U'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_DiJetAve30U_8E29Filter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_DiJetAve30U_8E29'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_QuadJet15UFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_QuadJet15U'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_MET45Filter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_MET45'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_MET100Filter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_MET100'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_HT100UFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_HT100U'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Ele10_LW_EleId_L1RFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Ele10_LW_EleId_L1R'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Ele15_SiStrip_L1RFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Ele15_SiStrip_L1R'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Ele20_LW_L1RFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Ele20_LW_L1R'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_DoubleEle5_SW_L1RFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_DoubleEle5_SW_L1R'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Photon10_L1RFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Photon10_L1R'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Photon15_L1RFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Photon15_L1R'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Photon20_L1RFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_Photon20_L1R'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_DoublePhoton10_L1RFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_DoublePhoton10_L1R'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_SingleLooseIsoTau20Filter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_SingleLooseIsoTau20'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_DoubleLooseIsoTau15Filter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_DoubleLooseIsoTau15'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_MinBiasBSCFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_MinBiasBSC'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_BTagMu_Jet10UFilter =cms.EDFilter(
    "HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring('HLT_BTagMu_Jet10U'),           # provide list of HLT paths (or patterns) you want
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(False),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
    )

HLT_Mu3CountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Mu5CountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Mu9CountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_DoubleMu3CountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Jet15UCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Jet30UCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Jet50UCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_DiJetAve30U_8E29CountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_QuadJet15UCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_MET45CountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_MET100CountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_HT100UCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Ele10_LW_EleId_L1RCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Ele15_SiStrip_L1RCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Ele20_LW_L1RCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_DoubleEle5_SW_L1RCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Photon10_L1RCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Photon15_L1RCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_Photon20_L1RCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_DoublePhoton10_L1RCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_SingleLooseIsoTau20CountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_DoubleLooseIsoTau15CountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_MinBiasBSCCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )
HLT_BTagMu_Jet10UCountFilter = cms.EDFilter("EventCounter",
                               maxEvents = cms.int32(400)
                               )

HLT_Mu3TrigSeq = cms.Sequence(HLT_Mu3Filter+HLT_Mu3CountFilter)
HLT_Mu5TrigSeq = cms.Sequence(HLT_Mu5Filter+HLT_Mu5CountFilter)
HLT_Mu9TrigSeq = cms.Sequence(HLT_Mu9Filter+HLT_Mu9CountFilter)
HLT_DoubleMu3TrigSeq = cms.Sequence(HLT_DoubleMu3Filter+HLT_DoubleMu3CountFilter)
HLT_Jet15UTrigSeq = cms.Sequence(HLT_Jet15UFilter+HLT_Jet15UCountFilter)
HLT_Jet30UTrigSeq = cms.Sequence(HLT_Jet30UFilter+HLT_Jet30UCountFilter)
HLT_Jet50UTrigSeq = cms.Sequence(HLT_Jet50UFilter+HLT_Jet50UCountFilter)
HLT_DiJetAve30U_8E29TrigSeq = cms.Sequence(HLT_DiJetAve30U_8E29Filter+HLT_DiJetAve30U_8E29CountFilter)
HLT_QuadJet15UTrigSeq = cms.Sequence(HLT_QuadJet15UFilter+HLT_QuadJet15UCountFilter)
HLT_MET45TrigSeq = cms.Sequence(HLT_MET45Filter+HLT_MET45CountFilter)
HLT_MET100TrigSeq = cms.Sequence(HLT_MET100Filter+HLT_MET100CountFilter)
HLT_HT100UTrigSeq = cms.Sequence(HLT_HT100UFilter+HLT_HT100UCountFilter)
HLT_Ele10_LW_EleId_L1RTrigSeq = cms.Sequence(HLT_Ele10_LW_EleId_L1RFilter+HLT_Ele10_LW_EleId_L1RCountFilter)
HLT_Ele15_SiStrip_L1RTrigSeq = cms.Sequence(HLT_Ele15_SiStrip_L1RFilter+HLT_Ele15_SiStrip_L1RCountFilter)
HLT_Ele20_LW_L1RTrigSeq = cms.Sequence(HLT_Ele20_LW_L1RFilter+HLT_Ele20_LW_L1RCountFilter)
HLT_DoubleEle5_SW_L1RTrigSeq = cms.Sequence(HLT_DoubleEle5_SW_L1RFilter+HLT_DoubleEle5_SW_L1RCountFilter)
HLT_Photon10_L1RTrigSeq = cms.Sequence(HLT_Photon10_L1RFilter+HLT_Photon10_L1RCountFilter)
HLT_Photon15_L1RTrigSeq = cms.Sequence(HLT_Photon15_L1RFilter+HLT_Photon15_L1RCountFilter)
HLT_Photon20_L1RTrigSeq = cms.Sequence(HLT_Photon20_L1RFilter+HLT_Photon20_L1RCountFilter)
HLT_DoublePhoton10_L1RTrigSeq = cms.Sequence(HLT_DoublePhoton10_L1RFilter+HLT_DoublePhoton10_L1RCountFilter)
HLT_SingleLooseIsoTau20TrigSeq = cms.Sequence(HLT_SingleLooseIsoTau20Filter+HLT_SingleLooseIsoTau20CountFilter)
HLT_DoubleLooseIsoTau15TrigSeq = cms.Sequence(HLT_DoubleLooseIsoTau15Filter+HLT_DoubleLooseIsoTau15CountFilter)
HLT_MinBiasBSCTrigSeq = cms.Sequence(HLT_MinBiasBSCFilter+HLT_MinBiasBSCCountFilter)
HLT_BTagMu_Jet10UTrigSeq = cms.Sequence(HLT_BTagMu_Jet10UFilter+HLT_BTagMu_Jet10UCountFilter)
