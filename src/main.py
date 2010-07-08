#!/usr/bin/python

import sys
import getopt
from AntSystem import *

#------------------------------ Global Variables -------------------------------
# Command line options
# Quantity of iterations
iterations = 0
jsspFile = ""
verbose = False

#--------------------------------- Functions -----------------------------------
def printUsage ():
	print """
command: main [-h -n] <JSSP Instance file>
params:
	-h Help
	-n Interations
	-v Verbose

example:
	./main.py -n 200 ../jssp_instances/abz5.txt 
"""


#-------------------------------- Main Program ---------------------------------

# Command line options
try:
	opts, args = getopt.getopt(sys.argv[1:], "hn:v")
except getopt.GetoptError, err:
	# print help information and exit:
	print str(err)
	printUsage()
	sys.exit(2)

# Validate JSSP file
if len(args) != 1:
	print "[Error] JSSP instace input file!"
	printUsage()
	sys.exit(2)
else:
	jsspFile = args[0]
	if os.path.isfile(jsspFile) == False:
		print "[Error] Argument is not a file: " + f
		printUsage()
		sys.exit(2)
# Options
for o, a in opts:
	if o == "-n":
		iterations = int(a)
	elif o == "-v":
		verbose = True
	else:
		printUsage()
		sys.exit(2)

# Running Ant System Heuristic
antSys = AntSystem(jsspFile)

antSys.runCompleteTour(iterations)

if verbose:
	print "--- TRAIL MATRIX ---"
	antSys.printTrailMatrix()
	print "\nGreedy: ", antSys.greedy
	print "\n--- FINAL SOLUTIONS ---"
	for i in range(len(antSys.antScheds)):
		print antSys.antScheds[i].makespan, antSys.antScheds[i].jobSched

print "\nBest solution built:"
print antSys.bestSchedule.makespan, antSys.bestSchedule.jobSched

