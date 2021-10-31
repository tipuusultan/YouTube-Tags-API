
from django.contrib import admin
from django.urls import path
from home.views import home, get_data

urlpatterns = [
    path('', home),
    path('get/', get_data, name='GetData'),
]
