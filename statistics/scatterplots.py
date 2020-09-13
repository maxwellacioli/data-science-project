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

# Scatter plots by class
df_abono = data[data['Situacao'] == 1]
df_avoluntario = data[data['Situacao'] == 2]
df_acompulsorio = data[data['Situacao'] == 3]

plt.scatter(df_abono["Meses"], df_abono["Salario"], s=1, c='b', alpha=0.5)
plt.title('Dispersão Meses X Salário - Abono permanência')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_ap.png", bbox_inches='tight', dpi=300)
plt.show()

plt.scatter(df_avoluntario["Meses"], df_avoluntario["Salario"], s=1, c='r', alpha=0.5)
plt.title('Dispersão Meses X Salário - Aposentadoria voluntária')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_av.png", bbox_inches='tight', dpi=300)
plt.show()

plt.scatter(df_acompulsorio["Meses"], df_acompulsorio["Salario"], s=1, c='g', alpha=0.5)
plt.title('Dispersão Meses X Salário - Aposentadoria compulsória')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_ac.png", bbox_inches='tight', dpi=300)
plt.show()

# Scatterplots plots by class without outliers
df_abono60 = df_abono[df_abono['Salario'] <60000]

plt.scatter(df_abono60["Meses"], df_abono60["Salario"], s=1, c='b', alpha=0.5)
plt.title('Dispersão Meses X Salário - Abono permanência, com salário < 60000')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_ap60.png", bbox_inches='tight', dpi=300)
plt.show()

df_avoluntario50 = df_avoluntario[df_avoluntario['Salario'] <50000]

plt.scatter(df_avoluntario50["Meses"], df_avoluntario50["Salario"], s=1, c='r', alpha=0.5)
plt.title('Dispersão Meses X Salário - Aposentadoria voluntária, com salário < 50000')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_av50.png", bbox_inches='tight', dpi=300)
plt.show()

''' CARGO '''

# Scatter plots by Cargo
df_prof_bas_tec = data[data['Cargo'] == "PROFESSOR ENS BASICO TECN TECNOLOGICO"]
df_prof_superior = data[data['Cargo'] == "PROFESSOR DO MAGISTERIO SUPERIOR"]

plt.scatter(df_prof_bas_tec["Meses"], df_prof_bas_tec["Salario"], s=1, c='b', alpha=0.5)
plt.title('Dispersão Meses X Salário - Professores Ens Básico Tecn Tecnológico')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_prof_bas_tec.png", bbox_inches='tight', dpi=300)
plt.show()

plt.scatter(df_prof_superior["Meses"], df_prof_superior["Salario"], s=1, c='r', alpha=0.5)
plt.title('Dispersão Meses X Salário - Professores do Magistério Superior')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_prof_superior.png", bbox_inches='tight', dpi=300)
plt.show()

# Scatterplots plots by class without outliers
df_prof_bas_tec50 = df_prof_bas_tec[df_prof_bas_tec['Salario'] <60000]

plt.scatter(df_prof_bas_tec50["Meses"], df_prof_bas_tec50["Salario"], s=1, c='b', alpha=0.5)
plt.title('Dispersão Meses X Salário - Professores Ens Básico Tecn Tecnológico, com salário < 50000')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_prof_bas_tec50.png", bbox_inches='tight', dpi=300)
plt.show()

df_prof_superior60 = df_prof_superior[df_prof_superior['Salario'] <60000]

plt.scatter(df_prof_superior60["Meses"], df_prof_superior60["Salario"], s=1, c='r', alpha=0.5)
plt.title('Dispersão Meses X Salário - Professores do Magistério Superior, com salário < 60000')
plt.xlabel('Meses')
plt.ylabel('Salário')
plt.savefig("graphics/dipersao_prof_superior60.png", bbox_inches='tight', dpi=300)
plt.show()

# All scatterplots
data60 = data[data['Salario'] < 60000]
data60sctt_prof = data60.iloc[:, 0:4]
sns.set(style="ticks")
sns.pairplot(data60sctt_prof, hue="Cargo")

data60sctt_sit = data60.iloc[:, 2:5]
sns.set(style="ticks")
sns.pairplot(data60sctt_sit, hue="Situacao")

'''CORRELATION AND SUMMARY '''

print("\n\nMatriz de correlação dos dados")
data_numeric = data.iloc[:, 2:4]
corr = data_numeric.corr()
print(corr)

print("\n\nEstatísticas dos dados")
print( data[["Meses", "Salario"]].describe() )

print("\n\nEstatísticas da Classe Abono Permanência")
print( df_abono[["Meses", "Salario"]].describe() )
print("\n\nEstatísticas da Classe Aposentadoria Voluntária")
print( df_avoluntario[["Meses", "Salario"]].describe() )
print("\n\nEstatísticas da Classe Aposentadoria Compulsória")
print( df_acompulsorio[["Meses", "Salario"]].describe() )

print("\n\nEstatísticas dos Professores de Ens Básico Tecn Tecnológico")
print( df_prof_bas_tec[["Meses", "Salario"]].describe() )
print("\n\nEstatísticas dos Professores do Magistério Superior")
print( df_prof_superior[["Meses", "Salario"]].describe() )




