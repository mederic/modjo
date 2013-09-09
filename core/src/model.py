import xml.etree.ElementTree as ET

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
        except ET.ParseError:
            raise XMLParseError(filePath)


class Model:

    def __init__(self, xml_model):
        self.name = xml_model.get('name')
        self.properties = []
        for xml_property in xml_model.iter('property'):
            self.properties.append(Property(xml_property))


class Property:

    def __init__(self, xml_property):
        self.name = xml_property.get('name')
        self.dataType = xml_property.get('type')


class XMLParseError(Exception):

    def __init__(self, filePath):
        self.filePath = filePath

    def __str__(self):
        return filePath + " is not a valid xml file..."
