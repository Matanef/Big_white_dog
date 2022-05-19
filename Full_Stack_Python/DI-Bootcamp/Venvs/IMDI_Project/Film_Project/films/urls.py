from django.urls import path
from .views import *

urlpatterns = [
    path('homepage', homepage, name = 'homepage'),
    path('add_film', AddFilmView.as_view(), name = 'add_film'),
    path('add_director', AddDirectorView.as_view(), name = 'add_director'),

]