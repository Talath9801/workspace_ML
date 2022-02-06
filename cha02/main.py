# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 13:39:34 2022

@author: lenovo
"""

import kNN
group,labels = kNN.createDataSet()
print(group)
print(labels)

classifyNew = kNN.classify0([1.2,1.2], group, labels, 2)
print(classifyNew)