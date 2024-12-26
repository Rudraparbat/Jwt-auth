from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
class Userserializer(serializers.ModelSerializer) :
    class Meta :
        model = Authuser
        fields = ['username' , 'password' , 'email' , 'phone_numbers' , 'date_of_birth' , 'last_login_ip']
    

    
class Myrefreshtoken(RefreshToken) :
    @classmethod
    def for_user(self , user) :
        token = super().for_user(user)
        token['username'] = user.username
        token['email'] = user.email
        token['date_of_birth'] = user.date_of_birth
        token['phone_numbers'] = user.phone_numbers
        token['last_login_ip'] = user.last_login_ip
        return token
