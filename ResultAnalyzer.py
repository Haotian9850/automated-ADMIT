#!/usr/bin/python
from ResultReader import parseFreq, parseChannels, parsePeakIntensity
from InputIngestor import getExpectedLineNum, getExpectedLines

expectedLineNum = getExpectedLineNum()
expectedLines = getExpectedLines()  #frequency range

actualLines = parseFreq()   #frequency range
actualLineChannels = parseChannels()
actualLineNum = len(parseFreq())

diff = []

#read and compare
def checkNumOfLines(expectedLineNum, actualLineNum):
    if(expectedLineNum != actualLineNum):
        print("Expected number of molecular lines does not match ADMIT calculation, applying soft comparison...")
        return False
    print("Expected number of molecular lines matches ADMIT calculation, applying strict comparison...")
    return True

def reduce(Rangelist):
    result = []
    for i in range(0, len(Rangelist), 1):
        midVal = abs(Rangelist[i][0] + Rangelist[i][1]) / 2.0
        result.append(midVal)
    return result 

def strictCompare():
    expectedMidVal = reduce(expectedLines)
    actualMidVal = reduce(actualLines)
    result = []
    for i in range(0, len(expectedMidVal), 1):
        lineDiff = abs(expectedMidVal[i] - actualMidVal[i])
        result.append(lineDiff)
    return result

def softCompare():
    return softCompareLists(reduce(expectedLines), reduce(actualLines))

def softCompareLists(list1, list2):
    result = []
    #complete search
    for i in range(0, len(list1), 1):
        lineDiff = -1
        for j in range(0, len(list2), 1):
            tempDiff = abs(list1[i] - list2[i])
            lineDiff = min(lineDiff, tempDiff)
        result.append(lineDiff)
    return result


#inputs are lists
#method export
def compare(expectedLines, actualLines):
    result = []
    if checkNumOfLines(expectedLines, actualLines) and len(actualLines) != 0:
        #compare every line
        result = strictCompare()
    else:
        #soft comparison
        result = softCompare()
    return result #final comparison result

