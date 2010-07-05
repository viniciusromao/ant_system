#coding=iso-8859-1

from JSSPInstance import *
from Schedule import *


class AntSystem:
	
	# Quantity of ants in the system
	ants = 0
	# Importance of the trail
	alpha = 0
	# Importance of the greedy heuristic value
	beta = 0
	# Evaporation coeficient
	roh = 0
	# Matrix of Pheromone trails
	trail=[]
	# Array with greedy heuristic values for each whole job
	greedy=[]
	# Array of job sequences build by each ant during a tour
	antSched=[]
	# JSSP problem instance
	jsspInst = 0

	# Minimum quantity of pheromone in a trail
	trailMin = 0
	# System parameter
	Q = 0

	def __init__(self, fileName, alpha = 1, beta = 1, roh = 0.7, Q = 1.0):
		self.antSched=[]

		self.alpha = alpha
		self.beta = beta
		self.roh = roh
		self.Q = Q
		self.jsspInst = JSSPInstance(fileName)
		self.ants = self.jsspInst.jobs

		# Initialize greedy values for each job with the whole duration
		self.greedy=[]
		for j in range(self.jsspInst.jobs):
			self.greedy.append(sum(self.jsspInst.jobSpan[j]))
	
		# Initialize trail matrix
		self.trailMin = self.Q/sum(self.greedy)
		self.trail=[]
		for i in range(self.jsspInst.jobs):
			self.trail.append([0.0] * self.jsspInst.jobs)
			for j in range(self.jsspInst.jobs):
				self.trail[i][j] = self.trailMin
		return


	def antTour(self):
		
		return


	def trailUpdate(self):
		return
