from distutils.log import error
from hashlib import new
from typing import overload
from DataInterface import extractor, convertDatatoPd, sectionAtor, strings2dict, DataInterface
import pandas as pd

class InadquateData(error):
    pass

def preComparator(data:list[pd.DataFrame]):
    """Compares the newly taken scan to master data and make adjustments to make the comparision right

    Args:
        data (list[pd.DataFrame]): Oncoming  
    """
    return

def comparator(data:list[pd.DataFrame]):
    """_summary_: takes in newly taken scan and compares it to master data

    Args:
        data (list[pd.DataFrame]): newly taken scan

    Raises:
        InadquateData: flag if there is a mismatch in the size of the data

    Returns:
        _type_: _description_
    """
    masterData=DataInterface()
    differences:list[float]=[]
    if len(masterData)==data:
        for index,item in enumerate(data):
            percentageDiff=(item['Dist']-masterData['Dist'])/masterData['Dist']
            differences.append(percentageDiff)
    else:
        raise InadquateData("The data is not adequate")
        
    return differences

def thresholder(data:list[pd.DataFrame]):
    change:bool=False
    difference_array=comparator(data)
    overall_difference=sum(difference_array)/len(difference_array)
    if overload(overall_difference)<0.4:
        change=True
    return change
    


    