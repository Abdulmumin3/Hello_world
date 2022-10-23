from tkinter import N
from django import urls
from django.urls import path
from .views import homePageView

urlpatterns = [
    path("", homePageView, name='home'),
]
