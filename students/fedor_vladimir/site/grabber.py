import requests
from bs4 import BeautifulSoup


class Grabber:
    def __init__(self, resource_url='https://webmonstr.com'):
        self.resourceUrl = resource_url
        self.result = requests.get(resource_url)
        self.soup = BeautifulSoup(self.result.text, 'html.parser')

    def find_element(self, el, params=None):
        if params is None:
            return self.soup.find(el)
        return self.soup.find(el, params)

    def find_elements(self, el, params=None):
        if params is None:
            return self.soup.findAll(el)
        return self.soup.findAll(el, params)

    @staticmethod
    def generate_file(el):
        filename = el.find('a')['href'].replace('/', '-')
        filename = filename.lstrip('-')
        filename = "content/%s" % filename
        title = el.get_text()
        description = el.parent.find_next('div').get_text()
        file_content = "%s\n%s" % (title, description)
        file = open(filename, 'w')
        file.write(file_content.strip())
        file.close()


grabber = Grabber()
h2s = grabber.find_elements('h2')


for h2 in h2s:
    grabber.generate_file(h2)
