from .views import USERREGISTER
from django.contrib import admin
from django.urls import path
app_name = 'accunts'
urlpatterns = [
path('register' ,USERREGISTER.as_view(), name='register' ),
]


