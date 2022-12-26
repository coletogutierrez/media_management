from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase
from django.test import TestCase
import requests








class ArtistsSimpleTests(TestCase):

    databases = '__all__'

    def testConnect(self):

        url = 'http://127.0.0.1:8000/api/v1/artists/'
        headers = {'Authorization': 'Token 0f600cb1b626c5a4b41c3a4e30fc5b0f09e7085f'}
        r = requests.get(url, headers=headers)
        
        assert r.status_code == 200     






