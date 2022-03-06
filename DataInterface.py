#interface to parse file received from the lidar into CSV format
#perform arythemtics to compare roughly equivalent point sets
#return a %of difference 

import csv
import pandas as pd
import zlib

def extractor():
    myvars=[]
    KeyValues=[]

    with open("data/lidarFile.txt") as myfile:
        for line in myfile:
            myvars.append(line)

    for item in myvars:
        #theta: 1.09 Dist: 00616.00 Q: 47; change this into a dictionary
        words=item.split()
        if len(words)==6:#can improve this condition
            dataPoint={
                str(words[0]).replace(":",""):float(words[1]),
                str(words[2]).replace(":",""):float(words[3]), 
                str(words[4]).replace(":",""):float(words[5])}
            KeyValues.append(dataPoint)

    #2 convert array for dictionaries to a dataframe
    Cleaned_Data=pd.DataFrame(KeyValues)
    return Cleaned_Data


#step1: delete rows with Q!=47
#step2: round up angles
#step3: set angles as indexes
#step4: drop duplicates
#step5: package every 0-360 as belonging to a single range in displacement
#step6: packagee every the sets of displacements as member of a given run 

#def indexer(data:pd.DataFrame):

def cleaner(data:pd.DataFrame):
    HQ_data=data.drop(data[data.Q!=47].index).round({'theta':0}).set_index('theta')
    HQ_data=HQ_data[~HQ_data.index.duplicated(keep='first')]
    return HQ_data

def spinPackager(spins,diplacement):
    return

def runPackager(displacement, run):
    return
    



print(cleaner(extractor()))

#subsampling before processing:
#setup file accumulation interface to be able to compare different runs
#https://towardsdatascience.com/how-to-automate-lidar-point-cloud-processing-with-python-a027454a536c

#plan1: subsample the dataframe to a smaller number of points; have a target number of points so that there is roughly a regular point density per unit area