#!/usr/bin/python

def checkNumOfLines(expectedLineNum, actualLineNum):
    """
    Args:
        expectedLineNum: expected number of molecular lines (int)
        actualLineNums: actual number of identified molecular lines (int, comes back from ADMIT task)
    Returns"
        Ture if inputs are equal in value, False otherwise
    """
    if(expectedLineNum != actualLineNum):
        print("Expected number of molecular lines does not match ADMIT calculation. Procced to next parameter set.")
        return False
    print("Expected number of mulecular lines matches ADMIT calculation. Proceed to further comparisons")
    return True

def reduce(l):
    """
    Args:
        Rangelist: generic list of tuples (can be either float or int tuple)
    Return:
        Reduced int list based on average value of every tuple in input tuple list
    """
    result = []
    for s in l:
        midVal = abs(float(s[0]) - float(s[1])) / 2.0
        result.append(midVal)
    return result 

def strictCompare(expectedMidVal, actualMidVal):
    """
    Args:
        expectedMidVal: reduced tuple list of expected molecular line ranges
        actualMidVal: reduced tuple list of actual identified molecular line ranges
    Returns:
        A list of absolute differences between every element in two input lists
    """
    result = []
    for i in range(0, len(expectedMidVal), 1):
        lineDiff = abs(expectedMidVal[i] - actualMidVal[i])
        result.append(lineDiff)
    return result

def softCompare(list1, list2):
    """
    Caller function of softCompareLists()
    """
    return softCompareLists(list1, list2)

def softCompareLists(list1, list2):
    """
    Args:
        list1: int / float list
        list2: int / float list
    Returns:
        A list of absolute differences between every element in two input lists based on soft comparison
    """
    result = []
    #complete search
    for i in range(0, len(list1), 1):
        lineDiff = -1
        for j in range(0, len(list2), 1):
            tempDiff = abs(list1[i] - list2[j])
            lineDiff = min(lineDiff, tempDiff)
        result.append(lineDiff) #length of result will be length of list1 (expectde molecular line)
    return result

def compare(expectedLines, actualLines):
    """
    Args:
        expectedLines: expeced molecular lines (list of float tuples)
        actualLines: actual identified molecular lines (list of float tuples)
    Returns:
        A list of absolute difference between every element in two input lists based on either soft or strict comparison
    """
    result = []
    if checkNumOfLines(expectedLines, actualLines) and len(actualLines) != 0:
        #compare every line
        result = strictCompare(reduce(expectedLines), reduce(actualLines))
    else:
        #soft comparison
        result = softCompare(reduce(expectedLines), reduce(actualLines))
    return result #final comparison result



