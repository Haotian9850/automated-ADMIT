#return a new combination of parameters based on previous parameter set
#parameters of concern: numsigma, minchan, maxgap

#complete search
#numsigma: 0.1 - 5.0, increment 0.1
#minchan: 1 - 20, increment 1
#maxchan: 5 - 40, increment 1

import numpy as np
from Main import numsigmaRange, minchanRange, maxchanRange

numsigmaRange = numsigmaRange
minchanRange = minchanRange
maxchanRange = maxchanRange

def findAllCombinations(numsigmaRange, minchanRange, maxchanRange):
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
