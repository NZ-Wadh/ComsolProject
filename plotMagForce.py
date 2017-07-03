# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 17:40:27 2017

@author: zha200
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:54:47 2017

@author: zha200
"""

import LSRALib as lLib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

#import numpy as np
import comsolLib as cLib

def plotMagForceInFormat(VW, MST):
    #plot the mutual inductance------------------------
    fontSizeLabel = 20
    fig = plt.figure(figsize = (10,5))
    ax = fig.add_subplot(111)
    ax.plot(VW.Positions,VW.Values, 'b')
    ax.plot( MST.Positions, MST.Values,'r')
    VWlegend = mlines.Line2D([],[],color = 'blue', label = 'Virtual Work')
    MSTlegend = mlines.Line2D([],[],color = 'red', label = 'Maxwell Stress Tensor')
    plt.legend(handles = [VWlegend, MSTlegend], loc = 1)
    leg  = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize = 18)

    ax.set_xlabel('Rotor position (mm)',fontsize = fontSizeLabel)
    ax.set_ylabel('Force (N)',fontsize = fontSizeLabel)

    plt.xlim([-2,10])
    #plt.gca().axes.get_yaxis().set_ticks([])
    plt.grid()
    fig.savefig('Magforce_Sino.png',format = 'png', dpi = 300)
#--------------------Plot for Unipolar ------------------------------

#UniPolarForce = cLib.comsolTxtFile('WindingSectionForConferencePaperUniPolar.txt', ['position', 'VW', 'MST'])
#positionList = list()
#VWList = list()
#MSTList = list()
#
#for element in UniPolarForce.comsolLineList:
#    #print 'Position is %f'  %(element.dataDictionary['position'])
#    positionList.extend([element.dataDictionary['position']*1000])
#    VWList.extend([element.dataDictionary['VW']])
#    MSTList.extend([element.dataDictionary['MST']])
#
## plot for unipolar operation
#
#VW_Unipolar = lLib.periodicDataStruc('UnipolarWV', -2, 10, 1000)
#VW_Unipolar.setValues(positionList,VWList)
#
#MST_Unipolar = lLib.periodicDataStruc('UnipolarMST', -2, 10, 1000)
#MST_Unipolar.setValues(positionList,MSTList)
#
#plotMagForceInFormat(VW_Unipolar, MST_Unipolar)

#----------------Plot for Bipolar -----------------------------------

#BiPolarForce = cLib.comsolTxtFile('WindingSectionForConferencePaperBiPolar.txt', ['position', 'VW', 'MST'])
#positionList = list()
#VWList = list()
#MSTList = list()
#
#for element in BiPolarForce.comsolLineList:
#    #print 'Position is %f'  %(element.dataDictionary['position'])
#    positionList.extend([element.dataDictionary['position']*1000])
#    VWList.extend([element.dataDictionary['VW']])
#    MSTList.extend([element.dataDictionary['MST']])
#
## plot for unipolar operation
#
#VW_Bipolar = lLib.periodicDataStruc('BipolarWV', -2, 10, 1000)
#VW_Bipolar.setValues(positionList,VWList)
#
#MST_Bipolar = lLib.periodicDataStruc('BipolarMST', -2, 10, 1000)
#MST_Bipolar.setValues(positionList,MSTList)
#
#plotMagForceInFormat(VW_Bipolar, MST_Bipolar)

#-------------plot for sinusoidal ------------------------------------
SinoForce = cLib.comsolTxtFile('WindingSectionForConferencePaperSin.txt',['position','VW','MST'])
positionList = list()
VWList = list()
MSTList = list()

for element in SinoForce.comsolLineList:
    #print 'Position is %f'  %(element.dataDictionary['position'])
    positionList.extend([element.dataDictionary['position']*1000])
    VWList.extend([element.dataDictionary['VW']])
    MSTList.extend([element.dataDictionary['MST']])

# plot for unipolar operation

VW_Sino = lLib.periodicDataStruc('SinoVW', -2, 10, 1000)
VW_Sino.setValues(positionList,VWList)

MST_Sino = lLib.periodicDataStruc('SinoMST', -2, 10, 1000)
MST_Sino.setValues(positionList,MSTList)

plotMagForceInFormat(VW_Sino, MST_Sino)