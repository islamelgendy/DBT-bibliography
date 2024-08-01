import os
import re
import shutil

def readCSVContents(file):
    with open(file, "r") as f:
        contents = f.readlines()

    return contents

def saveInSet(tokens):
    values = set()
    for elem in tokens:
        values.add(elem.strip())
    
    return values

def getValuesMap(contents):
    mapValues = dict()
    values = set()
    for line in contents:
        tokens = re.split(',', line)
        values = saveInSet(tokens[1:])
        mapValues[tokens[0]] = values
    
    return mapValues

def getNewContents(map1, map2):
    contents = list()
    # Add the header of the CSV
    id=0
    contents.append(',Artefact,Problem,count\n')

    test = dict()
    test.keys()
    metricKeys = map1.keys()
    artefactKeys = map2.keys()

    # Loop through the metric keys and find the occurences from the artefact keys
    for mk in metricKeys:
        metricRec = map1[mk]
        for ak in artefactKeys:
            artefactRec = map2[ak]
            count = getCountForSame(metricRec, artefactRec)
            
            # Add this to the contents
            contents.append(str(id) + ',' + mk + ',' + ak + ',' + str(count) + '\n')
            id += 1

    return contents

def getCountForSame(rec1, rec2):
    count = 0
    for elem in rec1:
        if elem in rec2:
            count += 1

    return count

def writeCsvFile(map1, map2, file):
    contents = getNewContents(map1, map2)

    with open(file, "w") as f:
        contents = "".join(contents)
        f.write(contents)

file1 = 'Survey/stats/artefacts.csv'
file2 = 'Survey/stats/problems.csv'
newFile = 'Survey/artefact-problem.csv'

contents1 = readCSVContents(file1)
contents2 = readCSVContents(file2)

map1 = getValuesMap(contents1)
map2 = getValuesMap(contents2)

# Write the sankey into the new file
writeCsvFile(map1, map2, newFile)