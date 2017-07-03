# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:52:21 2017

@author: zha200
"""
# work still to do
# add comments
# write method for user to format the printed figures
# write exception/error messages

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


class periodicDataStruc:
    
    
    def __init__(self, phaseName, startPos, endPos, numSteps ):
        
        self.Positions = np.linspace(startPos,endPos, numSteps)

        self.name = phaseName
        self.Values = self.Positions*0
    
    # set the shape of M by defining 
    def setValues(self, positions, values):
        # insert code to check if positions are increasing in value
        #
        #
        # repeat the shape over the range
        partPositions = positions[:]
        partValues = values[:]
        periodSize = positions[-1]-positions[0]

        # repeat the pattern for the whole range (min(Positions),max(Positions))
        indexAdd = 1
        indexExa = 1
        while (partPositions[-1]) < max(self.Positions):
              
              for i in range (1, len(positions)):
                  partPositions.extend([positions[i]+periodSize*indexAdd])
                  partValues.extend([values[i]])
              indexAdd = indexAdd+1
          
        while(partPositions[0]) > min(self.Positions):
              for i in range (1, len(positions)):
                 
                  partPositions.insert(0,positions[len(positions)-i-1]-periodSize*indexExa)
                 
                  partValues.insert(0,values[len(positions)-i-1])
                  
              indexExa = indexExa +1
              
        # interpolation 1D
        Mfunc = interp1d(partPositions, partValues)
        self.Values = Mfunc(self.Positions)
        #plt.plot(partPositions, partValues)
        
    def plotData(self,lineColor,title):
        
        fig = plt.figure(figsize = (10,3.3))
        ax = fig.add_subplot(111)
        ax.plot(self.Positions,self.Values, lineColor)
        ax.set_xlabel('Rotor position (mm)',fontsize = 10)
        ax.set_ylabel(title,fontsize = 12)
        #plt.gca().axes.get_yaxis().set_ticks([])
        plt.grid()
        plt.xlim([min(self.Positions),max(self.Positions)])
        return fig
        
    def saveImage(self, lineColor, figName, figFormat):
        
        self.plotData(lineColor).savefig(figName, format = figFormat, dpi = 300)