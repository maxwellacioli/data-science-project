#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:28:43 2020

@author: helynne
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind


data =  pd.read_csv('../datasets/dataset-docentes/docentes_dataset.csv', index_col=False, sep=';')

# print( data[["Meses", "Salario"]].describe() )

''' SITUACAO '''

# Scatter plots by class
df_abono = data[data['Situacao'] == 1]
df_aposentados = data[data['Situacao'] != 1]
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

''' CARGO '''

# # # Scatter plots by Cargo
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

# # # All scatterplots

data_sctt_prof = data.iloc[:, 0:4]
sns.set(style="ticks")
sns.pairplot(data_sctt_prof, hue="Cargo")

data_sctt_sit = data.iloc[:, 2:5]
sns.set(style="ticks")
sns.pairplot(data_sctt_sit, hue="Situacao")

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

''' SALARIOS AND MESES '''

salario = data['Salario']
meses = data['Meses']

salario_prof_bas_tec = df_prof_bas_tec['Salario']
meses_prof_bas_tec = df_prof_bas_tec['Meses']

salario_prof_superior = df_prof_superior['Salario']
meses_prof_superior = df_prof_superior['Meses']

salario_abono = df_abono['Salario']
meses_abono = df_abono['Meses']

salario_avoluntario = df_avoluntario['Salario']
meses_avoluntario = df_avoluntario['Meses']

salario_acompulsorio = df_acompulsorio['Salario']
meses_acompulsorio = df_acompulsorio['Meses']

salario_aposentados = df_aposentados['Salario']
meses_aposentados = df_aposentados['Meses']

''' T TESTS ''' 

# A média dos salários dos professores do ensino superior é maior que a média dos salários dos
# professorres do ensino técnico.

# H0: Os professores do ensino técnico tem salário maior ou igual que os do ensino superior
# HA: Os professores do ensino técnico tem salário menor que os do ensino superior

def compare_2_groups(arr_1, arr_2, alpha= 0.05):
    stat, p = ttest_ind(arr_1, arr_2)
    print('\n\nStatistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Same distributions (fail to reject H0)')
    else:
        print('Different distributions (reject H0)')

compare_2_groups(salario_prof_bas_tec, salario_prof_superior)

plt.figure()
ax1 = sns.distplot(salario_prof_bas_tec, color= 'b')
ax2 = sns.distplot(salario_prof_superior, color= 'r')

plt.axvline(np.mean(salario_prof_bas_tec), color='b', linestyle='dashed', linewidth=2)
plt.axvline(np.mean(salario_prof_superior), color='r', linestyle='dashed', linewidth=2)

# A média do salário de quem se aposenta de forma compulsória é maior do que a média do 
# salário de quem se aposenta de forma voluntária

# H0: Os professores aposentados voluntários tem salário maior ou igual que os compulsorios
# HA: Os professores aposentados voluntários tem salário menor que os compulsorios

compare_2_groups(salario_avoluntario, salario_acompulsorio)

plt.figure()
ax1 = sns.distplot(salario_avoluntario, color= 'b')
ax2 = sns.distplot(salario_acompulsorio, color= 'r')

plt.axvline(np.mean(salario_avoluntario), color='b', linestyle='dashed', linewidth=2)
plt.axvline(np.mean(salario_acompulsorio), color='r', linestyle='dashed', linewidth=2)

# A média do salário de quem recebe abono é maior do que a média do 
# salário de quem se aposenta

# H0: Os professores aposentados tem salário maior ou igual que professores que recebem abono
# HA: Os professores aposentados tem salário menor que professores que recebem abono

compare_2_groups(salario_aposentados, salario_abono)

plt.figure()
ax1 = sns.distplot(salario_aposentados, color= 'b')
ax2 = sns.distplot(salario_abono, color= 'r')

plt.axvline(np.mean(salario_aposentados), color='b', linestyle='dashed', linewidth=2)
plt.axvline(np.mean(salario_abono), color='r', linestyle='dashed', linewidth=2)
