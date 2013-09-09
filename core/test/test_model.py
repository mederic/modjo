import unittest
from core.src.model import *

class SimpleModelTestCase(unittest.TestCase):

    def testSimpleModel(self):
        try:
            modelDefinition = ModelDefinition("fixtures/model/ok/simpleModel.xml")
            self.assertEqual(len(modelDefinition.models), 1)

            locationModel = modelDefinition.models[0]
            self.assertEqual(locationModel.name, "location")
            self.assertEqual(len(locationModel.properties), 2)

            latitudeProperty = locationModel.properties[0]
            longitudeProperty = locationModel.properties[1]

            self.assertEqual(latitudeProperty.dataType, "double")
            self.assertEqual(latitudeProperty.name, "latitude")

            self.assertEqual(longitudeProperty.dataType, "double")
            self.assertEqual(longitudeProperty.name, "longitude")
        except IOError:
            self.fail("Fixture file does not exist...")
        except XMLParseError:
            self.fail("Unexpected exception when parsing model")

