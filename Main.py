#!/usr/bin/python
from ResultReader import getAllLineProfile
from TaskRunner import runAllProjects
from ResultAnalyzer import compare
from NewParamBuilder import findAllCombinations #is it really necessary?

#configs
numsigmaRange = [2.0, 4.0]
minchanRange = [1, 3]
maxchanRange = [4, 6]
inputFile = "fileName"

#workflow: 
