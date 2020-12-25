import requests
from bs4 import BeautifulSoup
from datetime import datetime

base_url = 'https://webmonstr.com'
res = requests.get(base_url)
html = res.text

soup = BeautifulSoup(html, 'html.parser')

courses = soup.select('.course-item')

for course in courses:
    h2 = course.find('h2', class_='course-title')
    if h2:
        a = h2.find('a')
        title = a.text
        href = a['href']
        filename = href.split('/').pop()

        description = h2.find_parent('div').find_next_sibling('div').text

        with open(filename + '.md', 'w') as file:
            now = datetime.now()

            print('Title:', title, file=file)
            print('Date:', now.strftime("%Y-%m-%d, %H:%M"), file=file)
            print('Category: Cources', file=file)
            print(file=file)
            print(description.strip(), file=file)
            print(f'[{title}]({base_url}{href})', file=file)
