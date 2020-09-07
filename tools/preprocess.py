# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:41:30 2020
@author: Acioli
"""


import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
# import datetime as dt

# def preprocess():

'''#### LOAD APOSENTADOS DATASET ####'''
aposentados_df1 = pd.read_csv('../datasets/dataset-aposentados/APOSENTADOS_052020_FULL_PARTE_1.csv', sep=';', encoding='ISO-8859-1', dtype='unicode')
aposentados_df2 = pd.read_csv('../datasets/dataset-aposentados/APOSENTADOS_052020_FULL_PARTE_2.csv', sep=';', encoding='ISO-8859-1', dtype='unicode')

dataframes = [aposentados_df1, aposentados_df2]

aposentados_df = pd.concat(dataframes)

row_index_column_error2_not_nan =  np.where(aposentados_df['Column Error2'].notnull())[0]

aposentados_df = aposentados_df.drop(row_index_column_error2_not_nan)

aposentados_df = aposentados_df.drop(columns=['Column Error2'])

row_index_column_error1_not_nan =  np.where(aposentados_df['Column Error1'].notnull())[0]

for i in row_index_column_error1_not_nan:
    if i in aposentados_df.index:
        aposentados_df = aposentados_df.drop(i)
    
aposentados_df = aposentados_df.drop(columns=['Column Error1'])

aposentados_docentes_df = aposentados_df[aposentados_df['Cargo emprego'].str.contains("PROFESSOR")]


'''#### LOAD ABONO DATASET ####'''

abono_df = pd.read_csv('../datasets/dataset-abono-permanencia/ABONOP_062020.csv', index_col=False, sep=';', encoding='ISO-8859-1', dtype='unicode')

abono_docentes_df = abono_df[abono_df['Descrição do cargo emprego'].str.contains("PROFESSOR")]

'''#### CREATE A NEW DATAFRAME FROM ABONO AND APOSENTADOS DATASETS ####'''

'''ABONDO'''
abono_name = abono_docentes_df['Nome'].tolist()
abono_cpf = abono_docentes_df['CPF'].tolist()
abono_cargo = abono_docentes_df['Descrição do cargo emprego'].tolist()
abono_orgao = abono_docentes_df['Denominação unidade organizacional'].tolist()
# abono_uf = abono_docentes_df['UF da Redidência'].tolist()
abono_valor = abono_docentes_df['Val'].tolist()

abono_aux_df = pd.DataFrame()
abono_aux_df['Nome'] = abono_name
abono_aux_df['CPF'] = abono_cpf
abono_aux_df['Cargo'] = abono_cargo
abono_aux_df['Orgao'] = abono_orgao
abono_aux_df['Valor'] = abono_valor
abono_aux_df['Afastamento'] = 1

'''APOSENTADOS'''
aposentados_nome = aposentados_docentes_df['Nome'].tolist()
# aposentados_cpf = aposentados_docentes_df['CPF'].tolist()
aposentados_cargo = aposentados_docentes_df['Cargo emprego'].tolist()
aposentados_orgao = aposentados_docentes_df['Orgao'].tolist()
# aposentados_uf = aposentados_docentes_df[''].tolist()
aposentados_valor = aposentados_docentes_df['Valor aposentadoria'].tolist()

aposentado_aux_df = pd.DataFrame()
aposentado_aux_df['Nome'] = aposentados_nome
# aposentado_aux_df['CPF'] = aposentados_cpf
aposentado_aux_df['Cargo'] = aposentados_cargo
aposentado_aux_df['Orgao'] = aposentados_orgao
aposentado_aux_df['Valor'] = aposentados_valor
aposentado_aux_df['Afastamento'] = 2

dataframes = [abono_aux_df, aposentado_aux_df]

abono_aposentados_df = pd.concat(dataframes)

# professor_abono = abono_docentes_df[abono_docentes_df['Nome'].str.contains("EDSON DOS SANTOS MARCHIORI")]
# professor_aposentadoria = aposentados_docentes_df[aposentados_docentes_df['Nome'].str.contains("EDSON DOS SANTOS MARCHIORI")]
# return aposentados_df