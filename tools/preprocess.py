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
# return aposentados_df