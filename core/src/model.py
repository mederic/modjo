import xml.etree.ElementTree as ET

from core.src.error import *
from core.src import utils

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

            self.check_properties()

        except ET.ParseError:
            raise XMLParseError(filePath)
        except AttributeError:
            raise ModjoSyntaxError("No models attribute found.")

    def check_properties(self):
        model_names = []
        models = {}
        for model in self.models:
            model_names.append(model.name)
            models[model.name] = model

        standard_types = utils.get_standard_types()

        base_types = model_names + standard_types
        available_types = model_names + standard_types
        for data_type in base_types:
            available_types.append(data_type + '[]')
            for second_data_type in base_types:
                available_types.append(data_type + '[' + second_data_type + ']')

        for model in self.models:
            for model_property in model.properties:
                if not model_property.dataType in available_types:
                    msg =  'Invalid property type : ' + model_property.dataType + '.'
                    raise ModjoSyntaxError(msg)
                elif model_property.dataType in model_names:
                    model.depending_models.add(models[model_property.dataType])

class Model:

    def __init__(self, xml_model):
        self.name = xml_model.get('name')
        self.Name = self.name.capitalize();
        if self.name is None:
            raise ModjoSyntaxError("Model defined without a name.")
        self.properties = []
        self.depending_models = set()
        for xml_property in xml_model.iter('property'):
            self.properties.append(Property(xml_property))


class Property:

    def __init__(self, xml_property):
        self.name = xml_property.get('name')
        self.Name = self.name.capitalize();
        if self.name is None:
            raise ModjoSyntaxError("Property defined without a name.")

        self.dataType = xml_property.get('type')
        if self.dataType is None:
            raise ModjoSyntaxError("Property defined without a type.")

