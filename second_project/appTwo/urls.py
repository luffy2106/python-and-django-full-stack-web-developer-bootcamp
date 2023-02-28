
from appTwo import views
from django.urls import path
from django.contrib import admin

urlpatterns = [path('', views.users, name='users'),
               ]





