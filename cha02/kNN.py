# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 13:29:04 2022

@author: lenovo
"""

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX,dataSet,labels,k):
    # P19
    #inX是待输入的点的坐标
    dataSetSize = dataSet.shape[0]#行数
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis = 1)
    distance = sqDistance**0.5
    sortedDistIndices = distance.argsort()
    #以上计算距离
    
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

    
