# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:11:30 2020
@author: Acioli
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

df =  pd.read_csv('../../datasets/dataset-abono-date/abono_date.csv', parse_dates=['date'], index_col='date')

def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

plot_df(df, x=df.index, y=df.value, title='Abonos')    


df['year'] = [d.year for d in df.index]
df['month'] = [d.strftime('%b') for d in df.index]
years = df['year'].unique()

# Prep Colors
np.random.seed(100)
mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)

# Draw Plot
plt.figure(figsize=(16,12), dpi= 80)
for i, y in enumerate(years):
    if i > 0:     
        plt.plot('month', 'value', data=df.loc[df.year==y, :], color=mycolors[i], label=y)
        plt.text(df.loc[df.year==y, :].shape[0]-.9, df.loc[df.year==y, 'value'][-1:].values[0], y, fontsize=12, color=mycolors[i])

# Decoration
plt.gca().set(xlim=(-0.3, 11), ylim=(2, 1000000), ylabel='$Abono$', xlabel='$Meses$')
plt.yticks(fontsize=12, alpha=.7)
plt.title("Sazonalidade da Série Temporal de Gastos com Abono", fontsize=20)
plt.show()

result_mul = seasonal_decompose(df['value'], model='multiplicative', extrapolate_trend='freq', period=12)

# Plot
# plt.rcParams.update({'figure.figsize': (10,10)})
result_mul.plot().suptitle('Decomposição da Série Temporal', fontsize=16)
plt.show()