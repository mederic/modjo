#! /usr/bin/python
import argparse

from core.test.test_model import *
from core.test.test_template import *

parser = argparse.ArgumentParser(description='Modjo - test runner')
parser.add_argument('-t', '--testName', action="store", dest="test_name",
default=None, help='run a single test by its name')

args = parser.parse_args()

suite = []

if args.test_name is None:
    suite.append(unittest.TestLoader().loadTestsFromTestCase(SimpleModelTestCase))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(WrongModelTestCase))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(SimpleTemplateTestCase))
    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suite))
else:
    try: 
        testClass = locals()[args.test_name]
        suite.append(unittest.TestLoader().loadTestsFromTestCase(testClass))
        unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suite))
    except KeyError:
        print "Inexisting test class : " + args.test_name


