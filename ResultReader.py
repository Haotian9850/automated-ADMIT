#!/usr/bin/python
import json


def getAllLineProfile(pathToJson, fileName):
    """
    Args:
        fileName: name of input admit result file (String)
    Retuens:
        all information on all identified molecular lines (nested list)
    """
    with open(pathToJson + fileName, 'r') as jsonFile:
        allResult = json.load(jsonFile)
        lines = allResult["linetable"]["lines"]
    return lines

def parseFreq(lines):
    """
    Args:
        lines: all information on all identified molecular lines (nested list)
    Returns:
        frequency range of all identified molecular lines (nested list)
    """
    result = []
    for line in lines:
        frequency = line["frequency"]
        result.append(frequency)
    print(result)
    return result

def parsePeakIntensity(lines):
    """#!/usr/bin/python
    Args:
        lines: all information on all identified molecular lines (nested list)
    Returns:
        list of peak intensity of all identified molecular lines (list)
    """
    result = []
    for line in lines:
        peakIntensity = line["peakintensity"]
        result.append(peakIntensity)
    print(result)
    return result

def parseChannels(lines):
    """
    Args:
        lines: all information on all identified molecular lines (nested list)
    Returns:
        list of channel ranges of all identified molecular lines (nestde list)
    """
    result = []
    for line in lines:
        startChan = line["startchan"]
        endChan = line["endchan"]
        result.append((startChan, endChan))
    print(result)
    return result

def parseCompound(lines):
    """
    Args:
        lines: all information on all identified molecular lines. nested list
    Returns:
        list of identified elements. Str list
    """
    result = []
    for line in lines:
        compound = line["formula"]
        result.append(compound)
    return result

def parseName(lines):
    """
    Args:
        lines: all information on all identified molecular lines. nested list
    Returns:
        list of names of identified elements. Str list
    """
    result = []
    for line in lines:
        name = line["name"]
        result.append(name)
    return result