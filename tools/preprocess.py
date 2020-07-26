# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:41:30 2020
@author: Acioli
"""


import pandas as pd
from sklearn.model_selection import train_test_split
import datetime as dt

def preprocess(file_name='../tools/covid19-al-sintomas.csv'):

    covid_df = pd.read_csv(file_name)