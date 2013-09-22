import xml.etree.ElementTree as ET

from core.src.error import *
from core.src import utils
class TemplateDefinition:

    def __init__(self, folderPath):
        self.folderPath = folderPath
        try:
            tree = ET.parse(folderPath + "/modjoManifest.xml")
            root = tree.getroot()

            self.equivalences = Equivalences(root.find('equivalences'))

            templates_root = root.find('templates')

            self.subtemplates = []
            for xml_subtemplate in templates_root.iter('template'):
                self.subtemplates.append(Template(xml_subtemplate, self))

            if not self.subtemplates:
                raise ModjoSyntaxError("No templates found.")
        except ET.ParseError:
            raise ModjoTemplateError("Incorrect modjoManifest.xml.")
        except IOError:
            raise ModjoTemplateError("No modjoManifest.xml found.")
        except AttributeError:
            raise ModjoSyntaxError("No templates  attribute found.")


class Equivalences:

    def __init__(self, xml_equivalences):
        self.equivalences = {}
        if not xml_equivalences is None:
            for xml_equivalence in xml_equivalences.iter('equivalence'):
                equivalence_name = xml_equivalence.get('name')
                self.equivalences[equivalence_name] = Equivalence(xml_equivalence)

    def convert(self, target, dataType):
        equivalence = self.equivalences[target]
        if equivalence is None:
            raise ModjoTemplateError("Unspecified equivalence : " + target)

        if (equivalence.equivalence_dict.has_key(dataType)):
            return equivalence.equivalence_dict[dataType]
        else:
            if utils.is_a_list(dataType):
                list_target = equivalence.list_equivalence_target
                if list_target is None:
                    list_target = target

                baseType = dataType.split('[')[0];
                result = equivalence.list_equivalence
                result = result.replace("type", self.convert(list_target, baseType))
                return result
            elif utils.is_a_map(dataType):
                map_target = equivalence.map_equivalence_target
                if map_target is None:
                    map_target = target

                baseType = dataType.split('[')[0];
                keyType = dataType.replace(baseType, '')
                keyType = keyType.replace('[', '')
                keyType = keyType.replace(']', '')

                result = equivalence.map_equivalence
                result = result.replace("key", self.convert(map_target, keyType))
                result = result.replace("value", self.convert(map_target, baseType))
                return result
            else:
                result = equivalence.model_equivalence
                result = result.replace("Model", dataType.capitalize())
                result = result.replace("model", dataType)
                return result


class Equivalence:

    def __init__(self, xml_equivalence):
        self.equivalence_dict = {}
        for base_type in utils.get_standard_types():
            self.equivalence_dict[base_type] = xml_equivalence.find(base_type).text
            if self.equivalence_dict[base_type] is None:
                raise ModjoTemplateError("Unspecified equivalence for " + base_type)

        self.model_equivalence = xml_equivalence.find('model').text
        if self.model_equivalence is None:
            raise ModjoTemplateError("Unspecified equivalence for model")

        list_node = xml_equivalence.find('list');
        self.list_equivalence = list_node.text
        self.list_equivalence_target = list_node.get('equivalence')
        if self.list_equivalence is None:
            raise ModjoTemplateError("Unspecified equivalence for list")

        map_node = xml_equivalence.find('map');
        self.map_equivalence = map_node.text
        self.map_equivalence_target = list_node.get('equivalence')
        if self.map_equivalence is None:
            raise ModjoTemplateError("Unspecified equivalence for map")

class Template:

    def __init__(self, xml_subtemplate, templateDefinition):
        self.target = xml_subtemplate.get('target')
        self.output_dir = xml_subtemplate.get('dir')
        self.templateDefinition = templateDefinition
        self.outputs = []
        for xml_output in xml_subtemplate.iter('output'):
            self.outputs.append(TemplateOutput(xml_output, self))


class TemplateOutput:

    def __init__(self, xml_output, template):
        self.template = template
        folder = template.templateDefinition.folderPath
        self.name = xml_output.get('name')

        self.output_dir = template.output_dir
        if self.output_dir is None:
            self.output_dir = str()

        sub_dir = xml_output.get('dir')
        if not sub_dir is None:
            self.output_dir += "/" + sub_dir

        self.src = folder + "/" + xml_output.get('src')
        self.equivalences = self.template.templateDefinition.equivalences
