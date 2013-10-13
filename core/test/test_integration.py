import os
import shutil
import unittest
import difflib
import xml.etree.ElementTree as ET
from core.test.utils import *
from core.src.model import *
from core.src.template import *
from core.src.generator import *

class IntegrationTestCase(unittest.TestCase):

    REF_FOLDER_PATH = os.getcwd() + '/fixtures/references/'
    MODELS_FOLDER_PATH = os.getcwd() + '/fixtures/model/ok/'
    TEMPLATES_FOLDER_PATH = os.getcwd() + '/fixtures/template/ok/'
    TARGET_FOLDER_PATH = os.getcwd() + '/.integration_test_result'

    def testAllReferences(self):
        for first_level in os.listdir(self.REF_FOLDER_PATH):
            for second_level in os.listdir(self.REF_FOLDER_PATH + first_level):
                self.delete(self.TARGET_FOLDER_PATH)

                self.current_folder = self.REF_FOLDER_PATH + first_level + "/" + second_level
                manifest = ET.parse(self.current_folder + "/referenceManifest.xml").getroot()
                model = self.MODELS_FOLDER_PATH + manifest.find('model').text
                template = self.TEMPLATES_FOLDER_PATH + manifest.find('template').text
                self.result_creation(model, template)
                self.folder_diff(self.TARGET_FOLDER_PATH, self.current_folder + '/result')

        self.delete(self.TARGET_FOLDER_PATH)

    def folder_diff(self, candidate, reference):
        for file_name in os.listdir(reference):
            if not os.path.exists(candidate + '/' + file_name):
                self.custom_fail(file_name + ' is missing!')

            if os.path.isdir(reference + '/' + file_name):
                self.folder_diff(candidate + '/' + file_name, reference + '/' + file_name)
            else:
                self.file_diff(candidate + '/' + file_name, reference + '/' + file_name)

        for file_name in os.listdir(candidate):
            if not os.path.exists(reference + '/' + file_name):
                self.custom_fail(file_name + ' is an extra file!')

    def file_diff(self, candidate, reference):
        candidate_file = open(candidate, 'r').read()
        reference_file = open(reference, 'r').read()
        diff = difflib.SequenceMatcher(None, candidate_file, reference_file)

        op_codes = diff.get_opcodes()
        if op_codes:
            for opcode in op_codes:
                if opcode[0] != 'equal':
                    msg = opcode[0]
                    msg += " : "
                    msg += candidate_file[opcode[1]:opcode[2]]
                    msg += " to "
                    msg += reference_file[opcode[3]:opcode[4]]
                    self.custom_fail(candidate + '\n' + msg)

    def custom_fail(self, msg):
        final_msg = self.current_folder
        final_msg += ' : '
        final_msg += '\n-------------------------------\n'
        final_msg += msg
        self.fail(final_msg)

    def delete(self, path):
        if os.path.exists(path):
            shutil.rmtree(path)


    def result_creation(self, model, template):
        model_definition = ModelDefinition(model)
        template_definition = TemplateDefinition(template)
        fill_with_default_values(template_definition)
        file_generator = Generator(model_definition, template_definition)
        file_generator.writeToDest(self.TARGET_FOLDER_PATH)


