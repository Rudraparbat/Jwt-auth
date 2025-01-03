from django.shortcuts import render , redirect ,HttpResponse 
from django.http import JsonResponse
from .models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.generic import TemplateView
import jwt
# This class for creating the user profile and save into db
class CreateUserProfile(APIView) :
    def post(self, request):
        data = request.data.copy()
        data['last_login_ip'] = request.ip_address
        data['password'] = make_password(data['password'])
        serializer = Userserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# This class for getting user profile (after login else it will show a not found message)
class Getuser(APIView) :
    def get(self, request) :
        try :
            access_token = request.COOKIES.get('access_token')
        except :
            access_token = None
        if access_token == None :
            return Response({
                "message" : "please login first to get the user profile",      
            },status = status.HTTP_401_UNAUTHORIZED)
        else : 
            user = jwt.decode(jwt = access_token,options={"verify_signature": False},algorithms=['HS256'])
            return Response({
                "user_id" : user['user_id'],
                "username" : user['username'],
                "phone_number" : user['phone_numbers'],
                "date_of_birth" : user['date_of_birth'],
                "email" : user['email'],
                "login_ip" : user['last_login_ip'],
            } , status= status.HTTP_200_OK)
            
# This class for user to login and create jwt authentication tokens and save it to the server session securely 
class Loginuser(APIView) :
    def post(self , request) :
        user = request.data
        username = user.get('username')
        password = user.get('password')
        authuser = Authuser.objects.filter(username = username).first()
        if authuser and authuser.check_password(password):
            authuser.last_login_ip = request.ip_address
            authuser.save() 
            refresh = Myrefreshtoken.for_user(authuser)
            access_token  = str(refresh.access_token)
            refresh_token = str(refresh)
            response = Response(
                {
                "message": f"Hello {user['username']}, login successful!",
                "access_token": access_token,
                "refresh_token": refresh_token,
                }
            )
            response.set_cookie(
                'access_token', value=access_token, httponly=True, secure=True, samesite='Strict'
            )
            response.set_cookie(
                'refresh_token', value=refresh_token, httponly=True, secure=True, samesite='Strict'
            )
            return response
        return Response({"message"  : f"{user['username']} doesnt exist"} , status=status.HTTP_404_NOT_FOUND)
#  This is for logging out a logged in user which flush the tokens from the session
class Logoutuser(APIView):
    def get(self, request):
        response = JsonResponse({"message": "Logged out successfully"})
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        request.session.flush()
        return response
class MainView(TemplateView):
    template_name = 'index.html'
class HomePageView(TemplateView):
    template_name = 'home.html'