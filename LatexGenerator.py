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

