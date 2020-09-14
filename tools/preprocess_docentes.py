# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:42:20 2020
@author: Acioli
"""


import pandas as pd
from datetime import datetime

def diff_month(d1, d2):
    months = abs((d1.year - d2.year) * 12 + d1.month - d2.month)
    if(d1.day > d2.day):
        months-=1
    return months

# def preprocess():
abono_docentes_df = pd.read_csv('../datasets/dataset-docentes/abono_docentes.csv', index_col=False, sep=';')
aposentados_docentes_df = pd.read_csv('../datasets/dataset-docentes/aposentados_docentes.csv', index_col=False, sep=';', low_memory=False)

# TODO GRAFICOS COM OS DADOS, QUANTIDADE DE PROFESSORES E ETC...

# Remove rows out of interest
index_to_remove_abono_df = []

for index, row in abono_docentes_df.iterrows():
    cargo = row['Descrição do cargo emprego'].strip()
    orgao = row['Denominação do órgão de atuação'].strip()

    if(cargo == "PROFESSOR DE 1  E 2  GRAUS" and orgao.startswith('INSTITUTO FEDERAL')):
        abono_docentes_df.at[index, 'Descrição do cargo emprego'] = "PROFESSOR ENS BASICO TECN TECNOLOGICO"
    elif(not(cargo == "PROFESSOR ENS BASICO TECN TECNOLOGICO" or cargo == "PROFESSOR DO MAGISTERIO SUPERIOR")):
        index_to_remove_abono_df.append(index)

abono_docentes_df.drop(abono_docentes_df.index[index_to_remove_abono_df], inplace=True )

index_to_remove_aposentados_df = []

for index, row in aposentados_docentes_df.iterrows():
        
    cargo = row['Cargo emprego'].strip()
    orgao = row['Orgao'].strip()
        
    if(cargo.strip() == "PROFESSOR DE 1  E 2  GRAUS" and orgao.startswith('INSTITUTO FEDERAL')):
        aposentados_docentes_df.at[index, 'Cargo emprego'] = "PROFESSOR ENS BASICO TECN TECNOLOGICO"
    elif(cargo == "PROFESSOR 3 GRAU"):
        aposentados_docentes_df.at[index, 'Cargo emprego'] = "PROFESSOR DO MAGISTERIO SUPERIOR"
    elif(cargo == "PROFESSOR DE ENSINO SUPERIOR"):
        aposentados_docentes_df.at[index, 'Cargo emprego'] = "PROFESSOR DO MAGISTERIO SUPERIOR"
    elif(not(cargo == "PROFESSOR ENS BASICO TECN TECNOLOGICO" or cargo == "PROFESSOR DO MAGISTERIO SUPERIOR")):
        index_to_remove_aposentados_df.append(index)
        
aposentados_docentes_df.drop(aposentados_docentes_df.index[index_to_remove_aposentados_df], inplace=True )
    

#  Remove column out of interest

remove_col_from_aposentados = ['Nome', 'CPF', 'Matricula', 'Sigla Orgao',  'Orgao vinculacao',
                                'Classe', 'Padrao', 'Referencia', 'Nivel', 'Fund legal aposentadoria',
                                'Portaria aposentadoria', 'Nome ocorrencia']

remove_col_from_abono = ['Nome', 'CPF', 'Nível de Escolaridade', 'UF da UPAG de vinculação',
        'Denominação unidade organizacional', 'UF da Residência','Cidade da residência']

aposentados_docentes_df = aposentados_docentes_df.drop(columns=remove_col_from_aposentados)
abono_docentes_df = abono_docentes_df.drop(columns=remove_col_from_abono)

abono_docentes_df = abono_docentes_df.reset_index(drop=True)
aposentados_docentes_df = aposentados_docentes_df.reset_index(drop=True)

abono_date_list = []
abono_val_list = []

for index, row in abono_docentes_df.iterrows():
    val_str = str(row['Val']).replace(',', '.')
    val = float(val_str)
    if(val >= 317.26 and val <= 4322.23):
        abono_val_list.append(val)
        
        date = str(row['Ano/Mês inicial do abono de permanência'])
        y, m = int(date[0:4]), int(date[4:6])
        abono_date = datetime(y,m,1)
        abono_date_list.append(abono_date)
    
abono_date_df = pd.DataFrame()
abono_date_df.insert(0, 'value', abono_val_list)
abono_date_df.insert(0, 'date', abono_date_list)

abono_date_df = abono_date_df.groupby('date')['value'].sum()

abono_date_df.to_csv(r'abono_date.csv') 

# Calculate number of months
table_date = datetime(2020, 6, 30)
for index, row in abono_docentes_df.iterrows():
    years = int(row['Quantidade de anos no Serviço público'])
    months = int(row['Quantidade de meses no Serviço público']) 
    months = years*12 + months
    
    date = str(row['Ano/Mês inicial do abono de permanência'])
    y, m = int(date[0:4]), int(date[4:6])
    abono_date = datetime(y,m,1)
    
    months -= diff_month(abono_date, table_date)
    abono_docentes_df.at[index, 'Quantidade de meses no Serviço público'] = months
   
    status = str(row['Situação servidor']).strip()
    abono_docentes_df.at[index, 'Situação servidor'] = status
   
    
# Remove year and date column
abono_docentes_df = abono_docentes_df.drop(columns=['Quantidade de anos no Serviço público'])
abono_docentes_df = abono_docentes_df.drop(columns=['Ano/Mês inicial do abono de permanência'])

index_to_remove_aposentados_df = []
for index, row in aposentados_docentes_df.iterrows():
    
    date1 = str(row['Dt ingresso servico publico']).strip()
    date2 = str(row['Dt ocorrencia inatividade']).strip()
    
    if(date1 == '' or date2 == ''):
        index_to_remove_aposentados_df.append(index)
    
    else:
        d1, m1, y1 = int(date1[0:2]), int(date1[2:4]), int(date1[4:8])
        d2, m2, y2 = int(date2[0:2]), int(date2[2:4]), int(date2[4:8])        
        months = diff_month(datetime(y1,m1,d1), datetime(y2,m2,d2))    
        aposentados_docentes_df.at[index, 'Dt ingresso servico publico'] = int(months)
        
    if(months <= 0):
        index_to_remove_aposentados_df.append(index)
        
    status = str(row['Tipo aposentadoria']).strip()
    aposentados_docentes_df.at[index, 'Tipo aposentadoria'] = status
        
aposentados_docentes_df.drop(aposentados_docentes_df.index[index_to_remove_aposentados_df], inplace=True )
        
# Remane month column
aposentados_docentes_df = aposentados_docentes_df.rename(columns = {'Dt ingresso servico publico': 'Meses'}, inplace = False)
# Remove the other data column
aposentados_docentes_df = aposentados_docentes_df.drop(columns=['Dt ocorrencia inatividade'])


# '''#### CREATE A NEW DATAFRAME FROM ABONO AND APOSENTADOS DATASETS ####'''

# '''ABONO columns casting'''
abono_docentes_df["Val"] = abono_docentes_df.iloc[:,-1].str.replace(',', '.').astype(float).reset_index(drop=True)

# '''Aponsentados Valor column casting'''
aposentados_docentes_df["Meses"] = aposentados_docentes_df["Meses"].astype(object).astype(int)
aposentados_valor = aposentados_docentes_df.iloc[:,-1].str.replace('.', '').reset_index(drop=True)
aposentados_docentes_df["Valor aposentadoria"] = aposentados_valor.str.replace(',', '.').astype(float)

# Calculate abono salario
'''TODO CALCULAR SALARIO: S = (100*A)/11'''
for index, value in abono_docentes_df["Val"].items():
    abono_docentes_df.at[index, 'Val'] = (100*value)/11
    
# Rename columns Aposentados
aposentados_docentes_df = aposentados_docentes_df.rename(columns =
                                                          {'Cargo emprego': 'Cargo', 
                                                          'Tipo aposentadoria': 'Situacao',
                                                          'Valor aposentadoria': 'Salario'},
                                                          inplace = False)
# Rename columns Abono
abono_docentes_df = abono_docentes_df.rename(columns =
                                                          {'Descrição do cargo emprego': 'Cargo', 
                                                          'Denominação do órgão de atuação': 'Orgao',
                                                          'Situação servidor': 'Situacao',
                                                          'Quantidade de meses no Serviço público': 'Meses',
                                                          'Val': 'Salario'},
                                                          inplace = False)
columnsTitles = ['Cargo', 'Orgao', 'Meses', 'Salario', 'Situacao']

aposentados_docentes_df = aposentados_docentes_df.reindex(columns=columnsTitles)
abono_docentes_df = abono_docentes_df.reindex(columns=columnsTitles)

# TODO Colocar no relatorio que excluiu as situacoes de nao interesse

abono_docentes_df = abono_docentes_df[abono_docentes_df['Situacao'] == 'ATIVO PERMANENTE']

aposentados_docentes_df = aposentados_docentes_df[aposentados_docentes_df['Situacao'] != 'OUTROS']
aposentados_docentes_df = aposentados_docentes_df[aposentados_docentes_df['Situacao'] != 'APOSENTADORIA POR INVALIDEZ']
                        
abono_docentes_df.loc[abono_docentes_df['Situacao'] == 'ATIVO PERMANENTE', ['Situacao']] = 1
aposentados_docentes_df.loc[aposentados_docentes_df['Situacao'] == 'VOLUNTARIA', ['Situacao']] = 2
aposentados_docentes_df.loc[aposentados_docentes_df['Situacao'] == 'COMPULSORIA', ['Situacao']] = 3


dataframe = pd.concat([abono_docentes_df, aposentados_docentes_df], ignore_index=True)

dataframe = dataframe.sample(frac=1).reset_index(drop=True)

dataframe.dropna(inplace=True)

dataframe["Situacao"] = dataframe["Situacao"].astype(int)

df_obj = dataframe.select_dtypes(['object'])
dataframe[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())

#exclusão das instancia cujo salario e' menor que o piso (2886.24)
dataframe = dataframe[dataframe['Salario'] >= 2886.24]
dataframe = dataframe[dataframe['Salario'] <= 39293]
#exclusão das instancia cujo meses e' inferior a 12
dataframe = dataframe[dataframe['Meses'] >= 12]

dataframe.to_csv(r'docentes_dataset.csv',index=False, header=True, sep=';')

# return dataframe