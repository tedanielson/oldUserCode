import FWCore.ParameterSet.Config as cms

# ==========  CUT ON PRIMARY VERTEX

primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                   vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                   minimumNumberOfTracks = cms.uint32(3) ,
                                   maxAbsZ = cms.double(15),
                                   maxd0 = cms.double(2)
                                   )
