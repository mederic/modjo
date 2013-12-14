#! /usr/bin/python

import argparse
import sys
from core.src import model
from core.src import template
from core.src import generator
from core.src.downloader import *

from core.src.error import *



print("\n\
                      _  _       \n\
      /\/\   ___   __| |(_) ___  \n\
     /    \ / _ \ / _` || |/ _ \ \n\
    / /\/\ \ (_) | (_| || | (_) |\n\
    \/    \/\___/ \__,_|/ |\___/ \n\
                       |__/      \n");

print("");
print("Version 1.0")
print("----------------------------------------------------");

parser = argparse.ArgumentParser(description='Modjo - model generator')
parser.add_argument('-m', '--model', action="store", dest="modelPath", default=None, help='path to the file describing the model')
parser.add_argument('-t', '--template', action="store", dest="templatePath", default=None, help='path to the folder container files describing the template')
parser.add_argument('-o', '--output', action="store", dest="outputPath",
default='modjoResult', help='path to the directory where result file(s) will be created')

args = parser.parse_args()

# TODO read modjo.cfg
# check if valid

if not args.checkMode:
    if args.modelPath is None:
        print("Path to the model is missing (option -m)")
        sys.exit(2)
    if args.templatePath is None:
        print("Path to the template is missing (option -t)")
        sys.exit(2)

modelDefinition = None
templateDefinition = None
 
if not args.modelPath is None:
    try:
        modelDefinition = model.ModelDefinition(args.modelPath)
    except ModjoSyntaxError as modjoSynError:
        print "Incorrect model file: " + modjoSynError.reason
    except IOError:
        print "File does not exist..."
    except model.XMLParseError:
        print "File specified in " + args.modelPath + " is not a valid xml file."

if not args.templatePath is None:
    try:
        downloader = TemplateDownloader(args.templatePath)
        local_path = downloader.getLocalPath()
        templateDefinition = template.TemplateDefinition(local_path)
    except ModjoSyntaxError as modjoSynError:
        print "Incorrect template: " + modjoSynError.reason

if not modelDefinition is None and not templateDefinition is None:
    if templateDefinition.has_inputs():
        print "This template needs some inputs..."
        for input_key in templateDefinition.get_input_keys():
            value = raw_input(input_key + ":\n")
            templateDefinition.put_input(input_key, value)

    fileGenerator = generator.Generator(modelDefinition, templateDefinition)
    fileGenerator.writeToDest(args.outputPath)

if args.checkMode:
    print "Files have been successfully checked!"
else:
    print "File(s) successfully created in \"" + args.outputPath + "\"!"
