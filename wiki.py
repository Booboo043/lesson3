import requests
from bs4 import BeautifulSoup
import os


u = "https://en.wikipedia.org/wiki/Deep_learning"
s = requests.get(u)
sp = BeautifulSoup(s.content, "html.parser")
r = sp.findAll('div')

for d in r:
    r1 = d.find('a')
    print(r1)
    div = sp.find('div', {'class': "mw-body"})
    print(div.text)
    n = d.get('href')
    print(n)



