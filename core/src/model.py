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
            webservices_root = root.find('webservices')

            self.models = []
            for xml_model in models_root.iter('model'):
                self.models.append(Model(xml_model))

            self.webservices = []
            if not webservices_root is None:
                for xml_webservice in webservices_root.iter('webservice'):
                    self.webservices.append(Webservice(xml_webservice))

            if not self.models:
                raise ModjoSyntaxError("No model found.")

            self.check_types()

        except ET.ParseError:
            raise XMLParseError(filePath)
        except AttributeError:
            raise ModjoSyntaxError("No models attribute found.")

    def check_types(self):
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

        for service in self.webservices:
            if not service.result in available_types:
                msg =  'Invalid webservice result type : ' + service.result + '.'
                raise ModjoSyntaxError(msg)
            elif service.result in model_names:
                service.depending_models.add(models[service.result])
            for parameter in service.parameters:
                if not parameter.dataType in available_types:
                    msg =  'Invalid webservice parameter type : ' + parameter.dataType + '.'
                    raise ModjoSyntaxError(msg)
                elif parameter.dataType in model_names:
                    service.depending_models.add(models[parameter.dataType])

class Model:

    def __init__(self, xml_model):
        self.name = xml_model.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Model defined without a name.")
        self.Name = self.name.capitalize();

        self.properties = []
        self.depending_models = set()
        for xml_property in xml_model.iter('property'):
            self.properties.append(Property(xml_property))


class Property:

    def __init__(self, xml_property):
        self.name = xml_property.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Property defined without a name.")
        self.Name = self.name.capitalize();

        self.dataType = xml_property.get('type')
        if self.dataType is None:
            raise ModjoSyntaxError("Property defined without a type.")


class Webservice:

    def __init__(self, xml_webservice):
        self.name = xml_webservice.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Webservice defined without a name.")
        self.Name = self.name.capitalize();

        self.method = xml_webservice.find('method').text
        self.path = xml_webservice.find('path').text
        self.result = xml_webservice.find('result').text

        self.depending_models = set()

        if self.method is None:
            raise ModjoSyntaxError("Webservice defined without a http method.")

        if self.path is None:
            raise ModjoSyntaxError("Webservice defined without a http path.")

        if self.result is None:
            raise ModjoSyntaxError("Webservice defined without a return type.")

        self.parameters = []
        xml_parameters = xml_webservice.find('parameters')
        if not xml_parameters is None:
            for xml_parameter in xml_parameters.iter('parameter'):
                self.parameters.append(Parameter(xml_parameter))


class Parameter:

    def __init__(self, xml_parameter):
        self.name = xml_parameter.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Webservice parameter defined without a name.")
        self.Name = self.name.capitalize();

        self.dataType = xml_parameter.get('type')
        if self.dataType is None:
            raise ModjoSyntaxError("Webservice parameter defined without a type.")
