# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 10:43:48 2017

@author: zha200
"""
import scipy.integrate as intergrate
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
import LSRALib as lLib
import comsolLib as cLib

def figplot(x,y):
    fontSizeLabel = 20
    fig = plt.figure(figsize = (10,5))
    ax = fig.add_subplot(111)
    ax.plot(x,y, 'b')
    ax.set_xlabel('Rotor position (mm)',fontsize = fontSizeLabel)
    ax.set_ylabel(r'$M_{ac}$',fontsize = fontSizeLabel)
    plt.xlim([-2,10])
    plt.gca().axes.get_yaxis().set_ticks([])
    plt.grid()

#def integrand(x):
#    return 2*x + x*x
#def integratedAna(x):
#    return x*x + float(1)/3*x*x*x

def integratedFunc(xList,yList,x1,x2):
    result = intergrate.quad(lambda xIn: interp1d(xList,yList)(xIn), x1, x2 )
    return result[0]

step = 1.813 
# test the integration algorithms of python
# data part 1: one step to the alignment of excited phases
magForcePart1 = cLib.comsolTxtFile('MutualInductanceForce_part1_MoveTo.txt',['position','VW','MST'])
positions1 = list()
VW1 = list()
MST1 = list()
for ele in magForcePart1.comsolLineList:
    positions1.extend([ele.dataDictionary['position']*1000])
    VW1.extend([ele.dataDictionary['VW']])
    MST1.extend([ele.dataDictionary['MST']])
    
figplot(positions1,VW1)
  
# data part 2: one step away from the alignment of the excited phases
magForcePart1 = cLib.comsolTxtFile('MutualInductanceForce_part2_MoveAway.txt',['position','VW','MST'])
positions2 = list()
VW2 = list()
MST2 = list()
for ele in magForcePart1.comsolLineList:
    positions2.extend([ele.dataDictionary['position']*1000])
    VW2.extend([ele.dataDictionary['VW']])
    MST2.extend([ele.dataDictionary['MST']])
    

# data part 3: move 
magForcePart1 = cLib.comsolTxtFile('MutualInductanceForce_part3_Flat.txt',['position','VW','MST'])
positions3 = list()
VW3 = list()
MST3 = list()
for ele in magForcePart1.comsolLineList:
    positions3.extend([ele.dataDictionary['position']*1000])
    VW3.extend([ele.dataDictionary['VW']])
    MST3.extend([ele.dataDictionary['MST']]) 
figplot(positions3,VW3)


# Assembing for full cycle data (3 steps)
positions = positions1[:]
VW = VW1[:]
for i,ele in enumerate(positions2):
    positions.extend([ele+step])
    VW.extend([VW2[i]])
    
for i,ele in enumerate(positions3):
    positions.extend([ele+step*2])
    VW.extend([VW3[i]])
    
figplot(positions,VW)

# intergration the force function to get the mutual inducatance
# interpolate the force function
Fab = lLib.periodicDataStruc('Mab', 0, 3*step, 100)
Fab.setValues(positions,VW)
Mab = list()

for i,element in enumerate(Fab.Positions):
    print i
    Mab.extend([integratedFunc(Fab.Positions,Fab.Values,Fab.Positions[0],element)])
    
FullMab = lLib.periodicDataStruc('Mab', -2, 10, 1000)
FullMab.setValues(Fab.Positions,Mab)
figplot(FullMab.Positions,FullMab.Values)

## integrate the force function to get the mutual inductance
#xList = np.linspace(0,10,10).tolist()
#yList = list()
#yListAna = list()
#for i,element in enumerate(xList):
#    
#    yList.extend([integratedFunc(0,element)])
#    yListAna.extend([integratedAna(element)])
#    
#figplot(xList,yList)
#figplot(xList,yListAna)