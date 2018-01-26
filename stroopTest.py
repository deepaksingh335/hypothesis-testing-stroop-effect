# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:49:52 2018

@author: singhd5
"""
import pandas as pd
from scipy import stats

df=pd.read_csv('stroopdata.csv')
print(df)
desc=df.describe()
print ("\nSome descriptive statistics of the data shown below:\n\n",desc)
range=df.max()-df.min()
print ("\nThe range for congruent and incongruent data is:\n\n",range)

# Build the visualizations here

df.plot.box() #Fig1
df.hist()     #Fig2
df.plot.kde() #Fig3

# Perform the statistical test here
paired_ttest=stats.ttest_rel(df['Congruent'], df['Incongruent'])
print (paired_ttest)