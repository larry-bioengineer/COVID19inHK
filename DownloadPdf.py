# Larry To
# Created on: 4/5/2020
# Go to the website of Department of Health and Protection and download their situational report 

# Import libraries
import requests 
from datetime import datetime 

# get response 
url = 'https://www.chp.gov.hk/files/pdf/local_situation_covid19_en.pdf'
r = requests.get(url)

# download file 
with open('data/pdf/local_situation_covid19_en.pdf', 'wb') as f:
	f.write(r.content)

now = datetime.now()
print(now.strftime("%Y-%m-%d") + ' COVID-19 Hong Kong situational data downloaded')
