#!/usr/bin/python
def readFile(fileName):
    paramsFile = open(fileName)
    paramFileLines = paramsFile.readlines()
    return paramFileLines

#number of expected molecular lines
def getExpectedLineNum(fileName):
    lines = readFile(fileName)
    print(lines[0])
    return lines[0]

#frequency ranges of all expected molecular lines
def getExpectedLines(fileName):
    result = []
    lines = readFile(fileName)
    for i in range(1, len(lines)):
        line = lines[i].split(" ")
        result.append((line[0], line[1][0:len(line[1]) - 1]))
    print(result)
    return result