#! /usr/bin/python

from core.test.test_model import *

suite = unittest.TestLoader().loadTestsFromTestCase(SimpleModelTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)

