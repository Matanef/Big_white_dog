from django.shortcuts import render, get_list_or_404
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental/', views.all_rental),    
    ]