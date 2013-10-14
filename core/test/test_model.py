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

            self.assertEquals(len(locationModel.depending_models), 0)
            self.assertFalse(locationModel.has_map)
            self.assertFalse(locationModel.has_list)
        except IOError:
            self.fail("Fixture file does not exist...")
        except XMLParseError:
            self.fail("Unexpected exception when parsing model")

    def testSimpleModelWithList(self):
        try:
            modelDefinition = ModelDefinition("fixtures/model/ok/simpleModelWithList.xml")
            self.assertEqual(len(modelDefinition.models), 3)

            locationModel = modelDefinition.models[2]
            self.assertEqual(locationModel.name, "trips")
            self.assertEqual(len(locationModel.properties), 1)

            locationsProperty = locationModel.properties[0]
            self.assertEqual(locationsProperty.dataType, "trip[]")
            self.assertEqual(locationsProperty.name, "locations")
        except IOError:
            self.fail("Fixture file does not exist...")
        except XMLParseError:
            self.fail("Unexpected exception when parsing model")

    def testSimpleModelWithMap(self):
        try:
            modelDefinition = ModelDefinition("fixtures/model/ok/simpleModelWithMap.xml")
            self.assertEqual(len(modelDefinition.models), 2)

            countryModel = modelDefinition.models[1]
            self.assertEqual(countryModel.name, "country")
            self.assertEqual(len(countryModel.properties), 1)

            citiesProperty = countryModel.properties[0]
            self.assertEqual(citiesProperty.dataType, "location[string]")
            self.assertEqual(citiesProperty.name, "cities")
        except IOError:
            self.fail("Fixture file does not exist...")
        except XMLParseError:
            self.fail("Unexpected exception when parsing model")


class ComplexModelTestCase(unittest.TestCase):

    def testComplexModel(self):
        try:
            modelDefinition = ModelDefinition("fixtures/model/ok/complexModel.xml")
            self.assertEqual(len(modelDefinition.models), 4)

            shopModel = modelDefinition.models[3]
            self.assertEqual(shopModel.name, "shop")
            self.assertEqual(len(shopModel.properties), 2)

            placeProperty = shopModel.properties[0]
            self.assertEqual(placeProperty.dataType, "place")
            self.assertEqual(placeProperty.name, "place")
        except IOError:
            self.fail("Fixture file does not exist...")
        except XMLParseError:
            self.fail("Unexpected exception when parsing model")

    def testDependingModels(self):
        try:
            modelDefinition = ModelDefinition("fixtures/model/ok/complexModelFullDependancies.xml")

            model1 = modelDefinition.models[0]
            self.assertEquals(model1.name, "model0")
            self.assertTrue(model1.has_map)
            self.assertTrue(model1.has_list)
            self.assertEquals(len(model1.depending_models), 4)
            depends = []
            for model in model1.depending_models:
                depends.append(model.name)
            self.assertTrue("model1" in depends)
            self.assertTrue("model2" in depends)
            self.assertTrue("model3" in depends)
            self.assertTrue("model4" in depends)

            ws1 = modelDefinition.webservices[0]
            self.assertEquals(ws1.name, "ws1")
            self.assertEquals(len(ws1.depending_models), 5)
            self.assertTrue(ws1.has_map)
            self.assertTrue(ws1.has_list)
            depends = []
            for model in ws1.depending_models:
                depends.append(model.name)
            self.assertTrue("model1" in depends)
            self.assertTrue("model2" in depends)
            self.assertTrue("model3" in depends)
            self.assertTrue("model4" in depends)
            self.assertTrue("model5" in depends)

            ws1 = modelDefinition.webservices[1]
            self.assertEquals(ws1.name, "ws2")
            self.assertEquals(len(ws1.depending_models), 5)
            self.assertTrue(ws1.has_map)
            self.assertTrue(ws1.has_list)
            depends = []
            for model in ws1.depending_models:
                depends.append(model.name)
            self.assertTrue("model1" in depends)
            self.assertTrue("model2" in depends)
            self.assertTrue("model3" in depends)
            self.assertTrue("model4" in depends)
            self.assertTrue("model5" in depends)

            ws1 = modelDefinition.webservices[2]
            self.assertEquals(ws1.name, "ws3")
            self.assertEquals(len(ws1.depending_models), 6)
            self.assertTrue(ws1.has_map)
            self.assertTrue(ws1.has_list)
            depends = []
            for model in ws1.depending_models:
                depends.append(model.name)
            self.assertTrue("model1" in depends)
            self.assertTrue("model2" in depends)
            self.assertTrue("model3" in depends)
            self.assertTrue("model4" in depends)
            self.assertTrue("model5" in depends)
            self.assertTrue("model6" in depends)

        except IOError:
            self.fail("Fixture file does not exist...")
        except XMLParseError:
            self.fail("Unexpected exception when parsing model")

    def testComplexModelAndServices(self):
        try:
            modelDefinition = ModelDefinition("fixtures/model/ok/complexModelAndServices.xml")
            self.assertEqual(len(modelDefinition.webservices), 3)

            getListShopService = modelDefinition.webservices[0]
            self.assertEqual(getListShopService.name, "getListShop")
            self.assertEqual(getListShopService.method, "get")
            self.assertEqual(len(getListShopService.path.entries), 1)
            self.assertEqual(getListShopService.path.entries[0].name, "shop")
            self.assertEqual(getListShopService.result, "shop[]")
            self.assertEqual(len(getListShopService.parameters), 2)

            latParam = getListShopService.parameters[0]
            self.assertEqual(latParam.dataType, "double")
            self.assertEqual(latParam.name, "latitude")

            lonParam = getListShopService.parameters[1]
            self.assertEqual(lonParam.dataType, "double")
            self.assertEqual(lonParam.name, "longitude")

            getAddPersonService = modelDefinition.webservices[1]
            self.assertEqual(getAddPersonService.name, "addPerson")
            self.assertEqual(getAddPersonService.method, "post")
            self.assertEqual(len(getAddPersonService.path.entries), 1)
            self.assertEqual(getAddPersonService.path.contains_parameter(), False)
            self.assertEqual(getAddPersonService.path.entries[0].name, "person")
            self.assertEqual(getAddPersonService.result, "string")
            self.assertEqual(len(getAddPersonService.parameters), 3)

            firstname = getAddPersonService.parameters[0]
            self.assertEqual(firstname.dataType, "string")
            self.assertEqual(firstname.name, "firstname")
            self.assertEqual(firstname.is_in_path, False)

            lastname = getAddPersonService.parameters[1]
            self.assertEqual(lastname.dataType, "string")
            self.assertEqual(lastname.name, "lastname")
            self.assertEqual(lastname.is_in_path, False)

            birthdate = getAddPersonService.parameters[2]
            self.assertEqual(birthdate.dataType, "long")
            self.assertEqual(birthdate.name, "birthdate")
            self.assertEqual(birthdate.is_in_path, False)

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

    def testPropertyWithInvalidTypeModel(self):
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/xmlPropertyInvalidType.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")

    def testServiceWithoutHttpMethod(self):
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/serviceWithoutHttpMethod.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")

    def testServiceWithoutHttpPath(self):
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/serviceWithoutHttpPath.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")

    def testServiceParameterWithoutName(self):
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/serviceParameterWithoutName.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")

    def testServiceParameterWithoutType(self):
    	with self.assertRaises(ModjoSyntaxError):
            try:
                modelDefinition = ModelDefinition("fixtures/model/ko/serviceParameterWithoutType.xml")
                self.fail("Fixture file seems to bo ok...")
            except IOError:
                self.fail("Fixture file does not exist...")
