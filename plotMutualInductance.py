# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 08:45:57 2017

@author: zha200
"""
import scipy.integrate as intergrate
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
import LSRALib as lLib
import comsolLib as cLib
# define the x-axis positions of the mover

def integratedFunc(xList,yList,x1,x2):
    result = intergrate.quad(lambda xIn: interp1d(xList,yList)(xIn), x1, x2 )
    return result[0]


def plotMutualInductanceInFormat(Mab, Mbc, Mac):
    #plot the mutual inductance------------------------
    fontSizeLabel = 20
    fig = plt.figure(figsize = (10,6))
    ax = fig.add_subplot(311)
    ax.plot(Mab.Positions,Mab.Values, 'b')
    ax.set_xlabel('Rotor position (mm)',fontsize = fontSizeLabel)
    ax.set_ylabel(r'$M_{ab}$',fontsize = fontSizeLabel)
    plt.xlim([-2,10])
    plt.gca().axes.get_yaxis().set_ticks([])
    plt.grid()

    ax = fig.add_subplot(312)
    ax.plot(Mbc.Positions,Mbc.Values, 'r')
    ax.set_xlabel('Rotor position (mm)',fontsize = fontSizeLabel)
    ax.set_ylabel(r'$M_{bc}$',fontsize = fontSizeLabel)
    plt.xlim([-2,10])
    plt.gca().axes.get_yaxis().set_ticks([])
    plt.grid()

    ax = fig.add_subplot(313)
    ax.plot(Mac.Positions,Mac.Values, 'k')
    ax.set_xlabel('Rotor position (mm)',fontsize = fontSizeLabel)
    ax.set_ylabel(r'$M_{ac}$',fontsize = fontSizeLabel)
    plt.xlim([-2,10])
    plt.gca().axes.get_yaxis().set_ticks([])
    plt.grid()
    fig.savefig('MutualInductance_Bipolar.png',format = 'png', dpi = 300)
# -----------unipolar operation------------------------------------------
# initialize the mutual inductance
#Mab = lLib.periodicDataStruc('UP_Mab', -2, 10, 200)
#Mbc = lLib.periodicDataStruc('UP_Mbc', -2, 10, 200)
#Mac = lLib.periodicDataStruc('UP_Mac', -2, 10, 200)
#
#Mab.setValues([0,1.81,1.81*2,1.81*3],[1,0,0,1])
#Mbc.setValues([0,1.81,1.81*2,1.81*3],[0,0,1,0])
#Mac.setValues([0,1.81,1.81*2,1.81*3],[0,1,0,0])
#
#plotMutualInductanceInFormat(Mab,Mbc,Mac)
step = 1.813 
# test the integration algorithms of python
# data part 1: one step to the alignment of excited phases
#magForcePart1 = cLib.comsolTxtFile('MutualInductanceForce_part1_MoveTo.txt',['position','VW','MST'])
#positions1 = list()
#VW1 = list()
#MST1 = list()
#for ele in magForcePart1.comsolLineList:
#    positions1.extend([ele.dataDictionary['position']*1000])
#    VW1.extend([ele.dataDictionary['VW']])
#    MST1.extend([ele.dataDictionary['MST']])
#    
## data part 2: one step away from the alignment of the excited phases
#magForcePart1 = cLib.comsolTxtFile('MutualInductanceForce_part2_MoveAway.txt',['position','VW','MST'])
#positions2 = list()
#VW2 = list()
#MST2 = list()
#for ele in magForcePart1.comsolLineList:
#    positions2.extend([ele.dataDictionary['position']*1000])
#    VW2.extend([ele.dataDictionary['VW']])
#    MST2.extend([ele.dataDictionary['MST']])
#    
## data part 3: move 
#magForcePart1 = cLib.comsolTxtFile('MutualInductanceForce_part3_Flat.txt',['position','VW','MST'])
#positions3 = list()
#VW3 = list()
#MST3 = list()
## asseminbing 3 parts 
#
#for ele in magForcePart1.comsolLineList:
#    positions3.extend([ele.dataDictionary['position']*1000])
#    VW3.extend([ele.dataDictionary['VW']])
#    MST3.extend([ele.dataDictionary['MST']]) 
## Assembing for full cycle data (3 steps)
#positions = positions1[:]
#VW = VW1[:]
#for i,ele in enumerate(positions2):
#    positions.extend([ele+step])
#    VW.extend([VW2[i]])
#    
#for i,ele in enumerate(positions3):
#    positions.extend([ele+step*2])
#    VW.extend([VW3[i]])
#    
##-------------------------------------------------------------------------
## one complete period of mutual inductance variation for Mac
#Fac = lLib.periodicDataStruc('Fac', 0, 3*step, 100)
#Fac.setValues(positions,VW)
#MacList = list()
#for i,element in enumerate(Fac.Positions):
#    print i
#    MacList.extend([integratedFunc(Fac.Positions,Fac.Values,Fac.Positions[0],element)])
## extend the mutual inductance into full range for all three phase 
#FullMac = lLib.periodicDataStruc('Mac', -2, 10, 1000)
#FullMac.setValues(Fac.Positions,MacList)

# one complete period of mutual inductance variation for Mab

# extend the mutual inductance into full range for all three phase 
#FullMab = lLib.periodicDataStruc('Mac', -2, 10, 1000)
#FullMab.setValues([ele - 1*step for ele in Fac.Positions],MacList)
#FullMbc = lLib.periodicDataStruc('Mac', -2, 10, 1000)
#FullMbc.setValues([ele + 1*step for ele in Fac.Positions],MacList)
#plotMutualInductanceInFormat(FullMab,FullMbc,FullMac)
#-----------Bipolar operation -------------------------------------------
# initialize the mutual inductance for bipolar

#BP_Mab = lLib.periodicDataStruc('BP_Mab', -2, 10, 200)
#BP_Mbc = lLib.periodicDataStruc('BP_Mbc', -2, 10, 200)
#BP_Mac = lLib.periodicDataStruc('BP_Mac', -2, 10, 200)
#
#BP_Mab.setValues([0,1.81,1.81*2,1.81*3],[0,1,0,0])
#BP_Mbc.setValues([0,1.81,1.81*2,1.81*3],[1,0,0,1])
#BP_Mac.setValues([0,1.81,1.81*2,1.81*3],[0,0,1,0])
#
#plotMutualInductanceInFormat(BP_Mab,BP_Mbc,BP_Mac)

magForcePart1 = cLib.comsolTxtFile('MutualInductanceForce_part1_MoveTo_bi.txt',['position','VW','MST'])
positions1 = list()
VW1 = list()
MST1 = list()
for ele in magForcePart1.comsolLineList:
    positions1.extend([ele.dataDictionary['position']*1000])
    VW1.extend([ele.dataDictionary['VW']])
    MST1.extend([ele.dataDictionary['MST']])
    
# data part 2: one step away from the alignment of the excited phases
magForcePart1 = cLib.comsolTxtFile('MutualInductanceForce_part2_MoveAway_bi.txt',['position','VW','MST'])
positions2 = list()
VW2 = list()
MST2 = list()
for ele in magForcePart1.comsolLineList:
    positions2.extend([ele.dataDictionary['position']*1000])
    VW2.extend([ele.dataDictionary['VW']])
    MST2.extend([ele.dataDictionary['MST']])
    
# data part 3: move 
magForcePart1 = cLib.comsolTxtFile('MutualInductanceForce_part3_Flat_bi.txt',['position','VW','MST'])
positions3 = list()
VW3 = list()
MST3 = list()
# asseminbing 3 parts 

for ele in magForcePart1.comsolLineList:
    positions3.extend([ele.dataDictionary['position']*1000])
    VW3.extend([ele.dataDictionary['VW']])
    MST3.extend([ele.dataDictionary['MST']]) 
# Assembing for full cycle data (3 steps)
positions = positions1[:]
VW = VW1[:]
for i,ele in enumerate(positions2):
    positions.extend([ele+step])
    VW.extend([VW2[i]])
    
for i,ele in enumerate(positions3):
    positions.extend([ele+step*2])
    VW.extend([VW3[i]])
    
#-------------------------------------------------------------------------
# one complete period of mutual inductance variation for Mac
Fab = lLib.periodicDataStruc('Fab', 0, 3*step, 100)
Fab.setValues(positions,VW)
MabList = list()
for i,element in enumerate(Fab.Positions):
    print i
    MabList.extend([integratedFunc(Fab.Positions,Fab.Values,Fab.Positions[0],element)])
# extend the mutual inductance into full range for all three phase 
FullMab = lLib.periodicDataStruc('Mab', -2, 10, 1000)
FullMab.setValues(Fab.Positions,MabList)

# one complete period of mutual inductance variation for Mab

# extend the mutual inductance into full range for all three phase 
FullMac = lLib.periodicDataStruc('Mac', -2, 10, 1000)
FullMac.setValues([ele + 1*step for ele in Fab.Positions],MabList)
FullMbc = lLib.periodicDataStruc('Mbc', -2, 10, 1000)
FullMbc.setValues([ele - 1*step for ele in Fab.Positions],MabList)
plotMutualInductanceInFormat(FullMab,FullMbc,FullMac)