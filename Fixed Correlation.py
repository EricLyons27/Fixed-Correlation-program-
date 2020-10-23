#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 01:08:15 2020

@author: ericlyons
"""

import numpy as np 
import scipy
from scipy import stats
import imageio
import matplotlib.pyplot as pl

image1 = (imageio.imread('(0).tif'))
x1 = np.array([i for i in range(6000)])
y1 = 4000 - np.argmax(image1, axis=0)

corre1 = []


for i in range(1812): # two values below the range of contact line so there are at least two points 
    y = []
    ydx = []
    for u in range(1814): # range of contact line 
        dx=i
        bg= 2718 #where contact line starts on image 
        z = u + bg
        t = u + bg + dx
        if u<1814-dx: #will stop the code once x + dx reaches the end of the contact line 
            m = y1[z]
            n = y1[t]
            if m != 4000 and n != 4000:
                 y.append(m)
                 ydx.append(n)  
        else:
            break
    b = scipy.stats.pearsonr(y,ydx) 
    corre1.append(b[0]) #creates array of correaltion for every dx 

dx1 = np.array([i for i in range(len(corre1))])    

fig, ax = pl.subplots(figsize = (12,9))
pl.plot(dx1,corre1,'r-',label = '0 Seconds')
pl.xlim(0,2000)
pl.ylim(-1,1)
pl.title('Correlation vs dx')  
pl.xlabel('dx')
pl.ylabel('Correlation')
ax.axhline(0, color='black', linewidth=1)
pl.grid()
pl.legend(loc = 'lower left')
