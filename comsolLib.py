# -*- coding: utf-8 -*-
# test python 2.7 script
#import matplotlib.pyplot as plt
#import numpy as ny 
#import linecatche 


class comsolTxtFile:
    
    def __init__(self, fileName, titleList):

        self.readComsolExportedTxt(fileName, titleList)

                 
    def readComsolExportedTxt(self,fullfileName, titleList):
        # open txt file
        file_obj = open(fullfileName,'r')
        endOfComment = 0

        # find thelast line of comments
        for line in file_obj:
            
            if line[0] == '%':
               endOfComment+= 1 
            else:
                    break
        # return the cursor to the start of the file
        file_obj.seek (0)
        
        # Extract the variable line from last comment line
        self.comsolLineList = list()
        for i, line in enumerate(file_obj):
            
            if i < endOfComment-1:
                pass
            elif i == endOfComment-1:
                # the comsol title row was not of well defined format to process automatically
                # use mannul setting for now
                pass
            elif i>endOfComment-1:

                aNewComsolLine = comsolLine(titleList)
                aNewComsolLine.setValues(self.splitRowToFloats(line))
                self.comsolLineList.extend([aNewComsolLine])
            
        file_obj.close()

    def splitRowToFloats(self,line):
         return [float(element) for element in line.split()]
            

class SizeDisagreeError(Exception):
    def __init__(self, Msg):
        self.Msg = Msg


class comsolLine:
    
    def __init__(self, nameList):
        self.nameList = nameList
        self.values = [None]*len(self.nameList)

   
    def setValues(self, values):
        self.values = values
#        for ele in self.values:
#            print ele
        if self.checkDimension() == False:
            raise SizeDisagreeError('nameList and values size does not agree !')
        # put data in to python dictionary structure
        self.dataDictionary = {}
        for i, ele in enumerate(self.nameList):
            self.dataDictionary[ele] = self.values[i] 
        #print dataDictionary

    def checkDimension(self):
        #print len(self.values) == len(self.nameList)
        return len(self.values) == len(self.nameList)
            

    
    