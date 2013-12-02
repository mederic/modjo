import os

from abc import ABCMeta, abstractmethod
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
                    self.outputs.append(ModelOutput(output, model, template))
            elif (template.target == 'webservice'):
                for webservice in modelDefinition.webservices:
                    self.outputs.append(WebserviceOutput(output, webservice, template))
            elif (template.target == 'models'):
                self.outputs.append(ModelsOutput(output, modelDefinition.models, template))
            elif (template.target == 'webservices'):
                self.outputs.append(WebservicesOutput(output, modelDefinition.webservices, template))
            else:
                self.outputs.append(StandardOutput(output, template))


class AbstractOutput:
    __metaclass__ = ABCMeta

    def __init__(self, output):  
        self.output = output
        self.create()
    
    @abstractmethod
    def getFilenameParams(self):
        pass
        
    @abstractmethod
    def getFileParams(self):
        pass
        
    def create(self): 
        name_tpl = SimpleTemplate(self.output.name)        
        filename = name_tpl.render(self.getFilenameParams())
        
        tpl_file = open(self.output.src, 'r')
        content_tpl = SimpleTemplate(tpl_file)
        content = content_tpl.render(self.getFileParams())
        tpl_file.close()
        
        output_dir = None
        if not self.output.output_dir is None and not self.output.output_dir == '':
            output_dir_tpl = SimpleTemplate(self.output.output_dir)
            output_dir = output_dir_tpl.render(self.getFilenameParams())
            
        self.output_dir = output_dir            
        self.name = filename
        self.content = content        


class StandardOutput(AbstractOutput):
    
    def __init__(self, output, template):
        self.template = template
        AbstractOutput.__init__(self, output)

    def getFilenameParams(self):
        return dict(inputs=self.template.templateDefinition.inputs)
        
    def getFileParams(self):
        return dict(inputs=self.template.templateDefinition.inputs)
     
     
class ModelOutput(AbstractOutput):
    
    def __init__(self, output, model, template):
        self.template = template
        self.model = model
        AbstractOutput.__init__(self, output)

    def getFilenameParams(self):
        return dict(model=self.model.name, Model=self.model.Name, MODEL=self.model.NAME, group=self.model.group, Group=self.model.Group, GROUP=self.model.GROUP, inputs=self.template.templateDefinition.inputs)
        
    def getFileParams(self):
        return dict(model=self.model, equ=self.output.equivalences, inputs=self.template.templateDefinition.inputs)
        
        
class ModelsOutput(AbstractOutput):

    def __init__(self, output, models, template):
        self.template = template
        self.models = models
        AbstractOutput.__init__(self, output)

    def getFilenameParams(self):
        return dict(inputs=self.template.templateDefinition.inputs)
        
    def getFileParams(self):
        return dict(models=self.models, equ=self.output.equivalences, inputs=self.template.templateDefinition.inputs)

           
class WebserviceOutput(AbstractOutput):
    
    def __init__(self, output, webservice, template):
        self.template = template
        self.webservice = webservice
        AbstractOutput.__init__(self, output)

    def getFilenameParams(self):
        return dict(webservice=self.webservice.name, Webservice=self.webservice.Name, WEBSERVICE=self.webservice.NAME, group=self.webservice.group, Group=self.webservice.Group, GROUP=self.webservice.GROUP, inputs=self.template.templateDefinition.inputs)
        
    def getFileParams(self):
        return dict(webservice=self.webservice, equ=self.output.equivalences, inputs=self.template.templateDefinition.inputs)
        
           
class WebservicesOutput(AbstractOutput):
    
    def __init__(self, output, webservices, template):
        self.template = template
        self.webservices = webservices
        AbstractOutput.__init__(self, output)

    def getFilenameParams(self):
        return dict(inputs=self.template.templateDefinition.inputs)
        
    def getFileParams(self):
        return dict(webservices=self.webservices, equ=self.output.equivalences, inputs=self.template.templateDefinition.inputs)
        
