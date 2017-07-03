# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 08:45:57 2017

@author: zha200
"""
import LSRALib as lLib
import matplotlib.pyplot as plt
# define the x-axis positions of the mover

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

#-----------Bipolar operation -------------------------------------------
# initialize the mutual inductance for bipolar

BP_Mab = lLib.periodicDataStruc('BP_Mab', -2, 10, 200)
BP_Mbc = lLib.periodicDataStruc('BP_Mbc', -2, 10, 200)
BP_Mac = lLib.periodicDataStruc('BP_Mac', -2, 10, 200)

BP_Mab.setValues([0,1.81,1.81*2,1.81*3],[0,1,0,0])
BP_Mbc.setValues([0,1.81,1.81*2,1.81*3],[1,0,0,1])
BP_Mac.setValues([0,1.81,1.81*2,1.81*3],[0,0,1,0])

plotMutualInductanceInFormat(BP_Mab,BP_Mbc,BP_Mac)