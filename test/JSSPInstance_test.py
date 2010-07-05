#coding=iso-8859-1

import unittest
import sys

# Importing test source file
sys.path.append("../src")
from JSSPInstance import *


class JSSPInstance_test(unittest.TestCase):

	def testCar5(self):
		#Testing Car5.txt file
		JSSPInst = JSSPInstance("../jssp_instances/Car5.txt")

		self.assert_(JSSPInst.jobs == 10, "Error: Jobs %i != %i" % (JSSPInst.jobs, 10)) 
		self.assert_(JSSPInst.machines == 6, "Error: Mach %i != %i" % (JSSPInst.machines, 6)) 

		self.assert_(JSSPInst.jobSpan[0][0] == 333, "Error: jobSpan[0][0] %i != %i" % (JSSPInst.jobSpan[0][0], 333))
		self.assert_(JSSPInst.jobSpan[4][2] == 123, "Error: jobSpan[4][2] %i != %i" % (JSSPInst.jobSpan[4][2], 123))
		self.assert_(JSSPInst.jobSpan[9][5] == 856, "Error: jobSpan[9][5] %i != %i" % (JSSPInst.jobSpan[9][5], 856))

		#JSSPInst.printJobSpan()
		#print "testCar5: OK"
	
	
	def testRec07(self):
		#Testing ReC07.txt file
		JSSPInst = JSSPInstance("../jssp_instances/ReC07.txt")

		self.assert_(JSSPInst.jobs == 20, "Error: Jobs %i != %i" % (JSSPInst.jobs, 20)) 
		self.assert_(JSSPInst.machines == 10, "Error: Mach %i != %i" % (JSSPInst.machines, 10)) 

		self.assert_(JSSPInst.jobSpan[0][0] == 28, "Error: jobSpan[0][0] %i != %i" % (JSSPInst.jobSpan[0][0], 28))
		self.assert_(JSSPInst.jobSpan[9][4] == 34, "Error: jobSpan[9][4] %i != %i" % (JSSPInst.jobSpan[9][4], 34))
		self.assert_(JSSPInst.jobSpan[19][9] == 41, "Error: jobSpan[19][9] %i != %i" % (JSSPInst.jobSpan[19][9], 41))

		#JSSPInst.printJobSpan()
		#print "testReC07: OK"
		

	def testAbz5(self):
		#Testing abz5.txt file
		JSSPInst = JSSPInstance("../jssp_instances/abz5.txt")
		self.assert_(JSSPInst.jobs == 10, "Error: Jobs %i != %i" % (JSSPInst.jobs, 10)) 
		self.assert_(JSSPInst.machines == 10, "Error: Mach %i != %i" % (JSSPInst.machines, 10)) 
		
		self.assert_(JSSPInst.jobSpan[0][0] == 86, "Error: jobSpan[0][0] %i != %i" % (JSSPInst.jobSpan[0][0], 86))
		self.assert_(JSSPInst.jobSpan[4][4] == 88, "Error: jobSpan[4][4] %i != %i" % (JSSPInst.jobSpan[4][4], 88))
		self.assert_(JSSPInst.jobSpan[9][9] == 96, "Error: jobSpan[9][9] %i != %i" % (JSSPInst.jobSpan[9][9], 96))
		
		#JSSPInst.printJobSpan()
		#print "testAbz5: OK"

	
	def runTest(self):
		return

	
	def getSuite(self):
		suite = unittest.TestSuite()
		suite.addTest(JSSPInstance_test("testCar5"))
		suite.addTest(JSSPInstance_test("testAbz5"))
		suite.addTest(JSSPInstance_test("testRec07"))
		#The test order commented below was used to debug an error 
#		suite.addTest(JSSPInstance_test("testAbz5"))
#		suite.addTest(JSSPInstance_test("testRec07"))
#		suite.addTest(JSSPInstance_test("testCar5"))
		return suite
