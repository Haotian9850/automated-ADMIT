#!/usr/bin/python
import json

def getAllLineProfile(fileName):
    with open(fileName, 'r') as jsonFile:
        allResult = json.load(jsonFile)
        lines = allResult["linetable"]["lines"]
    return lines

def parseFreq(lines):
    result = []
    for line in lines:
        frequency = line["frequency"]
        result.append(frequency)
    print(result)
    return result

def parsePeakIntensity(lines):
    result = []
    for line in lines:
        peakIntensity = line["peakintensity"]
        result.append(peakIntensity)
    print(result)
    return result

def parseChannels(lines):
    result = []
    for line in lines:
        startChan = line["startchan"]
        endChan = line["endchan"]
        result.append((startChan, endChan))
    print(result)
    return result