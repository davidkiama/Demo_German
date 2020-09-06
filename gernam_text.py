#Importing the Libraries
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

#Extracting the Whole page
url = ('https://www.dw.com/de/themen/s-9077')
response = requests.get(url)
html = response.text
parsed_html = soup(html, "html.parser")
link_lists = parsed_html.findAll('div', {'class': 'linkList'})

#Extracting the Product details
master_list = []
for link_item in link_lists:
    data_dict = {}
    title = link_item.find('h2').text.strip()
    print(title)

    #Fill the dictionary
    data_dict['Title'] = title
    master_list.append(data_dict)

#Saving the data in C.S.V
df = pd.DataFrame(master_list)
df.to_csv('German.csv', index=False)
