#! /usr/bin/python

from core.test.test_model import *

suite = unittest.TestLoader().loadTestsFromTestCase(SimpleModelTestCase)
suite = unittest.TestLoader().loadTestsFromTestCase(WrongModelTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)

