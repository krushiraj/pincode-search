from django.contrib import admin
from django.urls import path, include
from searchapp.views import *

urlpatterns = [
    path('', index, name='index')
]