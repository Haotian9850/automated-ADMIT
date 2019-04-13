#!/usr/bin/python

def generate(frequencies, intensities, channels):
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
        row = assembleRow(frequencies[i], intensities[i], channels[i])
        result.append(row)
    generateLatex(result)
    return result

def assembleRow(freq, intensity, channels):
    """
    Args:
        freq: frequency of a row, float
        intensity: peak intensity of a row, float
        channels: channels range of a row, int tuple
    Returns:
        a Latex table row as a string
    """
    return "".join(freq) + " & " + "".join(intensity) + " & " + "".join(channels[0]) + " & " + "".join(channels[1]) + "\\" + "\\"

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