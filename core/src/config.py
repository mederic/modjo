import os
from core.src.error import *
import ConfigParser

class Config:

    def __init__(self, path):
        config = ConfigParser.ConfigParser()
        config.read(path)

        self.default_output = config.get('general', 'default_output')
        self.template_folder = config.get('general', 'template_folder')

        if self.default_output is None:
            raise ModjoConfigError('missing \'default_output\' in default section...')

        if not os.path.exists(self.template_folder):
            raise ModjoConfigError('template folder \'' + self.template_folder + '\' not exists...')

        self.repos = {}
        for repos in config.items('repos'):
             self.repos[repos[0]] = Repos(repos[0], repos[1])

class Repos:

    def __init__(self, name, uri):
        splitted = uri.split('://', 1)
        if splitted[0] == 'file':
            self.is_local = True
            self.uri = splitted[1]
        elif splitted[0] == 'http' or splitted[0] == 'https':
            self.is_local = False
            self.uri = uri
        else:
            raise ModjoConfigError('invalid value for repos \'' + name + '\'')

        if not self.uri.endswith('/'):
            self.uri += '/'
