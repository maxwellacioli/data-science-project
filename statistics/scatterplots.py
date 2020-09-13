#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:28:43 2020

@author: helynne
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data =  pd.read_csv('../datasets/dataset-docentes/docentes_dataset.csv', index_col=False, sep=';')

print( data[["Meses", "Salario"]].describe() )

df_abono = data[data['Situacao'] == 1]
df_avoluntario = data[data['Situacao'] == 2]
df_acompulsorio = data[data['Situacao'] == 3]

# Scatter plots by class
plt.scatter(df_abono["Meses"], df_abono["Salario"], s=1, c='b', alpha=0.5)
plt.title('Dispersão Meses X Salário - Abono permanência')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_ap.png", dpi=300)
plt.show()

plt.scatter(df_avoluntario["Meses"], df_avoluntario["Salario"], s=1, c='r', alpha=0.5)
plt.title('Dispersão Meses X Salário - Aposentadoria voluntária')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_av.png", dpi=300)
plt.show()

plt.scatter(df_acompulsorio["Meses"], df_acompulsorio["Salario"], s=1, c='g', alpha=0.5)
plt.title('Dispersão Meses X Salário - Aposentadoria compulsória')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_ac.png", dpi=300)
plt.show()


# Scatterplots without outliers
df_abono = df_abono[df_abono['Salario'] <60000]

plt.scatter(df_abono["Meses"], df_abono["Salario"], s=1, c='b', alpha=0.5)
plt.title('Dispersão Meses X Salário - Abono permanência, com salário < 60000')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_ap60.png", dpi=300)
plt.show()

df_avoluntario = df_avoluntario[df_avoluntario['Salario'] <50000]

plt.scatter(df_avoluntario["Meses"], df_avoluntario["Salario"], s=1, c='r', alpha=0.5)
plt.title('Dispersão Meses X Salário - Aposentadoria voluntária, com salário < 50000')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_av.png", dpi=300)
plt.show()

data60 = data[data['Salario'] <60000]

datacov = data.iloc[:, 2:5]
cov = datacov.cov()
print(cov)

sns.set(style="ticks")
sns.pairplot(datacov, hue="Situacao")