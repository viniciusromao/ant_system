#!/usr/bin/python
#coding=iso-8859-1

import unittest
import JSSPInstance_test
import Schedule_test
import AntSystem_test

#------------------------------------ Main -------------------------------------

# Getting test suites
suite1 = JSSPInstance_test.JSSPInstance_test().getSuite()
suite2 = Schedule_test.Schedule_test().getSuite()
suite3 = AntSystem_test.AntSystem_test().getSuite()

# Bubling suites
allTests = unittest.TestSuite((suite1,suite2,suite3))

# Running tests
runner = unittest.TextTestRunner()
runner.run(allTests)

print "--- Tests End ---"
