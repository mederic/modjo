#! /usr/bin/python

import os
import datetime 
import shutil
import xml.etree.ElementTree as ET
from core.src.model import *
from core.src.template import *
from core.src.generator import *

def main():
    ref_folder_path = os.getcwd() + '/fixtures/references/'
    models_folder_path = os.getcwd() + '/fixtures/model/ok/'
    templates_folder_path = os.getcwd() + '/fixtures/template/ok/'

    # main references folder creation...
    if os.path.exists(ref_folder_path):
        print 'References folder already exist!'
        overwrite = raw_input('Overwrite ? [Y/n]')
        if overwrite.lower() == 'y':
            shutil.rmtree(ref_folder_path)
        else:
            return

    os.mkdir(ref_folder_path)
    print 'Main folder created'

    # model fixtures loop
    for model in os.listdir(models_folder_path):
        if model.endswith('.xml'):
            print model + ':'
            model_definition = ModelDefinition(models_folder_path + model)
            for template in os.listdir(templates_folder_path):
                print '    -> ' + template
                template_definition = TemplateDefinition(templates_folder_path + template)
                if template_definition.has_inputs():
                    for input_key in template_definition.get_input_keys():
                        value = input_key + "_default_value"
                        template_definition.put_input(input_key, value)

                file_generator = Generator(model_definition, template_definition)
                current_target_folder = ref_folder_path
                current_target_folder += "/" + os.path.splitext(model)[0]
                current_target_folder += "/" + template 
                file_generator.writeToDest(current_target_folder + "/result")
                create_reference_manifest(model, template, current_target_folder)

def create_reference_manifest(model, template, target_folder):
    root = ET.Element('root')
    date_value = datetime.datetime.now().strftime('%Y/%m/%d - %Hh%M')
    root.set('date', date_value)

    model_elem = ET.SubElement(root, 'model')
    model_elem.text = model

    template_elem = ET.SubElement(root, 'template')
    template_elem.text = template

    xml_tree = ET.ElementTree(element=root)
    xml_tree.write(target_folder + '/referenceManifest.xml')

if __name__ == '__main__':
    main()
