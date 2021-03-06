#!/usr/bin/python
from ResultReader import getAllLineProfile, parseChannels, parseFreq, parsePeakIntensity, parseCompound, parseName
from InputIngestor import getExpectedLineNum, getExpectedLines
from TaskRunner import runAllProjects
from ResultAnalyzer import compare
from NewParamBuilder import findAllCombinations
from LatexGenerator import generate

#configs
numsigmaRange = [8.0, 9.0]
minchanRange = [5, 6]
maxchanRange = [24, 25]
fileName = "../data/spw1.dirt.fits"
inputFile = "input.txt"


def generateAllParams():
    """
    Caller function of findAllCombinations in NewParamBuilder
    Args:
        (G) numsigmaRange, minchanRange, maxchanRange
    Returns:
        A list of all possible parameter combinations (list of triple tuples)
    """
    return findAllCombinations(numsigmaRange, minchanRange, maxchanRange)

#this step produces all results...MIGHT TAKE SOMETIME
def runAllTasks():
    """
    Caller function of runAllProjects in TaskRunner
    Args:
        (G) fileName
    Returns:
        NONE
    """
    allParams = generateAllParams()
    runAllProjects(allParams, fileName)

def getAllResult():
    """
    Args:
        (G) fileNmae
    Returns:
        a list of All identified molecular lines frequency range in all ADMIT result BDPS (nested list)
    """
    result = []
    folders = makeResultFolderNames()
    for folder in folders:
        lines = parseFreq(getAllLineProfile(folder, 'lltable.4.json'))
        result.append(lines)
    return result


def getExpectedMolecularLines():
    """
    Args:
        (G) inputFile
    Returns:
        frequency ranges of all expected molecular lines (nested list)
    """
    return getExpectedLines(inputFile)

def getAllDiff():
    """
    Args:
        NONE
    Returns:
        over diff result! this is what we WANT!
    """
    result = []
    allBDPResults = getAllResult()
    for BDPResult in allBDPResults:
        result.append(compare(getExpectedMolecularLines(), BDPResult))
    return result   #this is what we want! (index based)

#what algorithm to use???
def checkResults():
    """
    Args:
        NONE
    Returns:
        index of best-fit parameter set in allParams
    """
    overallDiff = getAllDiff()
    minIndex = -1
    min = 9223372036854775807
    for diff in overallDiff:
        temp = -1
        for i in diff:
            temp += i
        if(temp < min):
            minIndex = overallDiff.index(diff)
            min = temp
    return minIndex #here it goes!!!

def printResult():
    """
    Prints out best fit parameter combination
    """
    bestFitIndex = checkResults()
    print(generateAllParams()[bestFitIndex])

def makeResultFolderNames():
    """
    Args:
        NONE
    Returns:
         A list of all ADMIT task BDP folder names (custom naming fashion in TaskRunner)
    """
    result = []
    for i in range(0, len(generateAllParams())):
        folderName = 'molecular-line.admit' + '_' + str(i) + '/'
        result.append(folderName)
    return result

def run():
    """
    Master function, calls every functions to complete workflow
    """
    printResult()


runAllTasks()
run()
