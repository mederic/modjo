import xml.etree.ElementTree as ET

from core.src.error import *
from core.src import utils
from core.src.OrderedSet import *

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
        except AttributeError as attr_error:
            raise ModjoSyntaxError(str(attr_error))

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
                elif utils.is_a_list(model_property.dataType):
                    model.has_list = True
                    baseType = model_property.dataType.split('[')[0];
                    if baseType in model_names:
                        model.depending_models.add(models[baseType])
                elif utils.is_a_map(model_property.dataType):
                    model.has_map = True
                    baseType = model_property.dataType.split('[')[0];
                    keyType = model_property.dataType.replace(baseType, '')
                    keyType = keyType.replace('[', '')
                    keyType = keyType.replace(']', '')
                    if keyType in model_names:
                        model.depending_models.add(models[keyType])
                    if baseType in model_names:
                        model.depending_models.add(models[baseType])

        for service in self.webservices:
            if not service.result in available_types:
                msg =  'Invalid webservice result type : ' + service.result + '.'
                raise ModjoSyntaxError(msg)
            elif service.result in model_names:
                service.depending_models.add(models[service.result])
            elif utils.is_a_list(service.result):
                service.has_list = True
                baseType = service.result.split('[')[0];
                if baseType in model_names:
                    service.depending_models.add(models[baseType])
            elif utils.is_a_map(service.result):
                service.has_map = True
                baseType = service.result.split('[')[0];
                keyType = service.result.replace(baseType, '')
                keyType = keyType.replace('[', '')
                keyType = keyType.replace(']', '')
                if keyType in model_names:
                    service.depending_models.add(models[keyType])
                if baseType in model_names:
                    service.depending_models.add(models[baseType])
            for parameter in service.parameters:
                if not parameter.dataType in available_types:
                    msg =  'Invalid webservice parameter type : ' + parameter.dataType + '.'
                    raise ModjoSyntaxError(msg)
                elif parameter.dataType in model_names:
                    service.depending_models.add(models[parameter.dataType])
                elif utils.is_a_list(parameter.dataType):
                    service.has_list = True
                    baseType = parameter.dataType.split('[')[0];
                    if baseType in model_names:
                        service.depending_models.add(models[baseType])
                elif utils.is_a_map(parameter.dataType):
                    service.has_map = True
                    baseType = parameter.dataType.split('[')[0];
                    keyType = parameter.dataType.replace(baseType, '')
                    keyType = keyType.replace('[', '')
                    keyType = keyType.replace(']', '')
                    if keyType in model_names:
                        service.depending_models.add(models[keyType])
                    if baseType in model_names:
                        service.depending_models.add(models[baseType])

class Model:

    def __init__(self, xml_model):
        self.name = xml_model.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Model defined without a name.")
        self.Name = self.name[0].upper() + self.name[1:]
        self.NAME = self.name.upper()

        self.has_list = False
        self.has_map = False

        self.properties = []
        self.depending_models = OrderedSet()
        for xml_property in xml_model.iter('property'):
            self.properties.append(Property(xml_property))


class Property:

    def __init__(self, xml_property):
        self.name = xml_property.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Property defined without a name.")
        self.Name = self.name[0].upper() + self.name[1:]
        self.NAME = self.name.upper()

        self.dataType = xml_property.get('type')
        if self.dataType is None:
            raise ModjoSyntaxError("Property defined without a type.")


class Webservice:

    def __init__(self, xml_webservice):
        self.name = xml_webservice.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Webservice defined without a name.")
        self.Name = self.name[0].upper() + self.name[1:]
        self.NAME = self.name.upper()

        self.has_list = False
        self.has_map = False

        self.method = None
        self.result = None
        if not xml_webservice.find('method') is None:
            self.method = xml_webservice.find('method').text
        if not xml_webservice.find('result') is None:
            self.result = xml_webservice.find('result').text

        self.depending_models = OrderedSet()

        if self.method is None:
            raise ModjoSyntaxError("Webservice defined without a http method.")
        self.Method = self.method[0].upper() + self.method[1:]
        self.METHOD = self.method.upper()

        if self.result is None:
            raise ModjoSyntaxError("Webservice defined without a return type.")

        self.parameters = []
        xml_parameters = xml_webservice.find('parameters')
        if not xml_parameters is None:
            for xml_parameter in xml_parameters.iter('parameter'):
                self.parameters.append(Parameter(xml_parameter))
                
        if xml_webservice.find('path') is None:
            raise ModjoSyntaxError("Webservice defined without a http path.")
        else:
            path = xml_webservice.find('path').text
            self.path = Path(path, self)


class Path:

    def __init__(self, raw_path, webservice):
        self.entries = []
        for entry in raw_path.split('/'):
            if len(entry) > 0:
                self.entries.append(PathEntry(entry, webservice))
            
    def contains_parameter(self):
        for entry in self.entries:
            if entry.is_parameter:
                return True
        return False
        
    def __repr__(self):
        return self.__str__()
        
    def __str__(self):
        final_str = ''
        for entry in self.entries:
            final_str += '/' + entry.name
        return final_str


class PathEntry:

    def __init__(self, raw_entry, webservice):
        if raw_entry.startswith('{{') and raw_entry.endswith('}}'):
            self.is_parameter = True
            self.name = raw_entry[2:len(raw_entry) - 2]
            
            existing_parameter = False
            for parameter in webservice.parameters:
                print self.name + ' vs ' + parameter.name
                if self.name == parameter.name:
                    existing_parameter = True
                    parameter.is_in_path = True
                    break
                    
            if not existing_parameter:
                raise ModjoSyntaxError("Webservice http path contains undefined parameter...")               
        else:
            self.is_parameter = False
            self.name = raw_entry
        
        
        self.Name = self.name[0].upper() + self.name[1:]
        self.NAME = self.name.upper()


class Parameter:

    def __init__(self, xml_parameter):
        self.name = xml_parameter.get('name')
        if self.name is None:
            raise ModjoSyntaxError("Webservice parameter defined without a name.")
        self.Name = self.name[0].upper() + self.name[1:]
        self.NAME = self.name.upper()

        self.dataType = xml_parameter.get('type')
        if self.dataType is None:
            raise ModjoSyntaxError("Webservice parameter defined without a type.")
            
        self.is_in_path = False
