from core.src.template import *

def fill_with_default_values(template_definition):
    if template_definition.has_inputs():
        for input_key in template_definition.get_input_keys():
            value = input_key + "_default_value"
            template_definition.put_input(input_key, value)
