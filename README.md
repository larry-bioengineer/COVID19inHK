# COVID-19 Hong Kong Situation Study 

## Goal 
1. Gain a better understand on the situation of Hong Kong Cases 
2. Better visualization of Hong Kong Outbreak 

## Development Milestone 
![Development Milestone](/img/DevelopmentMilestone.png)

## Import Data from Department of Health and Protection 
### Data Source 
https://www.chp.gov.hk/files/pdf/local_situation_covid19_en.pdf

### Import tabular data 
I am using camelot (ref: https://camelot-py.readthedocs.io/en/master/). This library scans each page of the document and looks for table-like object. Then, user can use it to generate a pandas dataframe object. 

### Quick sheet using Pandas dataframe 
https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/

### Import Meta data 