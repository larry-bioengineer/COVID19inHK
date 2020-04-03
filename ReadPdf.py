# Larry To
# Created on: 4/3/2020
# Import a pdf file from Center for Health Protection (CHP) to extract information from Hong Kong COVID-19 situation report

# Import libraries 
from tika import parser

# # Import Files 
# Parse data from file 
raw = parser.from_file('local_situation_covid19_en.pdf')
print(raw['content'])

from tabula import read_pdf

df = read_pdf("local_situation_covid19_en.pdf", pages='2', multiple_tables='False')
print(df)