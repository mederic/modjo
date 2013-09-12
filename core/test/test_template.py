import unittest
from core.src.template import *
from core.src import error

class SimpleTemplateTestCase(unittest.TestCase):

    def testSimpleTemplate(self):
        templateDefinition = TemplateDefinition("fixtures/template/ok/simpleTemplate")
        self.assertEqual(len(templateDefinition.subtemplates), 1)

        subtemplate = templateDefinition.subtemplates[0]
        self.assertEqual(subtemplate.target, "model")

        self.assertEqual(len(subtemplate.outputs), 1)
        template_output = subtemplate.outputs[0]

        self.assertEqual(template_output.src, "model.tmpl.txt")
        self.assertEqual(template_output.name, "{{model}}.txt")
