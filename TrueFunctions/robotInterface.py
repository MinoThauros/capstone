import numpy as np
import pandas as pd
from DataInterface import strings2dict
from dataProcessor import *

#interface should do take in address of master data, incoming scan data and index of master data
#scan starts at 0
#

class robotInterface:
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
        
        
    def compare(self,incomindData:pd.DataFrame,masterIndex:int):
        masterData=self.getmasterData()
        
        
         
        
        return self.masterData
        
"""
robot=robotInterface("data/lidarFile.txt")

robot.getMasterdata()

robot.clean()

robot.compare([dfsdfdsfgsd],scanNumber:int)->bool
"""      
