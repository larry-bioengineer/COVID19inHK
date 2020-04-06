import pickle 

path = "data/processedData/"
filename = "mainDataSet.pkl"
print(path+filename)
covidTable = pickle.load(open(path + filename, "rb"))

print(covidTable.info())