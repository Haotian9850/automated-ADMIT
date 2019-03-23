import numpy as np
from Main import numsigmaRange, minchanRange, maxchanRange

numsigmaRange = numsigmaRange
minchanRange = minchanRange
maxchanRange = maxchanRange


def findAllCombinations(numsigmaRange, minchanRange, maxchanRange):
    """
    Args:
        numsigmaRange: range of numsigma
        minchanRange: range of minchan (integer range)
        maxchanRange: range of maxchan (integer range)
    Returns:
        all possible executable parameter combinations (nested list)
    """
    result = []
    for numsigma in np.arange(numsigmaRange[0], numsigmaRange[1], 1.0):
        for minchan in range(minchanRange[0], minchanRange[1]):
            for maxchan in range(maxchanRange[0], maxchanRange[1]):
                newParamSet = ()
                if(minchan < maxchan):
                    newParamSet = (numsigma, minchan, maxchan)
                    result.append(newParamSet)
    print(len(result))
    return result
