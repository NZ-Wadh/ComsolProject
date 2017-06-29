# -*- coding: utf-8 -*-
# test python 2.7 script
import matplotlib.pyplot as plt
import numpy as ny

class SizeDisagreeError(Exception):
    def __init__(self, Msg):
        self.Msg = Msg

class comsolLine:
    
    def __init__(self, nameList):
        self.nameList = nameList
        self.values = [None]*len(self.nameList)
        for ele in self.values:
            print ele
    
    def setValues(self, values):
        self.values = values
        for ele in self.values:
            print ele
        if self.checkDimension() == False:
            raise SizeDisagreeError('nameList and values size does not agree !')
        
    def checkDimension(self):
        #print len(self.values) == len(self.nameList)
        return len(self.values) == len(self.nameList)
            
line1 = comsolLine(['position', 'VW', 'MST'])
line1.setValues([1,2,3,4])
print line1.checkDimension()