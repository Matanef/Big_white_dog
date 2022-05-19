from django.urls import path #path function
from . import views # . is shorthand for the current directory


# one urlpattern per line
urlpatterns = [
    path('index', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('email', views.email, name='email'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('all/', views.PostIndex.as_view(), name='posts'),
    path(r'new_person/(?P<first_name>)', views.Person_id.as_view(), name='person'),
]

# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route

