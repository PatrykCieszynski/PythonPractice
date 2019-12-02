import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
title = soup.find_all('h2')
string = ""
for x in title:
    print(x.text.strip())
    string += x.text + "\n"

with open('file_to_save.txt','w') as open_file:
    open_file.write(string)
