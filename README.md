# COVID-19 Hong Kong Situation Study 

## Goal 
1. Gain a better understand on the situation of Hong Kong Cases 
2. Better visualization of Hong Kong Outbreak 

## Development Milestone 
![Development Milestone](/img/DevelopmentMilestone.png)

## Import Data from Department of Health and Protection 
### Data Source 
Center for Health Protection 
- Local Situational Data(https://www.chp.gov.hk/files/pdf/local_situation_covid19_en.pdf)
- Mandatory quarantine citizens(https://www.chp.gov.hk/files/pdf/599c_en.pdf)
To download the data, I am using requests, which will get the file from the center and save it to folder. 

### Import tabular data 
I am using camelot (ref: https://camelot-py.readthedocs.io/en/master/). This library scans each page of the document and looks for table-like object. Then, user can use it to generate a pandas dataframe object. 

This picture represents how camelot processes a table within a PDF. It recognizes all the element and converts the data into a pandas dataframe object. 

![PDF Sample](/img/PDFSC.png)

### Quick cheat sheet using Pandas dataframe 
https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/

## Performing analytics 

### Analyzing location of self-quarantined personal 
(https://towardsdatascience.com/geocode-with-python-161ec1e62b89)

### Challenge facing right now 
- Camelot cannot recognize all the data on the PDF 
	- possible solution: 
		- download new data and see if camelot can read the new data better, it fills in the missing data in existing dataset 
- geopy cannot recognize a few street address in Hong Kong 
	- possible solution: 
		- text processing to a simpler address format 
		- explain the location is an estimate with possible radius 


## Display data and analytics on a web app 
### Displaying analytics on a web app 
I am using flask (ref: https://flask.palletsprojects.com/en/1.1.x/). Flask is python library for developing minimal application 

### Deploying the website 
I am using Heroku (ref: https://dashboard.heroku.com/apps) Heroku allows users to deploy their flask app on their server for free. 

