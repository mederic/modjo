#! /usr/bin/python

import argparse
import sys
from core.src import model
from core.src import template
from core.src import generator

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
parser.add_argument('-d', '--debug', action="store_true", dest="debug", help='print debug informations')
parser.add_argument('-c', '--check', action="store_true", dest="checkMode", help='validate (or not) a template and/or a model')

args = parser.parse_args()

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
        templateDefinition = template.TemplateDefinition(args.templatePath)
    except ModjoSyntaxError as modjoSynError:
        print "Incorrect template: " + modjoSynError.reason

if not modelDefinition is None and not templateDefinition is None:
    fileGenerator = generator.Generator(modelDefinition, templateDefinition)
    fileGenerator.writeToDest(args.outputPath)

