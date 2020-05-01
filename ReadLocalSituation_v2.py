# Larry To
# Created on: 4/3/2020
# Import a pdf file from Center for Health Protection (CHP) to extract information from Hong Kong COVID-19 situation report

# Import libraries 
import camelot 
import pandas as pd
from pandas import DataFrame
from datetime import datetime 
import os 
import matplotlib.pyplot as plt
import numpy as np 

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

# Remove empty row 
covidTable = covidTable.dropna(axis=0, how='any', thresh=7, subset=None, inplace=False)

# Cast each column into a correct data type 
covidTable = covidTable.astype({'CaseNo': 'int32'})
covidTable['ReportDate'] = pd.to_datetime(covidTable['ReportDate'])
# covidTable['OnsetDate'] = pd.to_datetime(covidTable['OnsetDate'])
covidTable = covidTable.astype({'Gender': 'category'})
covidTable = covidTable.astype({'Age': 'float'})
covidTable = covidTable.astype({'HospitalName': 'category'})
covidTable = covidTable.astype({'Status': 'category'})
covidTable = covidTable.astype({'Residency': 'category'})
covidTable = covidTable.astype({'Classification': 'category'})
covidTable = covidTable.astype({'ConfirmCase': 'category'})

# print(covidTable.info())

# Saving file 
now = datetime.now()
fileName = "data/processedData/" + now.strftime("%Y%m%d") + ".pkl"
covidTable.to_pickle(fileName)

