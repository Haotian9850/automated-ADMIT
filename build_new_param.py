#return a new combination of parameters based on previous parameter set
#parameters of concern: numsigma, minchan, maxgap

#complete search
#numsigma: 0.1 - 5.0, increment 0.1
#minchan: 1 - 20, increment 1
#maxchan: 5 - 40, increment 1

import numpy as np

def findAllCombinations():
    result = []
    for numsigma in np.arange(3.0, 6.0, 1.0):
        for minchan in range(1, 5):
            for maxchan in range(10, 20):
                newParamSet = ()
                if(minchan < maxchan):
                    newParamSet = (numsigma, minchan, maxchan)
                    result.append(newParamSet)
    print(len(result))
    print(result)
    return result

def splitInto5():
    result = []
    temp = findAllCombinations()
    for i in range(0, len(temp), 5):
        group = []
        for j in range(i, i + 5):
            group.append(temp[j])
        result.append(group)
    print(len(result))
    print(result)
    return result

findAllCombinations()
splitInto5()