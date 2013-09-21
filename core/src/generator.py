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
                output_dest = dest + "/" + output.name
                f = open(output_dest, 'w')
                f.write(output.content)
                f.close()

class TemplateGenerator:

    def __init__(self, template, modelDefinition):
        self.outputs = []
        if (template.target == 'model'):
            for model in modelDefinition.models:
                for output in template.outputs:
                    self.outputs.append(ModelOutput(output, model))


class ModelOutput:

    def __init__(self, output, model):
        name_tpl = SimpleTemplate(output.name)
        filename = name_tpl.render(model=model.name, Model=model.Name)

        tpl_file = open(output.src, 'r')
        content_tpl = SimpleTemplate(tpl_file)
        content = content_tpl.render(model=model,equ=output.equivalences)
        tpl_file.close()

        self.name = filename
        self.content = content
