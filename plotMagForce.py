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
#import numpy as np
import comsolLib as cLib



#line1 = comsolLine(['position', 'VW', 'MST'])
#line1.setValues([1,2,3])
#print line1.checkDimension()

BiPolarForce = cLib.comsolTxtFile('WindingSectionForConferencePaperBiPolar.txt', ['position', 'VW', 'MST'])
positionList = list()
VWList = list()
MSTList = list()

for element in BiPolarForce.comsolLineList:
    #print 'Position is %f'  %(element.dataDictionary['position'])
    positionList.extend([element.dataDictionary['position']*1000])
    VWList.extend([element.dataDictionary['VW']])
    MSTList.extend([element.dataDictionary['MST']])
    
# define the x-axis positions of the mover

VW_Bipolar = lLib.periodicDataStruc('BipolarMagForce', -2, 10, 200)
VW_Bipolar.setValues(positionList,VWList)
VW_Bipolar.plotData('r','VW')

