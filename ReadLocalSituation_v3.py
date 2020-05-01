# Larry To
# Created on: 4/6/2020
# Import a pdf file from Center for Health Protection (CHP) to extract information from Hong Kong COVID-19 situation report
# Update: changing how data is saved and append new data to existing data storage 

# Import libraries 
import camelot 
import pandas as pd
from pandas import DataFrame
from datetime import datetime 
import os 
import matplotlib.pyplot as plt
import numpy as np 
import pickle 

# Read Data 
tables = camelot.read_pdf('data/pdf/local_situation_covid19_en.pdf', 
	pages='1-end')

# camelot.plot(tables[0], kind='grid')
# plt.show()

# Append table from different pages 


covidTable = []
for table in tables:
	if table.parsing_report['accuracy'] < 80:
		break

	covidTable.append(table.df)
covidTable = pd.concat(covidTable)

covidTable.columns = ['CaseNo', 'ReportDate', 'OnsetDate'
	, 'Gender', 'Age', 'HospitalName', 'Status', 'Residency'
	, 'Classification', 'ConfirmCase']



# Remove row with header information 
covidTable = DataFrame.drop_duplicates(covidTable)
covidTable = covidTable.iloc[1:,] # remove first header row()

# Remove any row with nan
nan_value = float("NaN")
covidTable = covidTable.replace("", nan_value, inplace=False)
covidTable = covidTable.dropna(axis=0, how='any', thresh=10, subset=None, inplace=False)

# Cast each column into a correct data type 
# covidTable = covidTable.astype({'CaseNo': 'float'})
# covidTable['ReportDate'] = pd.to_datetime(covidTable['ReportDate'])
# covidTable['OnsetDate'] = pd.to_datetime(covidTable['OnsetDate'])
# covidTable = covidTable.astype({'Gender': 'category'})
# covidTable = covidTable.astype({'Age': 'float'})

# Sort Data by case number 
covidTable = covidTable.sort_values(by=['CaseNo'])



# Saving file 
path = "data/processedData/"
filename = "mainDataSet.pkl"

try:
	oldTable = pickle.load(open(path + filename, "rb"))

	# Append data
	covidTable = oldTable.append(covidTable)
	covidTable = DataFrame.drop_duplicates(covidTable)
	covidTable = covidTable.dropna(axis=0, how='any', thresh=10, subset=None, inplace=False)
	covidTable = covidTable.sort_values(by=['CaseNo'])
	covidTable.to_pickle(path + filename)
	
except:
	covidTable.to_pickle(path + filename)

print(covidTable.info())
