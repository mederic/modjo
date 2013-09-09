#! /usr/bin/python

import argparse
import sys
from core import model


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
parser.add_argument('-t', '--template', action="store", dest="templatePath", default=None, help='path to the file describing the templat')
parser.add_argument('-o', '--output', action="store", dest="outputPath", default=None, help='path to the directory where result file(s) will be created')
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


if not args.modelPath is None:
    try:
        modelDefinition = model.ModelDefinition(args.modelPath)
    except model.XMLParseError:
        print "File specified in " + modelPath + " is not a valid xml file." 
