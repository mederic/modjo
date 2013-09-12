import xml.etree.ElementTree as ET

from core.src.error import *

class TemplateDefinition:

    def __init__(self, folderPath):
        self.folderPath = folderPath
        try:
            tree = ET.parse(folderPath + "/modjoManifest.xml")
            root = tree.getroot()
            templates_root = root.find('templates')

            self.subtemplates= []
            for xml_subtemplate in templates_root.iter('template'):
                self.subtemplates.append(Template(xml_subtemplate))

            if not self.subtemplates:
                raise ModjoSyntaxError("No templates found.")
        except ET.ParseError:
            raise XMLParseError(filePath)
        except IOError:
            raise ModjoTemplateError("No modjoManifest.xml found.")
        except AttributeError:
            raise ModjoSyntaxError("No templates  attribute found.")


class Template:

    def __init__(self, xml_subtemplate):
        self.target = xml_subtemplate.get('target') 

        self.outputs = []
        for xml_output in xml_subtemplate.iter('output'):
            self.outputs.append(TemplateOutput(xml_output))


class TemplateOutput:

    def __init__(self, xml_output):
        self.name = xml_output.get('name')
        self.src= xml_output.get('src')

