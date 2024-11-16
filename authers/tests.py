from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
import requests
class UserTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.endpoint = 'http://127.0.0.1:8000/api'
        
        # Register a user for login and other tests

    def test_register_user(self):
        response = requests.post(self.endpoint + '/register/', json={
            "username": "justin",
            "password": "Bieber@200",
            "date_of_birth": "21-12-2003",
            "phone_numbers": 9789343431,
            "email": "justin@gmail.com"
        })
        if response.status_code == 400:
            print("USER ALREADY EXIST")
            self.assertEqual(response.status_code, 400)
        else:
            self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        response = requests.post(self.endpoint +'/login/', json={
            "username": "ruddy",
            "password": "12345"
        })
        response_body = response.json()
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        session['access_token'] = response_body['access_token']
        session['refresh_token'] = response_body['refresh']
        session.save()

    def test_get_user(self):
        response = requests.get(self.endpoint+'/profile')
        if response.status_code == 401:
            print("USER IS UNAUTHORIZED PLS LOGIN FIRST")
            self.assertEqual(response.status_code, 401)
        else:
            self.assertEqual(response.status_code, 200)

    def test_logout_user(self):
        response = requests.get(self.endpoint+'/logout/')
        self.assertEqual(response.status_code, 200)


