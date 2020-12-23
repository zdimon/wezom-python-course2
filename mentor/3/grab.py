import requests
from bs4 import BeautifulSoup


rezult = requests.get('https://webmonstr.com')
#print(rezult.text)
soup = BeautifulSoup(rezult.text, 'html.parser')
h2s = soup.findAll('h2')
for h in h2s:
    a = h.find('a')
    print(a.text)
    print(a['href'])


file = open('filename','w')
file.write('bla bla')
file.close()