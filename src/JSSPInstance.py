#coding=iso-8859-1

import os

class JSSPInstance:

	# Number of jobs
	jobs = 0 
	# Number of machines
	machines = 0
	# Matrix indicates how long does each job take
	jobSpan = []
	# File descriptor to the input file
	fd = 0


	def __init__(self, fileName):
		self.jobs = 0
		self.machines = 0
		self.jobSpan=[]
		self.fd = open(fileName, 'r')
		self.parseFile()
		return

	
	def parseFile(self):
		# First line: read Jobs and Machines converting to int
		line = self.fd.readline()
		self.jobs, self.machines = map(int, line.split())

		# Reading the each job span
		for j in range(self.jobs):
			self.jobSpan.append([0] * self.machines) # append a job row to the matrix filled with zeroes.
			line = self.fd.readline()
			fields = line.split()
			f = 0
			while(f < len(fields)):
				m = int(fields[f])     # Machine ID
				s = int(fields[f+1])   # Span
				self.jobSpan[j][m] = s
				f = f + 2
		return

	
	def printJobSpan(self):
		for i in range(len(self.jobSpan)):
			print self.jobSpan[i]	
		return
