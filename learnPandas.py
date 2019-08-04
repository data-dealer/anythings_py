# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 10:58:59 2018

@author: User
"""
import numpy as np
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
# get data
data[1]
data['b']

# data from dict

population_dict = {'California': 38332521,
 'Texas': 26448193,
 'New York': 19651127,
 'Florida': 19552860,
 'Illinois': 12882135}
population = pd.Series(population_dict)

# get data from row to row
population['California':'Illinois']

# create new 
pd.Series({2:'a', 1:'b', 3:'c'})
pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])

#--------------------------------------#

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
 'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)

# create dataframe

states = pd.DataFrame({'population': population,
 'area': area})

states.index
states.columns
states['them']=states['population']*2 # add col
states['area'] # get one attribute
# make dataframe
data = [{'a': i, 'b': 2 * i}
    for i in range(3)]
fr1 = pd.DataFrame(data)
#
pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])

fr2 = pd.DataFrame(np.random.rand(3, 2),
             columns=['foo', 'bar'],
             index=['a', 'b', 'c'])
fr2

# time series -----------------------------------------
dates = pd.to_datetime([ '4th of July, 2015','2015-Jul-6', '07-07-2015', '20150708'])
dates
dates.to_period('D')
pd.date_range('2015-07-03', '2015-07-10')
pd.date_range('2015-07-03', periods=8,freq='3M')

pd.timedelta_range(0, periods=10, freq='H') #hours