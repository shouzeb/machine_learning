# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:50:04 2020

@author: Shouzeb
"""

from sklearn import tree

features= [[140,1],[130,1],[150,0],[170,0]]
labels=[0,0,1,1]
clf = tree.DecisionTreeClassifier()


clf = clf.fit(features, labels)

print (clf.predict([[150,0]]))
