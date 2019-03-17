from read_calculated_result import parseChannels, parseFreq, parsePeakIntensity

from ingest_input import getExpectedNumPeaks, getExpectedPeaks

diff = []
allActualLineChannels = parseChannels()
allActualLineFreq = parseFreq()

allExpectedLines = getExpectedPeaks()
expectedNumLines = getExpectedNumPeaks()

#read and compare
def checkNumOfLines(expectedNumLines, actualNumLines):
    if(expectedNumLines != actualNumLines):
        print("Expected number of molecular lines does not match ADMIT calculation, applying soft comparison...")
        return False 
    print("Expected number of molecular lines matches ADMIT calculation, applying strict comparison...")
    return True

def strictCompare():
    result = []
    for i in range(0, len(allActualLineChannels), 1):
        lineDiff = abs((allActualLineFreq[i][1] + allActualLineChannels[i][0]) / 2.0 - allExpectedLines[i])
        result.append(lineDiff)
    return result

def softCompare():
    actualLines = []
    for i in range(0, len(allActualLineChannels), 1):
        line = (allActualLineFreq[i][1] + allActualLineFreq[i][0]) / 2.0
        actualLines.append(line)
    return softCompareLists(actualLines, allExpectedLines)

def softCompareLists(actualLines, expectedLines):
    result = []
    #complete search
    for i in range(0, len(expectedLines), 1):
        lineDiff = -1
        for j in range(0, len(actualLines), 1):
            tempDiff = abs(actualLines[i] - expectedLines[i])
            lineDiff = min(lineDiff, tempDiff)
        result.append(lineDiff)
    return result


#inputs are lists
def compare(expectedLines, actualLines):
    result = []
    if(checkNumOfLines(expectedNumLines, len(allActualLineChannels)):
        #compare every line
        result = strictCompare()
    else:
        #soft comparison
        result = softCompare
    return result #final comparison result

