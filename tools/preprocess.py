# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:41:30 2020
@author: Acioli
"""


import pandas as pd
# from sklearn.model_selection import train_test_split
# import datetime as dt

# def preprocess():
# aposentados_file='../datasets/dataset-aposentados/APOSENTADOS_052020_FULL_PARTE_1.csv'
aposentados_df = pd.read_csv('../datasets/dataset-aposentados/APOSENTADOS_052020_FULL_PARTE_1.csv', error_bad_lines=False, encoding="utf-8")
    
# return aposentados_df