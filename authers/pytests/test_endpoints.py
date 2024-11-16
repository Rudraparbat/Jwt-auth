import requests
import pytest
from django.test import Client
endpoint = 'http://127.0.0.1:8000/api'

def test_register_user() :
    response = requests.post(endpoint+'/register/' ,json={
        "username" : "justin",    # you can add your username
        "password" : "Bieber@200", # you can add your password but must be in this pattern 
        "date_of_birth" : "21-12-2003" , # you cann add tour birth date
        "phone_numbers" : 9789343431 , # also phone number but not a string include as a phone number
        "email" : "jsutin@gmail.com" # also add your eamil in string format
    })
    if response.status_code == 400 :
        print("USER ALREADY EXIST")
        assert response.status_code == 400
    else :
        assert response.status_code == 201

def test_login_user(db) :
    client = Client()
    # test with default username and password which is already saved in database
    response = requests.post(endpoint+'/login/',json={
        "username" : "ruddy",
        "password" : 12345
    })
    response_body = response.json()
    assert response.status_code == 200
    session = client.session
    session['access_token'] = response_body['access_token']
    session['refresh_token'] = response_body['refresh']
    session.save()


def test_get_user() :
    response = requests.get(endpoint+'/profile')
    if response.status_code == 401 :
        print("USER IS UNAUTHORIZED PLS LOGIN FIRST")
        assert response.status_code == 401
    else :
        assert response.status_code == 200


def test_logout_user() :
    response = requests.get(endpoint+'/logout')
    assert response.status_code == 200