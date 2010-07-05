#coding=iso-8859-1

import os

class Schedule:

	# Reference to the JSSP problem instance
	jsspInst = 0
	# List of jobs
	jobSched = []
	# Time elapsed to complete to the schedule
	makespan = 0


	def __init__(self, jsspInstance):
		self.makespan = 0
		self.jobSched = []
		self.jsspInst = jsspInstance
		return


	def addJob(self, jobId):
		if jobId >= self.jsspInst.jobs:
			return False

		if len(self.jobSched) < self.jsspInst.jobs:
			if not self.jobSched.count(jobId):
				self.jobSched.append(jobId)
			else:
				return False

			if len(self.jobSched) == self.jsspInst.jobs:
				self.objectiveFunction()
			
			return True
		return False


	def objectiveFunction(self):
		# Time spent for each machine
		machTime = [0] * self.jsspInst.machines

		for j in self.jobSched:
			machTime[0] = machTime[0] + self.jsspInst.jobSpan[j][0]
			for m in range(1, self.jsspInst.machines):
				if machTime[m] > machTime[m-1]:
					machTime[m] = machTime[m] + self.jsspInst.jobSpan[j][m]
				else:
					machTime[m] = machTime[m - 1] + self.jsspInst.jobSpan[j][m]

		self.makespan = machTime[len(machTime) - 1] # Accomplish time of the last machine
		return
