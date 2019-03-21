#!/usr/bin/python

def readFile():
    paramsFile = open("input.txt")
    paramFileLines = paramsFile.readlines()
    return paramFileLines

#number of expected molecular lines
def getExpectedLineNum(): 
    lines = readFile()
    print(lines[0])
    return lines[0]

#frequency ranges of all expected molecular lines
def getExpectedLines():
    result = []
    lines = readFile()
    for i in range(1, len(lines)):
        line = lines[i].split(" ")
        result.append((line[0], line[1][0:len(line[1]) - 1]))
    print(result)
    return result


getExpectedNumPeaks()
getExpectedPeaks()