# Unit test configuration file for MessageLogger service:
# statistics destination :  tests reset versus no reset
# behavior when multiple statistics summaries are triggered

import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

import FWCore.Framework.test.cmsExceptionsFatal_cff
process.options = FWCore.Framework.test.cmsExceptionsFatal_cff.options

process.load("FWCore.MessageService.test.Services_cff")

process.MessageLogger = cms.Service("MessageLogger",
    u5_errors = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR'),
        noTimeStamps = cms.untracked.bool(True),
        preEventProcessing = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    ),
    categories = cms.untracked.vstring('preEventProcessing'),
    u5_default = cms.untracked.PSet(
        enableStatistics = cms.untracked.bool(True),
        default = cms.untracked.PSet(
          limit = cms.untracked.int32(0)
        )
    ),
    u5_noreset = cms.untracked.PSet(
        resetStatistics = cms.untracked.bool(False),
        enableStatistics = cms.untracked.bool(True),
        default = cms.untracked.PSet(
          limit = cms.untracked.int32(0)
        )
    ),
    u5_reset = cms.untracked.PSet(
        resetStatistics = cms.untracked.bool(True),
        enableStatistics = cms.untracked.bool(True),
        default = cms.untracked.PSet(
          limit = cms.untracked.int32(0)
        )
    ),
    destinations = cms.untracked.vstring('u5_errors', 'u5_reset', 'u5_noreset', 'u5_default')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(3)
)

process.source = cms.Source("EmptySource")

process.sendSomeMessages = cms.EDAnalyzer("UnitTestClient_B")

process.p = cms.Path(process.sendSomeMessages)
