#! /usr/local/bin/python3.3

import sys
import getopt
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

def usage():
    print("Usage: modjo -m <model> -t <template> -o <output>")
    print()
    print("Options:")    
    print("   -m | --model     : path to the file describing the model");
    print("   -t | --template  : path to the file describing the template");
    print("   -o | --output    : path to the directory where result file(s) will be created");
    print("   -d | --debug     : print debug informations")
    print("   -c | --check     : validate (or not) a template and/or a model") 

try:
    opts, args = getopt.getopt(sys.argv[1:], "m:t:o:dhc", ["model=", "template=", "output=", "debug", "help", "check"])
except getopt.GetoptError as err:
    print(err) 
    usage()
    sys.exit(2)

modelPath = None
templatePath = None
outputPath = None
debug = False
checkMode = False

for o, a in opts:
    if o in ("-m", "--model"):
        modelPath = a
    elif o in ("-t", "--template"):
        templatePath = a
    elif o in ("-o", "--output"):
        outputPath = a
    elif o in ("-debug", "--debug"):
        debug = True
    elif o in ("-c", "--check"):
        checkMode = True
    elif o in ("-h", "--help"):
        usage()
        sys.exit()
        output = a
    else:
        print("Option {} unknown".format(o))
        sys.exit(2)

if not checkMode:
    if modelPath is None:
        print("Path to the model is missing (option -m)")
        sys.exit(2)
    if templatePath is None:
        print("Path to the template is missing (option -t)")
        sys.exit(2)

