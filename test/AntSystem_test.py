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
		self.assert_(antSys.Q == 2.0, "Init Q = %i" % antSys.Q)
	
		self.assert_(antSys.greedy==[18,14,17], "Greedy values: %s" % antSys.greedy)

		return


	def testAntTour(self):
		# Testing the presentation istance
		antSys = AntSystem("../jssp_instances/transparencia.txt")
		#antSys = AntSystem("../jssp_instances/Car5.txt")
		#antSys = AntSystem("../jssp_instances/abz5.txt")
		antSys.antTour()
		antSys.antTour()
		print "antTour:"
		
		print antSys.antScheds[0].makespan
		print antSys.antScheds[0].jobSched
		
		print antSys.antScheds[1].makespan
		print antSys.antScheds[1].jobSched
		
		return


	def testTrailUpdate(self):
		return

	
	def testRunCompleteTour(self):
		# Testing the presentation istance
		#antSys = AntSystem("../jssp_instances/transparencia.txt")
		antSys = AntSystem("../jssp_instances/Car5.txt")
		#antSys = AntSystem("../jssp_instances/abz5.txt", roh = 0.9)

		antSys.runCompleteTour(100)
		
		print "final solutions"
		for i in range(len(antSys.antScheds)):
			print "i: ", antSys.antScheds[i].makespan, antSys.antScheds[i].jobSched

		print "\nBest solution"
		print antSys.bestSchedule.makespan, antSys.bestSchedule.jobSched
		return


	def testFindBestJobSchedule(self):
		antSys = AntSystem("../jssp_instances/abz5.txt")

		for i in range(3):
			antSys.antScheds = []
			for j in range(antSys.ants):
				antSys.antTour()
			#antSys.trailUpdate()
			antSys.findBestJobSchedule()
			
			print "Ant Schedules"
			for i in range(len(antSys.antScheds)):
				print "i: ", antSys.antScheds[i].makespan, antSys.antScheds[i].jobSched
			
			print "\nBest solution"
			print antSys.bestSchedule
			print antSys.bestSchedule.makespan, antSys.bestSchedule.jobSched
		return
	
	
	def runTest(self):
		return


	def getSuite(self):
		suite = unittest.TestSuite()
		suite.addTest(AntSystem_test("testInit"))
		suite.addTest(AntSystem_test("testAntTour"))
		suite.addTest(AntSystem_test("testTrailUpdate"))
#		suite.addTest(AntSystem_test("testFindBestJobSchedule"))
		suite.addTest(AntSystem_test("testRunCompleteTour"))
		return suite
