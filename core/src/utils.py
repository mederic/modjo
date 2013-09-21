import re

def get_standard_types():
    return ['date', 'string', 'float', 'int', 'long', 'double', 'char']

def is_a_list(data_type):
    reg = re.compile('[a-zA-Z]+\[\]')
    return reg.match(data_type)

def is_a_map(data_type):
    reg = re.compile('[a-zA-Z]+\[[a-zA-Z]+\]')
    return reg.match(data_type) 
