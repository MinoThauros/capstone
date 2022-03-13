import csv
import pandas as pd
import numpy as np
import math

# ex of address :"data/lidarFile.txt"


def extractor(address: str):
    """Extracts .text file and returns an array of strings

    Returns:
        _type_: list[dict[str:float]]
    """
    myvars = []

    with open(address) as myfile:
        for line in myfile:
            myvars.append(line)
    return myvars


def strings2dict(myvars: list[str]):
    """converts a list of strings into a list of dictionary"""
    KeyValues = []
    for item in myvars:
        # creates a list made of every line
        # theta: 1.09 Dist: 00616.00 Q: 47; change this into a dictionary
        words = item.split()
        if len(words) <= 6:  # can improve this condition
            dataPoint = {
                str(words[0]).replace(":", ""): float(words[1]),
                str(words[2]).replace(":", ""): float(words[3]),
                str(words[4]).replace(":", ""): float(words[5])}
            KeyValues.append(dataPoint)
    return KeyValues


def convertDatatoPd(data: list[dict[str:float]]):
    """converts a list of strings into a list of dataframe"""
    Cleaned_Data = pd.DataFrame(data)
    return Cleaned_Data


def sectionAtor(data: list[str]):
    """creates a list of list by detecting seperators

    Args:
        text (str): a string of text to be parsed.

    Returns:
        array[str]: an array of sectioned strings
    """
    sublists: list = []  # to store newly accumulated sublist
    temp_element: list[str] = [""]
    currentSeparatorIndex = -1
    previousSeparatorIndex = -1
    for index, item in enumerate(data):
        if len(item) <= 8:
            currentSeparatorIndex = index
            temp_element = data[previousSeparatorIndex+1:currentSeparatorIndex]
            if previousSeparatorIndex+1 != currentSeparatorIndex:
                sublists.append(temp_element)
            previousSeparatorIndex = currentSeparatorIndex
    # print(currentSeparatorIndex+1)
    endElement = data[currentSeparatorIndex+1:]
    if endElement != []:
        sublists.append(endElement)
    # sublists.append(data_copy)
    # go through the list; when we meet a separator, append data from previous previous separator to current separator
    # create a new array everytime we match the sectioning string
    return sublists


def cleaner(data: pd.DataFrame):
    """formats extracted data:
#step1: delete rows with Q!=47
#step2: round up angles
#step3: set angles as indexes
#step4: drop duplicates
#step5: package every 0-360 as belonging to a single range in displacement
#step6: packagee every the sets of displacements as member of a given run 
    Args:
        data (pd.DataFrame): unindexed dataframe (with respect to angles)

    Returns:
        _pd.Dataframe: desired dataframe
    """

    HQ_data = data.drop(data[data.Q != 47].index)
    indexes = HQ_data['theta'].apply(np.floor)
    if len(indexes) == len(HQ_data):
        HQ_data = HQ_data.set_index(indexes).drop('theta', axis=1)
    # need to find a better alternative to round (theta)
    HQ_data = HQ_data[~HQ_data.index.duplicated(keep='first')]
    return HQ_data


def spinPackager(spins, diplacement):
    """packages a set of 0-360 data to the unit displacement

    Args:
        spins (pd.DataFrame[]): a list of dataframes of 0-360 data
        diplacement (int): the indexed displacement of robot

    Returns: Full data for a given displacement (unit)
    """
    return


def runPackager(displacement, run):
    """_summary_: standadizes the number of angles for a given displacement

    Args:
        displacement (_type_): _description_
        run (_type_): _description_
    """
    return


def DataInterface():
    """_summary_: _description_
        Extractor() extracts data from a .txt file; returns an array of strings (each line an element)

        SectionAror() takes in an array of strings and returns an array of arrays od strings (separated by Scan #)

        ConvertDataToPd() takes in an array of arrays of strings and returns an array of  dataframes

        cleaner() takes in a dataframe; cleans it up and drop an array of 0-360 dataframe

    """

    temp_file: list[dict] = []
    scans: list[pd.DataFrame] = []
    rawdata = extractor("data/master_data.txt")
    sectionedData = sectionAtor(rawdata)
    print('NUmber of data in 1 scan', len(sectionedData[0]))
    for element in sectionedData:
        temp_file = cleaner(convertDatatoPd(strings2dict(element)))
        scans.append(temp_file)
    return scans


"""bugs: after rounding up angles, the dataframe is not indexed properly sometimes, it does not go from 0-360; floor doesnt solve this issue

Egde cases:
+IF (element exists in new data but not in master data):
    =>Drop the indexes that are missing from master data 
+IF (element exists in master data but not in new data):
    =>Do not take these elements of new data into account for the comparison; but keep them in case next scan has them

=>length of comparison dataframe should be the same as the length of the smaller one

Clarifications (assumptions):
+the comparation function would be called directly from driving API; called everytime a new scan is received
+the new scan will then be cleaned up and packaged into a dataframe
+The dataframe will then be compared to corresponding dataframe in master data; how to do this?
    ==> drive function which calls the comparator will also send an index sequencially incremented when the function is called
    ==> this index ought to exist as a global variable in the file from which the comparator is called
    
Performance concerns:
+rewrite work in cython
"""


master_data = DataInterface()

for elemet in master_data:
    print(len(elemet))


print(len(DataInterface()[2]))

# print(master_data.index)
