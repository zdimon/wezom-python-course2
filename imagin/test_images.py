print('Testing images')
import requests
from bs4 import BeautifulSoup


rezult = requests.get('http://localhost:8080')
#print(rezult.text)
soup = BeautifulSoup(rezult.text, 'html.parser')
images = soup.findAll('img')
if len(images) < 6:
    raise Exception("Test is failed!!!")
else:
    print('OK')

# for h in h2s:
#     a = h.find('a')
#     print(a.text)
#     print(a['href'])


# file = open('filename','w')
# file.write('bla bla')
# file.close()