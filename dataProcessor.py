from hashlib import new
from typing import overload
from DataInterface import extractor, convertDatatoPd, sectionAtor, cleaner, DataInterface, basicExtractor
import pandas as pd
"""
class InadquateData(error):
    pass
"""


def compa_adjust(newScan:pd.DataFrame, masterIndex:int, masterData:list[pd.DataFrame]):
    """Compares the newly taken scan to master data and make adjustments to make the comparision right
    
    Args:
        data (list[pd.DataFrame]): Oncoming  scan
        
    returns: index object of the comon indexes
    """
    relevant_master_data=masterData[masterIndex]
    #get index comon to both dataframes
    master_index=relevant_master_data.index
    newScan_index=newScan.index
    comonIndexes=master_index.intersection(newScan_index)
    return comonIndexes

def comparator(newScanData:list[pd.DataFrame],comonIndexes:pd.Index, masterIndex:int):
    """_summary_: takes in newly taken scan and compares it to adequate element in master data

    Args:
        data (list[pd.DataFrame]): newly taken scan

    Raises:
        InadquateData: flag if there is a mismatch in the size of the data

    Returns:
        _type_: _description_
    """
    masterData=DataInterface()[masterIndex]
    matching_masterData=masterData.loc[comonIndexes]
    matching_newScanData=newScanData.loc[comonIndexes]
    differences:list[float]=[]
    #we're now comparing a dataframe to another dataframe
    if len(matching_masterData)==len(matching_newScanData):
        percentageDiff=abs(((matching_masterData['Dist']-matching_newScanData['Dist'])/matching_masterData['Dist'])*100)
    else:
        #raise InadquateData("The data is not adequate")
        print("The data is not adequate")
        
    return percentageDiff

def thresholder(data:list[pd.DataFrame]):
    change:bool=False
    overall_difference=sum(data)/len(data)
    print(overall_difference)
    if overall_difference>=10:
        change=True
    return change
    


#test_index=[1,2,3,4,10,7]
#test_index=test_index.sort()
#print(comparator(DataInterface()[2],test_index,8))

"""
def mainComparator():
    masterData=DataInterface()
    incommingData=cleaner(convertDatatoPd(basicExtractor("data/all_close_run2_good.txt")))
    common_indexes:pd.Index=compa_adjust(incommingData,6,masterData)
    comparing=comparator(incommingData,common_indexes,6)
    isDifferent=thresholder(comparing)
    return(isDifferent)

"""


    
    

