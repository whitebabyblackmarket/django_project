from django.test import TestCase, Client
from django.urls import reverse
from replicate_integration import views

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.index_url = reverse('index')

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'replicate_integration/index.html')

