#coding=iso-8859-1

import unittest
import sys

# Importing test source files
sys.path.append("../src")
from Schedule import *
from JSSPInstance import *

class Schedule_test (unittest.TestCase):

	def testAddJob(self):
		# Testing the presentation istance
		jsspInst = JSSPInstance("../jssp_instances/transparencia.txt")
		sched = Schedule(jsspInst)

		status = sched.addJob(0)
		self.assert_(status == True, "Error job 0")
		
		status = sched.addJob(1)
		self.assert_(status == True, "Error job 1")
		
		status = sched.addJob(1)
		self.assert_(status == False, "Duplicated jobId")
		
		status = sched.addJob(6)
		self.assert_(status == False, "Invalid jobId(0-2): 6")
		
		status = sched.addJob(2)
		self.assert_(status == True, "Error job 2")
		
		status = sched.addJob(3)
		self.assert_(status == False, "Maximum jobs exceeded")

		self.assert_(sched.jobSched[0] == 0, "jobSched 0")
		self.assert_(sched.jobSched[1] == 1, "jobSched 1")
		self.assert_(sched.jobSched[2] == 2, "jobSched 2")
		return


	def testObjectiveFunction(self):
		# Testing the presentation istance
		jsspInst = JSSPInstance("../jssp_instances/transparencia.txt")
		
		sched = Schedule(jsspInst)
		sched.addJob(0)
		sched.addJob(1)
		sched.addJob(2)
		self.assert_(sched.makespan == 30, "Makespan: %i" % sched.makespan)

		sched = Schedule(jsspInst)
		sched.addJob(0)
		sched.addJob(2)
		sched.addJob(1)
		self.assert_(sched.makespan == 34, "Makespan: %i" % sched.makespan)
		
		sched = Schedule(jsspInst)
		sched.addJob(1)
		sched.addJob(0)
		sched.addJob(2)
		self.assert_(sched.makespan == 29, "Makespan: %i" % sched.makespan)
		
		sched = Schedule(jsspInst)
		sched.addJob(2)
		sched.addJob(1)
		sched.addJob(0)
		self.assert_(sched.makespan == 26, "Makespan: %i" % sched.makespan)
		
		# Testing the Abz5 istance. Makespan value sent from e-mail list
		jsspInst = JSSPInstance("../jssp_instances/abz5.txt")
		
		sched = Schedule(jsspInst)
		sched.addJob(7)
		sched.addJob(0)
		sched.addJob(2)
		sched.addJob(9)
		sched.addJob(6)
		sched.addJob(8)
		sched.addJob(4)
		sched.addJob(5)
		sched.addJob(1)
		sched.addJob(3)
		self.assert_(sched.makespan == 1544, "Makespan: %i" % sched.makespan)
		
		# Prof. Valdisio said that this is the best known makespan: 1544. But we found 1731.
		sched = Schedule(jsspInst)
		sched.addJob(5)
		sched.addJob(9)
		sched.addJob(3)
		sched.addJob(4)
		sched.addJob(6)
		sched.addJob(2)
		sched.addJob(7)
		sched.addJob(0)
		sched.addJob(1)
		sched.addJob(8)
		self.assert_(sched.makespan == 1731, "Makespan: %i" % sched.makespan)
		
		# Testing the Car5 istance. Makespan value sent from e-mail list
		jsspInst = JSSPInstance("../jssp_instances/Car5.txt")
		
		sched = Schedule(jsspInst)
		sched.addJob(4)
		sched.addJob(3)
		sched.addJob(2)
		sched.addJob(0)
		sched.addJob(5)
		sched.addJob(1)
		sched.addJob(8)
		sched.addJob(6)
		sched.addJob(9)
		sched.addJob(7)
		self.assert_(sched.makespan == 7822, "Makespan: %i" % sched.makespan)
		return


	def runTest(self):
		return


	def getSuite(self):
		suite = unittest.TestSuite()
		suite.addTest(Schedule_test("testAddJob"))
		suite.addTest(Schedule_test("testObjectiveFunction"))
		return suite
