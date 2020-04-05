# Larry To 
# Created on: 4/5/2020
# Analyze COVID-19 data 

# Import libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import pickle 

file = open('data/processedData/20200405.pkl', 'rb')
data = pickle.load(file)
file.close()

print(data)
