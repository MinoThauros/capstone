import numpy as np
import pandas as pd
from DataInterface import arrayExtractor, strings2dict
from dataProcessor import *

#interface should do take in address of master data, incoming scan data and index of master data
#scan starts at 0
#

class robotInterface:
    """summary: class which takes in address of master data as initialization parameter
                
        Methods: 
        
            + getmasterData()->list[pd.dataframe] 
                returns masterData fromt the initialization address
            
            + compare(incomindData:pd.DataFrame,masterIndex:int)-> bool 
                takes in incomming data and index of master data to compare it with; returns True if the data is different
    """
    def __init__(self,addy:str):
        self.masterData:str=addy
        
    def getmasterData(self):
        temp_file: list[dict] = []
        scans: list[pd.DataFrame] = []
        rawdata = extractor(self.masterData)
        sectionedData = sectionAtor(rawdata)
        #print('NUmber of data in 1 scan', len(sectionedData[0]))
        for element in sectionedData:
            temp_file = cleaner(convertDatatoPd(strings2dict(element)))
            scans.append(temp_file)
        return scans
        
        
    def compare(self,incomindData:pd.DataFrame,masterIndex:int,masterData:list[DataInterface]):
        """summary: takes in incomming data and index of master data to compare it with; returns True if the data is different
        
        [Note]:to avoid multiple calls to getmasterData(), intantialize getmasterData() and then feed it to this method
        """
        cleanIncommingData=cleaner(convertDatatoPd(arrayExtractor(incomindData)))
        common_index=compa_adjust(cleanIncommingData,masterIndex,masterData)
        comparing=comparator(cleanIncommingData,common_index,masterIndex)
        isDifferent=thresholder(comparing)
        return isDifferent
        
        

        
        
robotObj=robotInterface("data/half_close_master.txt")

print(robotObj.getmasterData())


    

