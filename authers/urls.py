from django.contrib import admin
from django.urls import path , include
from authers.views import *
from authers import views
urlpatterns = [
    path('',MainView.as_view(), name='main'),
    path('profile/',Getuser.as_view(),name='profile'),
    path('register/',CreateUserProfile.as_view(),name='register'),
    path('login/',Loginuser.as_view(),name='login'),
    path('logout/',Logoutuser.as_view() , name='logout'),
]
