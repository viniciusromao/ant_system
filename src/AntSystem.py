#coding=iso-8859-1

import time
import random

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
	# System parameter used to update pheromone trail
	Q = 0
	# System parameter used to initialize pheromone trail
	Qini = 0
	# Minimum quantity of pheromone in a trail
	trailMin = 0
	# Matrix of Pheromone trails
	trail=[]
	# Array with greedy heuristic values for each whole job
	greedy=[]
	# Array of job schedules build by each ant during a tour
	antScheds=[]
	# Best job schedule found
	bestSchedule = 0
	# JSSP problem instance
	jsspInst = 0
	# Selects the strategy to the pheromone increase: 0 - func pheromoneAdd, 1 - func pheromoneAddElitist (default)
	pheromoneStrategy = 0
	# best solutions found after every iteration
	spanList = []

	def __init__(self, fileName, alpha = 1, beta = 1, roh = 0.7, Q = 2.0, antX = 2, pheromoneStrategy = 1):
		# Initialize default values.
		self.antScheds=[]

		self.alpha = alpha
		self.beta = beta
		self.roh = roh
		self.Q = float(Q)
		self.Qini = 1.0
		self.jsspInst = JSSPInstance(fileName)
		self.ants = int(antX * self.jsspInst.jobs)
		self.pheromoneStrategy = pheromoneStrategy
		self.spanList = []

		# Initialize greedy values for each job with the whole duration
		self.greedy=[]
		for j in range(self.jsspInst.jobs):
			self.greedy.append(sum(self.jsspInst.jobSpan[j]))
	
		# Initialize trail matrix
		self.trailMin = self.Qini/sum(self.greedy)
		self.trail=[]
		for i in range(self.jsspInst.jobs):
			self.trail.append([0.0] * self.jsspInst.jobs)
			for j in range(self.jsspInst.jobs):
				self.trail[i][j] = self.trailMin

		# Initialize it with the worst possible value
		self.bestSchedule = Schedule(self.jsspInst)
		self.bestSchedule.makespan = sum(self.greedy)

		random.seed(time.time())
		return


	def antTour(self):
		# The job sequence build by the ant
		antSched=Schedule(self.jsspInst)
		# Initialize the roulette, which is a dictionary with JobId and the probability interval: (jobId:[pStart,pEnd])
		jobRoulette = dict([x, [0.0,0.0]] for x in range(self.jsspInst.jobs))

		# Defining the first job: randomized(70%) or best schedule(30%).
		if len(self.bestSchedule.jobSched) > 0 and random.random() > 0.7:
			currJob = self.bestSchedule.jobSched[0]   # The same first position of the last best schedule
		else:
			currJob = int((random.random() * 1000) % self.jsspInst.jobs)
		del jobRoulette[currJob]
		antSched.addJob(currJob)

		# Select next jobs
		while (len(jobRoulette) > 0):
			self.buildRoulette(jobRoulette, currJob)
			
			bingo = random.random()
			for jId,prob in jobRoulette.iteritems():
				if prob[0] < bingo < prob[1]:
					currJob = jId
					break
			del jobRoulette[currJob]
			antSched.addJob(currJob)

		self.antScheds.append(antSched)
		return
	

	def buildRoulette(self, jobRoulette, currJob):

		# Sum the pruducts (trail * greedy) for each job allowed to the ant
		denominator = 0
		for nextJob in jobRoulette:
			denominator = denominator +  self.trail[currJob][nextJob] * (1.0/self.greedy[nextJob])

		# Calculate the probability for each job
		pStart = 0.0
		pEnd = 0.0
		for nextJob in jobRoulette:
			p = (self.trail[currJob][nextJob] * (1.0/self.greedy[nextJob])) / denominator
			pStart = pEnd      # The interval starts after the last one.
			pEnd = pStart + p  # The end of interval
			jobRoulette[nextJob][0]= pStart
			jobRoulette[nextJob][1]= pEnd
		return


	def trailUpdate(self):
		self.pheromoneEvap()
		if self.pheromoneStrategy == 0:
			self.pheromoneAdd()
		else:
			self.pheromoneAddElitist()
		return


	def pheromoneEvap(self):
		for i in range(self.jsspInst.jobs):
			self.trail.append([0.0] * self.jsspInst.jobs)
			for j in range(self.jsspInst.jobs):
				newTrail = self.trail[i][j] * self.roh
				if newTrail > self.trailMin:
					self.trail[i][j] = newTrail
				#self.trail[i][j] *= self.roh
		return


	def pheromoneAdd(self):
		for sched in self.antScheds:
			for i in range(len(sched.jobSched) - 1):
				self.trail[sched.jobSched[i]][sched.jobSched[i+1]] += self.Q/sched.makespan
		return
	
	
	def pheromoneAddElitist(self):
		sched = self.bestSchedule
		for i in range(len(sched.jobSched) - 1):
			self.trail[sched.jobSched[i]][sched.jobSched[i+1]] += self.Q/sched.makespan
		return


	def runCompleteTour(self, iterations):
		for i in range(iterations):
			self.antScheds = []
			for j in range(self.ants):
				self.antTour()
			self.findBestJobSchedule()
			self.trailUpdate()
			self.spanList.append(self.bestSchedule.makespan)
		return


	def findBestJobSchedule(self):
		min = self.antScheds[0]
		for s in self.antScheds:
			if s.makespan < min.makespan:
				min = s
		
		if min.makespan < self.bestSchedule.makespan:
			self.bestSchedule = min
			

	def printTrailMatrix(self):
		for i in range(self.jsspInst.jobs):
			print self.trail[i]





