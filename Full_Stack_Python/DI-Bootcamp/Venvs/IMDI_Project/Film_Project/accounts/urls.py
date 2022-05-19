from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginViewForm.as_view(), name='login'),
]