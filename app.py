# Larry To
# Created on: 4/5/2020
# An web application to display analytics 

# Import libraries
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
import pickle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


# Load data 
path = "data/processedData/"
filename = "mainDataSet.pkl"
print(path+filename)
covidTable = pickle.load(open(path + filename, "rb"))

@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('index.html',  tables=[covidTable.to_html(classes='data')], titles=covidTable.columns.values)


# Running app 
if __name__ == "__main__":
	app.run(debug=True)