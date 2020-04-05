# COVID-19 Hong Kong Situation Study 

## Goal 
1. Gain a better understand on the situation of Hong Kong Cases 
2. Better visualization of Hong Kong Outbreak 

## Development Milestone 
![Development Milestone](/img/DevelopmentMilestone.png)

## Import Data from Department of Health and Protection 
### Data Source 
Center for Health Protection (https://www.chp.gov.hk/files/pdf/local_situation_covid19_en.pdf)
To download the data, I am using requests, which will get the file from the center and save it to folder. 

### Import tabular data 
I am using camelot (ref: https://camelot-py.readthedocs.io/en/master/). This library scans each page of the document and looks for table-like object. Then, user can use it to generate a pandas dataframe object. 

### Quick cheat sheet using Pandas dataframe 
https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/

## Performing analytics 

## Display data and analytics on a web app 
### Displaying analytics on a web app 
I am using flask (ref: https://flask.palletsprojects.com/en/1.1.x/). Flask is python library for developing minimal application 

### Deploying the website 
I am using Heroku (ref: https://dashboard.heroku.com/apps) Heroku allows users to deploy their flask app on their server for free. 

