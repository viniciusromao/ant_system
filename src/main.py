#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
from AntSystem import *
import time


#------------------------------ Global Variables -------------------------------
# Command line options
# Quantity of iterations
iterations = 0
# Parameter System used in pheromone increase
q = 2.0
# Ants multiplicative factor
aX = 2
# number of runs
runs = 10
jsspFile = ""
instance = ""
verbose = False
# instance count
count = 0

#--------------------------------- Functions -----------------------------------
def printUsage ():
	print """
command: main [-h -n] <JSSP Instance file>

params:
	-h Help
	-n Interations
	-Q Parameter System (see Paper)
	-a Multiplicative factor of ants. For a = 2, ants = 2 * jobs
	-v Verbose

example:
	./main.py -n 200 ../jssp_instances/abz5.txt 

	./main.py -a 3 -Q 10 -n 200 ../jssp_instances/abz5.txt
"""


#-------------------------------- Main Program ---------------------------------

# Command line options
try:
	opts, args = getopt.getopt(sys.argv[1:], "hn:Q:a:v:r")
except getopt.GetoptError, err:
	# print help information and exit:
	print str(err)
	printUsage()
	sys.exit(2)

# Validate JSSP file
if len(args) != 1:
	print "[Error] JSSP instance input file!"
	printUsage()
	sys.exit(2)
else:
	jsspFile = args[0]
#	if os.path.isfile(jsspFile) == False:
#		print "[Error] Argument is not a file: " + f
#		printUsage()
#		sys.exit(2)


# Options
for o, a in opts:
	if o == "-n":
		iterations = int(a)
	elif o == "-Q":
		q = float(a)
	elif o == "-a":
		aX = float(a)
	elif o == "-v":
		verbose = True
	elif o == "-r":
		runs = int(a)
	else:
		printUsage()
		sys.exit(2)


### results
class Result:
	span = 0
	dtime = 0
	spanList = []
	
	def __init__(self, span, dtime, spanList):
		self.span = int(span)
		self.dtime = dtime
		self.spanList = spanList 

	def __str__(self):
		return "[" + str(self.spanList) + "; " + str(self.span) + "; " + str(self.dtime) + "]"

	def __repr__(self):
		return self.__str__()

### latex

def print_latex_preamble():
	print r'''\documentclass{article}
	\usepackage{multirow}
	\usepackage[utf8]{inputenc}
	\usepackage{amssymb}
	\begin{document}'''

	return


def print_latex_table_beginning():
	print r'''	\begin{table}
	\begin{tabular}{c|c|c|c||c||c|c|c||c}
	\hline\hline
	\multicolumn{4}{c||}{Instâncias Comparativas} & Solução 
	& \multicolumn{3}{|c||}{Solução Obtida} & Aproximação\\
	\hline
	Nº &  Referência & m & n & ``Ótima'' & Inicial & tempo (s) & Melhor & Gap\\
	\hline\hline
	1 & Abz5 & 10 & 10 & 1544 &  &  &  & \\
	2 & Car5 & 10 & 6 & 7720 & & & &\\
	\hline\hline
	\multicolumn{8}{r||}{Média das aproximações com resultados conhecidos
	$\rightarrowtail$} &
	\\
	\hline\hline
	Nº &  Referência & m & n & Inicial & Máxima & Média & Melhor & tempo (s)\\
	\hline\hline'''

def print_latex_table_end():
	print r'''	\hline\hline
	\end{tabular}
	\end{table}
	\end{document}'''


def print_gnuplot(l, instance):
	fname = "fig/" + instance + ".dat"
	f = open(fname, 'w')
	for i in range(len(l[0].spanList)):
		line = str((i+1)) + "\t" + str(l[0].spanList[i]) + "\n"
		f.write(line)
	f.close()

def print_latex(l, count, ants, instance):
	if len(l) > 0:
		average = 0
		for i in l:
			average += i.span
		average /= len(l)

		best = l[0]
		worst = l[-1]
		print '\t', count, "&",  instance, "&", ants.jsspInst.jobs, "&", ants.jsspInst.machines, "&", best.spanList[0], "&", worst.span, "&", average, "&", best.span, "&", best.dtime, r'\\'
	return


print_latex_preamble()
print_latex_table_beginning()

for inst in jsspFile.split(":"):
	results = []
	cont  = 0
	# Running Ant System Heuristic
	for i in range(20):
		antSys = AntSystem(inst, Q=q, antX=aX)
		start = time.clock()
		antSys.runCompleteTour(iterations)
		end = time.clock()
		r = Result(antSys.bestSchedule.makespan, 10 * (end - start), antSys.spanList)
		results.append(r)

	count += 1
	results = sorted(results, key=lambda item: item.span)
	instance = os.path.basename(inst).split(".")[0].lower()
	print_latex(results, count, antSys, instance)
	print_gnuplot(results, instance)

print_latex_table_end()

