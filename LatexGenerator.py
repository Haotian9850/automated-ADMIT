#!/usr/bin/python
import re
from ResultReader import getAllLineProfile, parseChannels, parseCompound, parseFreq, parseName, parsePeakIntensity

#(G)
DATA_PRODUCT_FILE_NAME = "data_product_spw0.dirt/"

def generate(frequencies, compounds, names, intensities, channels):
    """
    Args:
        frequencies: frequency result from best-fit ADMIT data product. float list
        intensities: peak intensity result from best-fit ADMIT data product. float list
        channels: channel result from best-fit ADMIT data product. list of int tuples
    Return:
        a list of strings each of which corresponds to a row in a Latex table
    """
    result = []
    for i in range(0, len(frequencies)):
        row = assembleRow(frequencies[i], compounds[i], names[i], intensities[i], channels[i])
        result.append(row)
    generateLatex(result)
    return result

def prettyPrintCompound(compound):
    """
    Linear complexity, most efficient!
    Args:
        compound: ugly compound name. Str
    Returns:
        a latex-compatible pretty print of the input name
    """
    # unable to identify
    if compound[0] == 'U':
        return "null"

    compoundList = []
    splitIndice = []
    result = []
    for i in range(0, len(compound) - 1):
        if (compound[i].isdigit() and not compound[i + 1].isdigit()):
            splitIndice.append(i + 1)
        elif (not compound[i].isdigit() and compound[i + 1].isdigit()):
            splitIndice.append(i + 1)

    splitIndice.insert(0, 0)
    splitIndice.insert(len(splitIndice), len(compound))

    for i in range(0, len(splitIndice) - 1):
        compoundList.append(compound[splitIndice[i] : splitIndice[i + 1]])
    for element in compoundList:
        newElement = element
        if element.isdigit():
            newElement = "_{" + element + "}"
        result.append(newElement)
    return "".join(result)
    

def assembleRow(freq, compound, name, intensity, channels):
    """
    Args:
        freq: frequency of a row, float
        intensity: peak intensity of a row, float
        channels: channels range of a row, int tuple
    Returns:
        a Latex table row as a string
    """
    return  "$" + "".join(str(round(float(freq), 6))) + "$" + " & " + "$" + "".join(prettyPrintCompound(compound)) + "$" + " & " + "".join(name)  + " & " + "$" + "".join(str(round(float(intensity), 6))) + "$" + "&" + "$" + "".join(channels[0]) + "$" + " & " + "$" + "".join(channels[1]) + "$" + "\\" + "\\"

def generateLatex(rows):
    """
    Writes table rows to latex.txt under root dir
    Args:
        list: a list of all table rows. String list
    Returns:
        NULL
    """
    file = open("latex.txt", "w+")
    for row in rows:
        file.write(row + "\n")
    file.close()

generate(parseFreq(getAllLineProfile(DATA_PRODUCT_FILE_NAME, "lltable.4.json")), 
        parseCompound(getAllLineProfile(DATA_PRODUCT_FILE_NAME, "lltable.4.json")),
        parseName(getAllLineProfile(DATA_PRODUCT_FILE_NAME, "lltable.4.json")),
        parsePeakIntensity(getAllLineProfile(DATA_PRODUCT_FILE_NAME, "lltable.4.json")), 
        parseChannels(getAllLineProfile(DATA_PRODUCT_FILE_NAME, "lltable.4.json")))

