import unittest
from core.src.model import *
from core.src import error

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


class WrongModelTestCase(unittest.TestCase):

    def testUnexistingFileModel(self):
    	with self.assertRaises(IOError):
            try:
                modelDefinition = ModelDefinition("path/to/unexisting/model/file")
                self.fail("Fixture file seems to exist...")
            except XMLParseError:
                self.fail("Unexpected exception when parsing model")
            
    def testWrongXmlModel(self):    
    	with self.assertRaises(XMLParseError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/wrongXml.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")
            
    def testWithoutRootNodeModel(self):    
    	with self.assertRaises(XMLParseError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/xmlWithoutRootNode.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")
            
    def testWithoutModelsNodeModel(self):    
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/xmlWithoutModelsNode.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")
            
    def testWithoutModelsModel(self):
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/xmlWithoutModels.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")
                
    def testModelWithoutNameModel(self):
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/xmlModelWithoutName.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")
                
    def testPropertyWithoutTypeModel(self):
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/xmlPropertyWithoutType.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")

    def testPropertyWithoutNameModel(self):
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/xmlPropertyWithoutName.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")