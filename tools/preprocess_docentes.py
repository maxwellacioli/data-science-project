# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:42:20 2020
@author: Acioli
"""


import pandas as pd
import numpy as np

abono_docentes_df = pd.read_csv('../datasets/dataset-docentes/abono_docentes.csv', index_col=False, sep=';')
aposentados_docentes_df = pd.read_csv('../datasets/dataset-docentes/aposentados_docentes.csv', index_col=False, sep=';')

'''#### CREATE A NEW DATAFRAME FROM ABONO AND APOSENTADOS DATASETS ####'''

'''ABONDO'''
abono_name = abono_docentes_df['Nome'].tolist()
abono_cargo = abono_docentes_df['Descrição do cargo emprego'].tolist()
abono_orgao = abono_docentes_df['Denominação unidade organizacional'].tolist()
abono_valor_aux = abono_docentes_df.iloc[:,-1].str.replace(',', '.').astype(float).reset_index(drop=True)

# Calculate abono salario
'''TODO CALCULAR SALARIO: S = (100*A)/11'''
abono_valor = list()
for index, value in abono_valor_aux.items():
    abono_valor.append((100*value)/11)

abono_aux_df = pd.DataFrame()
abono_aux_df['Nome'] = abono_name
abono_aux_df['Cargo'] = abono_cargo
abono_aux_df['Orgao'] = abono_orgao
abono_aux_df['Valor'] = abono_valor 
abono_aux_df['Afastamento'] = 1

'''APOSENTADOS'''
aposentados_nome = aposentados_docentes_df['Nome'].tolist()
aposentados_cargo = aposentados_docentes_df['Cargo emprego'].tolist()
aposentados_orgao = aposentados_docentes_df['Orgao'].tolist()
aposentados_valor = aposentados_docentes_df.iloc[:,-1].str.replace('.', '').reset_index(drop=True)
aposentados_valor = aposentados_valor.str.replace(',', '.').astype(float)


aposentado_aux_df = pd.DataFrame()
aposentado_aux_df['Nome'] = aposentados_nome
aposentado_aux_df['Cargo'] = aposentados_cargo
aposentado_aux_df['Orgao'] = aposentados_orgao
aposentado_aux_df['Valor'] = aposentados_valor
aposentado_aux_df['Afastamento'] = 2

dataframes = [abono_aux_df, aposentado_aux_df]

print(abono_docentes_df['Descrição do cargo emprego'].unique())

# TODO EXCLUIR LINHAS COM VALORES ERRAADOS (NA PORTARIA DEVE TER O SIMBOLO ; -> BUGOU O CSV)

# professor_abono = abono_docentes_df[abono_docentes_df['Nome'].str.contains("EDSON DOS SANTOS MARCHIORI")]
# professor_aposentadoria = aposentados_docentes_df[aposentados_docentes_df['Nome'].str.contains("EDSON DOS SANTOS MARCHIORI")]
# return aposentados_df