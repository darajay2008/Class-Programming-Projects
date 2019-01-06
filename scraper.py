import urllib2
from bs4 import BeautifulSoup
import pandas as pd

quote_page='https://wallethub.com/edu/states-with-the-best-schools/5335/'
page=urllib2.urlopen(quote_page)
soup=BeautifulSoup(page, 'html.parser')

#column_headers=[th.getText() for th in soup.findAll('tr', limit=1)[0].findAll('th')]
column_headers=['Overall Rank','State','Total Score','SchoolSystemQuality','SchoolSystemSafety']

data_rows= soup.findAll('tr')[1:]
type(data_rows)
school_data=[[td.getText() for td in data_rows[i].findAll('td')]for i in range(len(data_rows))]

school_data_2=[]
for i in range (len(data_rows)):
    school_row=[]
    for td in data_rows[i].findAll('td'):
        school_row.append(td.getText())
    school_data_2.append(school_row)
    
school_data == school_data_2

df=pd.DataFrame(school_data, columns=column_headers)
df.head()
df.head(20)


print(df.columns)
df=df.convert_objects(convert_numeric=True)
df.dtypes
df.to_csv("School_rankings_in_2016.csv")
import sys
import bs4
print('Python version:',sys.version_info)
print('urllib2 version:',urllib2.__version__)
print('BeautifulSoup version:', bs4.__version__)
print('Pandas version:',pd.__version__)