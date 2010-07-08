#!/usr/bin/python
#coding=iso-8859-1

import os

#------------------------------ Global Variables -------------------------------


#--------------------------------- Functions -----------------------------------
def runCmdLog(cmd, nTimes, logFile):
	lf = os.open(logFile, os.O_RDWR | os.O_CREAT | os.O_APPEND)
	
	for i in range(nTimes):
		pstdin, pstdout, pstderr = os.popen3(cmd)
		
		line = pstdout.readline()
		makespan = line[0:line.find(' ')]
		jobSched = line[line.find(' ')+1:]

		line = pstderr.readline()
		time = line[0:line.find('u')]

		logLine = "%i\t%s\t%s\t%s" % (i, makespan, time, jobSched)
		print logLine
		os.write(lf, logLine)

		pstdin.close()
		pstdout.close()
		pstderr.close()
	
	os.close(lf)
	
	return

#-------------------------------- Main Program ---------------------------------

#Run each instance N-times and log results

nTimes = 20
cmd = "time ../src/main.py -n 20 ../jssp_instances/abz5.txt"
logFile = "abz5.log"
runCmdLog(cmd, nTimes, logFile)


nTimes = 100
cmd = "time ../src/main.py -n 2000 ../jssp_instances/ReC07.txt"
logFile = "ReC07.log"
runCmdLog(cmd, nTimes, logFile)

nTimes = 100
cmd = "time ../src/main.py -n 2000 ../jssp_instances/Rec13.txt"
logFile = "Rec13.log"
runCmdLog(cmd, nTimes, logFile)
print "--- END ---"
