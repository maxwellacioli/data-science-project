# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:11:30 2020
@author: Acioli
"""


# import sys
# sys.path.append("../../tools/")
# from preprocess_docentes import preprocess
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

data =  pd.read_csv('../../datasets/dataset-docentes/docentes_dataset.csv', index_col=False, sep=';')
target = data.pop('Situacao')

cargos_df = pd.DataFrame()
cargos = data.pop('Cargo')
cargos_df.insert(0, 'Cargo', cargos)

orgaos_df = pd.DataFrame()
orgaos = data.pop('Orgao')
orgaos_df.insert(0, 'Orgao', orgaos)

enc = preprocessing.OrdinalEncoder()

cargos_df = enc.fit(cargos_df).transform(cargos_df)
orgaos_df = enc.fit(orgaos_df).transform(orgaos_df)

data.insert(0, 'Orgao', orgaos_df)
data.insert(0, 'Cargo', cargos_df)

gnb = GaussianNB()

acc_scor = np.mean(cross_val_score(gnb, data, target, cv=10, scoring='accuracy'))
f1_scor = np.mean(cross_val_score(gnb, data, target, cv=10, scoring='f1_weighted'))

print("Accuracy: {}\n".format(acc_scor) 
       + 
       "F1: {}\n".format(f1_scor)
      )