# Larry To
# Created on: 4/10/2020
# Import a pdf file from Center for Health Protection (CHP) to extraction 
# information about which building contains self-quarantine citizens 

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
tables = camelot.read_pdf('data/pdf/self_quarantine.pdf', pages='1')

camelot.plot(tables[0], kind='joint')
plt.show()

sqTable = []
for table in tables:
	sqTable.append(table.df)

sqTable = pd.concat(sqTable)

sqTable.columns = ['CaseNo', 'District', 'Address', 'EndDate']

sqTable.District.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
sqTable.Address.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)

# for address in sqTable['Address']:
# 	print(address)

# Saving File 
path = "data/processedData/"
filename = "self_quarantine.pkl"

try:
	oldTable = pickle.load(open(path + filename, "rb"))

	# Append data
	sqTable = oldTable.append(sqTable)
	sqTable = DataFrame.drop_duplicates(sqTable)
	# sqTable = sqTable.dropna(axis=0, how='any', thresh=10, subset=None, inplace=False)
	sqTable = sqTable.sort_values(by=['CaseNo'])
	sqTable.to_pickle(path + filename)
	
except:
	sqTable.to_pickle(path + filename)

print(sqTable.head())
print(sqTable.info())