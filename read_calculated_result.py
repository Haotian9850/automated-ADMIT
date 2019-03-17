import json

def getAllLineProfile():
    with open('sample_result.json', 'r') as jsonFile:
        allResult = json.load(jsonFile)
        lines = allResult["linetable"]["lines"]
    return lines

def parseFreq():
    result = []
    lines = getAllLineProfile()
    for line in lines:
        frequency = line["frequency"]
        result.append(frequency)
    print(result)
    return result

def parsePeakIntensity():
    result = []
    lines = getAllLineProfile()
    for line in lines:
        peakIntensity = line["peakintensity"]
        result.append(peakIntensity)
    print(result)
    return result

def parseChannels():
    result = []
    lines = getAllLineProfile()
    for line in lines:
        startChan = line["startchan"]
        endChan = line["endchan"]
        result.append((startChan, endChan))
    print(result)
    return result

def test():
    parseFreq()
    parseChannels()
    parsePeakIntensity()

test()