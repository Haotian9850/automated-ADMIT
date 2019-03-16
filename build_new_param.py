#return a new combination of parameters based on previous parameter set
#parameters of concern: numsigma, minchan, maxgap


def increaseGap(numsigma, minchan, maxgap):
    result = [numsigma, minchan + 1, maxgap]
    return result

def decreaseGap(numsigma, minchan, maxgap):
    result = [numsigma, minchan, maxgap - 1]
    return result

