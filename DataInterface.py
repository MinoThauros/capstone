import csv
import pandas as pd
import zlib

#ex of address :"data/lidarFile.txt"
def extractor(address:str):
    """Extracts .text file and returns an array of strings

    Returns:
        _type_: list[dict[str:float]]
    """
    myvars=[]

    with open(address) as myfile:
        for line in myfile:
            myvars.append(line)
    return myvars

def strings2dict(myvars:list[str]):
    """converts a list of strings into a list of dictionary"""
    KeyValues=[]
    for item in myvars:
        #creates a list made of every line
        #theta: 1.09 Dist: 00616.00 Q: 47; change this into a dictionary
        words=item.split()
        if len(words)==6:#can improve this condition
            dataPoint={
                str(words[0]).replace(":",""):float(words[1]),
                str(words[2]).replace(":",""):float(words[3]), 
                str(words[4]).replace(":",""):float(words[5])}
            KeyValues.append(dataPoint)
    return KeyValues


def convertDatatoPd(data:list[dict[str:float]]):
    """converts a list of strings into a dataframe"""
    Cleaned_Data=pd.DataFrame(data)
    return Cleaned_Data

def sectionAtor(data:list[str]):
        """creates a list of list by detecting seperators
        Args:
            text (str): a string of text to be parsed.

        Returns:
            array[str]: an array of sectioned strings
        """
        sublists:list=[]#to store newly accumulated sublist
        temp_element:list[str]=[""]
        currentSeparatorIndex=-1
        previousSeparatorIndex=-1
        for index,item in enumerate(data):
            if len(item)==4:
                currentSeparatorIndex=index
                temp_element=data[previousSeparatorIndex+1:currentSeparatorIndex]
                if previousSeparatorIndex+1!=currentSeparatorIndex:
                    sublists.append(temp_element)
                previousSeparatorIndex=currentSeparatorIndex
        #print(currentSeparatorIndex+1)
        endElement=data[currentSeparatorIndex+1:]
        if endElement!=[]:
            sublists.append(endElement)
        #sublists.append(data_copy)
        #go through the list; when we meet a separator, append data from previous previous separator to current separator    
        #create a new array everytime we match the sectioning string
        return sublists

def cleaner(data:pd.DataFrame):
    """formats extracted data:#step1: delete rows with Q!=47
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
    HQ_data=data.drop(data[data.Q!=47].index).round({'theta':0}).set_index('theta')
    HQ_data=HQ_data[~HQ_data.index.duplicated(keep='first')]
    return HQ_data

def spinPackager(spins,diplacement):
    """packages a set of 0-360 data to the unit displacement

    Args:
        spins (pd.DataFrame[]): a list of dataframes of 0-360 data
        diplacement (int): the indexed displacement of robot
        
    Returns: Full data for a given displacement (unit)
    """
    return

def runPackager(displacement, run):
    return
    

#IDEAS:
"""
+ returned numbers of spins are purely based on time
+-> solution: we expect a data set for a fixed amount of time; start with a desired number of spins per unit distance (desired resolution)
=>develop an interface which receives the speed to  adjust the number of spins recieved




=>
"""

def main():
    data=cleaner(convertDatatoPd(strings2dict(extractor("data/lidarFile.txt"))))
    return data
    
print(sectionAtor(["boob","a",'bob',"b",'b0ob',"c","de",'b0ob',"f",'b0ob',"g","hi",'bo0b',"j","k","l",'bo0b',"m","n",'bo0b',"o","p","boob"]))




#plan1: subsample the dataframe to a smaller number of points; have a target number of points so that there is roughly a regular point density per unit area