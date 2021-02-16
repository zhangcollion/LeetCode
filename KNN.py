from numpy import *
import operator
def creatDataSet():
    group = array([[1,1],[1,2],[2,3],[3,2]])
    label = ['A','A','B','B']
    return group, label
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append((listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector