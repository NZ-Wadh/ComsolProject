# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 10:53:11 2017

@author: zha200
"""
import LSRALib as lLib
import matplotlib.pyplot as plt
import numpy as np
import math as mt

# plot current waveform for all operational modes
def plotCurrentInFormat(Ia, Ib, Ic):
    #plot the mutual inductance------------------------
    fontSizeLabel = 20
    fig = plt.figure(figsize = (10,6))
    fig.suptitle('MMF (ampere-turns)',fontsize = fontSizeLabel)
    
    ax = fig.add_subplot(311)
    ax.plot(Ia.Positions,Ia.Values, 'b')
    ax.set_xlabel('Rotor position (mm)',fontsize = fontSizeLabel)
    ax.set_ylabel('Phase a',fontsize = fontSizeLabel-6)
    plt.xlim([-2,10])
   # plt.gca().axes.get_yaxis().set_ticks([])
    plt.grid()

    ax = fig.add_subplot(312)
    ax.plot(Ib.Positions,Ib.Values, 'r')
    ax.set_xlabel('Rotor position (mm)',fontsize = fontSizeLabel)
    ax.set_ylabel('Phase b',fontsize = fontSizeLabel-6)
    plt.xlim([-2,10])
   # plt.gca().axes.get_yaxis().set_ticks([])
    plt.grid()

    ax = fig.add_subplot(313)
    ax.plot(Ic.Positions,Ic.Values, 'k')
    ax.set_xlabel('Rotor position (mm)',fontsize = fontSizeLabel)
    ax.set_ylabel('Phase c',fontsize = fontSizeLabel-6)
    plt.xlim([-2,10])
    #plt.gca().axes.get_yaxis().set_ticks([])
    plt.grid()
    fig.savefig('Current_Sino.png',format = 'png', dpi = 300)
# maximum MMF
MMF = 705  
step = 1.813
# Unipolar operation-----------------------------------------------------------
# initializing the currents
#UP_Ia = lLib.periodicDataStruc('Ia', -2, 10, 1000)
#UP_Ib = lLib.periodicDataStruc('Ib', -2, 10, 1000)
#UP_Ic = lLib.periodicDataStruc('Ic', -2, 10, 1000)
#
#UP_Ia.setValues([0, step, step+0.001, step*2, 1.82*2+0.001, step*3], [MMF,MMF,0,0,MMF,MMF])
#UP_Ib.setValues([0, step, step+0.001, step*2, step*3, step*3+0.001],[0,0,MMF,MMF,MMF,0])
#UP_Ic.setValues([0, step, step*2,    step*2+0.001, step*3, step*3+0.001],[MMF,MMF,MMF,0,0,MMF])
#
#plotCurrentInFormat(UP_Ia,UP_Ib,UP_Ic)


# Bipolar operation
# initializing the currents
#BP_Ia = lLib.periodicDataStruc('Ia', -2, 10, 1000)
#BP_Ib = lLib.periodicDataStruc('Ib', -2, 10, 1000)
#BP_Ic = lLib.periodicDataStruc('Ic', -2, 10, 1000)
#
#BP_Ia.setValues([0, step, step*2, 1.82*2+0.001, step*3, step*3+0.001,step*4, step*5, step*5+0.001,step*6,step*6+0.001], [-MMF,-MMF,-MMF, 0, 0, MMF, MMF, MMF, 0,0,0])
#BP_Ib.setValues([0, step, step+0.001, step*2, step*2 + 0.001, step*3, step*4, step*4+0.001,step*5,step*5+0.001, step*6],[MMF,MMF,0,0,-MMF, -MMF, -MMF,0, 0, MMF,MMF])
#BP_Ic.setValues([0, step, step + 0.001, step*2, step*3,step*3+0.001, step*4, step*4+0.001, step*5,  step*6,step*6+0.001],[0,0,MMF,MMF,MMF,0,0,-MMF, -MMF,-MMF, 0])
#
#plotCurrentInFormat(BP_Ia,BP_Ib,BP_Ic)

# sinusoidal opeartion
phi = np.linspace(0,2*mt.pi,200)

phaseA = [((float(1)/2-float(2)/3)*mt.pi+ ele) for ele in phi]
phaseB = [((float(1)/2)*mt.pi+ ele) for ele in phi]
phaseC = [((float(1)/2+float(2)/3)*mt.pi+ ele) for ele in phi]

positionA = [6*step/(2*mt.pi)*ele for ele in phaseA]
positionB = [6*step/(2*mt.pi)*ele for ele in phaseB]
positionC = [6*step/(2*mt.pi)*ele for ele in phaseC]
print max(phi)
print max(phaseA), max(phaseB), max(phaseC)
print max(positionA), max(positionB), max(positionC)

SI_Ia = lLib.periodicDataStruc('Ia', -2, 10, 1000)
SI_Ib = lLib.periodicDataStruc('Ib', -2, 10, 1000)
SI_Ic = lLib.periodicDataStruc('Ic', -2, 10, 1000)
sinWave = [ MMF*ele for ele in np.sin(phi).tolist()]
SI_Ia.setValues(positionA, sinWave )
SI_Ib.setValues(positionB, sinWave)
SI_Ic.setValues(positionC, sinWave)

plotCurrentInFormat(SI_Ia,SI_Ib,SI_Ic)