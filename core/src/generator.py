import os

from core.src.error import *
from core.src.model import *
from core.src.template import *

from core.lib.bottle import SimpleTemplate

class Generator:

    def __init__(self, modelDefinition, templateDefinition):
        self.template_generator = []
        for template in templateDefinition.subtemplates:
            templateGenerator = TemplateGenerator(template, modelDefinition)
            self.template_generator.append(templateGenerator)

    def writeToDest(self, dest):

        if not os.path.exists(dest):
            os.makedirs(dest)

        for sub_generator in self.template_generator:
            for output in sub_generator.outputs:
                output_dest = dest + "/" 
                if not output.output_dir is None:
                   output_dest += output.output_dir + "/"
                   if not os.path.exists(output_dest):
                        os.makedirs(output_dest)

                output_dest += output.name
                f = open(output_dest, 'w')
                f.write(output.content)
                f.close()

class TemplateGenerator:

    def __init__(self, template, modelDefinition):
        self.outputs = []
        for output in template.outputs:
            if (template.target == 'model'):
                for model in modelDefinition.models:
                    self.outputs.append(ModelOutput(output, model))
            elif (template.target == 'webservice'):
                for webservice in modelDefinition.webservices:
                    self.outputs.append(WebserviceOutput(output, webservice))
            else:
                    self.outputs.append(StandardOutput(output))

class StandardOutput:

    def __init__(self, output):
        name_tpl = SimpleTemplate(output.name)
        filename = name_tpl.render()

        tpl_file = open(output.src, 'r')
        content_tpl = SimpleTemplate(tpl_file)
        content = content_tpl.render()
        tpl_file.close()

        output_dir_tpl = SimpleTemplate(output.output_dir)
        output_dir = output_dir_tpl.render()

        self.output_dir = output_dir
        self.name = filename
        self.content = content


class ModelOutput:

    def __init__(self, output, model):
        name_tpl = SimpleTemplate(output.name)
        filename = name_tpl.render(model=model.name, Model=model.Name, MODEL=model.NAME)

        tpl_file = open(output.src, 'r')
        content_tpl = SimpleTemplate(tpl_file)
        content = content_tpl.render(model=model,equ=output.equivalences)
        tpl_file.close()

        output_dir_tpl = SimpleTemplate(output.output_dir)
        output_dir = output_dir_tpl.render(model=model.name, Model=model.Name, MODEL=model.NAME)

        self.output_dir = output_dir
        self.name = filename
        self.content = content


class WebserviceOutput:

    def __init__(self, output, webservice):
        name_tpl = SimpleTemplate(output.name)
        filename = name_tpl.render(webservice=webservice.name, Webservice=webservice.Name, WEBSERVICE=webservice.NAME)

        tpl_file = open(output.src, 'r')
        content_tpl = SimpleTemplate(tpl_file)
        content = content_tpl.render(webservice=webservice,equ=output.equivalences)
        tpl_file.close()

        output_dir_tpl = SimpleTemplate(output.output_dir)
        output_dir = output_dir_tpl.render(webservice=webservice.name, Webservice=webservice.Name, WEBSERVICE=webservice.NAME)

        self.output_dir = output_dir
        self.name = filename
        self.content = content
