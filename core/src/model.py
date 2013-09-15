import xml.etree.ElementTree as ET

from core.src.error import *

class ModelDefinition:

    def __init__(self, filePath):
        self.filePath = filePath
        try:
            tree = ET.parse(filePath)
            root = tree.getroot()
            models_root = root.find('models')

            self.models = []
            for xml_model in models_root.iter('model'):
                self.models.append(Model(xml_model))

            if not self.models:
                raise ModjoSyntaxError("No model found.")
        except ET.ParseError:
            raise XMLParseError(filePath)
        except AttributeError:
            raise ModjoSyntaxError("No models attribute found.")


class Model:

    def __init__(self, xml_model):
        self.name = xml_model.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Model defined without a name.")
        self.properties = []
        for xml_property in xml_model.iter('property'):
            self.properties.append(Property(xml_property))


class Property:

    def __init__(self, xml_property):
        self.name = xml_property.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Property defined without a name.")

        self.dataType = xml_property.get('type')
        if self.dataType is None:
            raise ModjoSyntaxError("Property defined without a type.")

