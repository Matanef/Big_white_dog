from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
# path('displayAllAnimals/', views.displayAllAnimals, name='displayAllAnimals'),
path('<int:id>', views.displayAllAnimals, name = "blah"),
path('<int:x>', views.family, name='family'),
]