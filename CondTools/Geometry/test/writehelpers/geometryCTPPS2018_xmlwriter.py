import FWCore.ParameterSet.Config as cms

process = cms.Process("GeometryXMLWriter")

process.load('Geometry.VeryForwardGeometry.geometryRPFromDD_2018_cfi')
from Geometry.VeryForwardGeometry.geometryRPFromDD_2018_cfi import XMLIdealGeometryESSource_CTPPS
process.XMLIdealGeometryESSource = XMLIdealGeometryESSource_CTPPS.clone()

process.source = cms.Source("EmptyIOVSource",
                            lastValue = cms.uint64(1),
                            timetype = cms.string('runnumber'),
                            firstValue = cms.uint64(1),
                            interval = cms.uint64(1)
                            )

process.BigXMLWriter = cms.EDAnalyzer("OutputDDToDDL",
                                      rotNumSeed = cms.int32(0),
                                      fileName = cms.untracked.string("./ge2018SingleBigFile.xml")
                                      )


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
    )

process.p1 = cms.Path(process.BigXMLWriter)

