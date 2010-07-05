#coding=iso-8859-1

import unittest
import sys

# Importing test source files
sys.path.append("../src")
from Schedule import *
from JSSPInstance import *
from AntSystem import *

class AntSystem_test (unittest.TestCase):

	def testInit(self):
		# Testing the presentation istance
		antSys = AntSystem("../jssp_instances/transparencia.txt")

		self.assert_(antSys.alpha == 1, "Init alpha = %i" % antSys.alpha)
		self.assert_(antSys.beta == 1, "Init beta = %i" % antSys.beta)
		self.assert_(antSys.roh == 0.7, "Init roh = %i" % antSys.roh)
		self.assert_(antSys.Q == 1.0, "Init Q = %i" % antSys.Q)
	
		self.assert_(antSys.greedy==[18,14,17], "Greedy values: %s" % antSys.greedy)

		return


	def testAntTour(self):
		return


	def testTrailUpdate(self):
		return


	def runTest(self):
		return


	def getSuite(self):
		suite = unittest.TestSuite()
		suite.addTest(AntSystem_test("testInit"))
		suite.addTest(AntSystem_test("testAntTour"))
		suite.addTest(AntSystem_test("testTrailUpdate"))
		return suite
