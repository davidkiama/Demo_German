#Importing the Libraries
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

#Extracting the Whole page
url = ('https://www.dw.com/de/themen/s-9077')
response = requests.get(url)
html = response.text
parsed_html = soup(html, "html.parser")
titles = parsed_html.findAll('div', {'class': 'news'})

#Extracting all the Headings
master_list = []
for title in titles:
    data_dict = {}
    heading = title.find('h2').text.strip()

    #Fill the dictionary
    data_dict['LIST OF HEADINGS'] = heading
    master_list.append(data_dict)

#Saving the data in C.S.V
df = pd.DataFrame(master_list)
df.to_csv('Headings.csv', index=False)
