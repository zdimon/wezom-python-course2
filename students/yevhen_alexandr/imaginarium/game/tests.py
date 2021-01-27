from django.test import TestCase
from django.test import Client

class homePageTestCase(TestCase):
    def test_home_page_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


    #def test_home_page_images(self):

