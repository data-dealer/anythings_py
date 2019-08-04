# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:29:07 2018

@author: User
"""

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdate
import numpy as np


def graphRawFX():
    date,bid,ask = np.loadtxt('GBPUSD1d.txt',unpack = True, 
                              delimiter = ',',
                              converters = {0: mdate.strpdate2num('%Y%m%d%')})
                              
    fig = plt.figure(figsize = (10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan= 40 , colspan= 40)
    
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    
    ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.grid(True)
    plt.show()
    