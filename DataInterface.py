#interface to parse file received from the lidar into CSV format
#perform arythemtics to compare roughly equivalent point sets
#return a %of difference 

import csv
import pandas as pd
import zlib

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

print(KeyValues[:10])
print(KeyValues[-10:])

#next step:creating a function which takes in a similar LidaR file and returns dictionaries
#subsampling before processing:
#https://towardsdatascience.com/how-to-automate-lidar-point-cloud-processing-with-python-a027454a536cs