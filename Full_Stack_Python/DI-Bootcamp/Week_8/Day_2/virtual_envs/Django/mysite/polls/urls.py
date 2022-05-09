from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('index', views.index, name='index'),
    # path('About_website', views.About, name = 'About')
    path('about/<str:name>/<str:last_name>/', views.About, name='about'),
    path('profile', views.profile, name='profile'),
]

# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route