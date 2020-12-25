import requests
from bs4 import BeautifulSoup

resourseUrl = 'https://webmonstr.com'
result = requests.get(resourseUrl)

soup = BeautifulSoup(result.text, 'html.parser')
h2s = soup.findAll('h2', {"class": "course-title"})

for h in h2s:
    generateFile(h)


def generateFile(h):
    filename = h.find('a')['href'].replace('/', '-')
    file = open("content/%s" % (filename), 'w')
    file.write(content(h))
    file.close()


def content(h):
    link = h.find('a')
    linkText = link.text
    linkHref = "%s/%s" % (resourceUrl, link['href'])
