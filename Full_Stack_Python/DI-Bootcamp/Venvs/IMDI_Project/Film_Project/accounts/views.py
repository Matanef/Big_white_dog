from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView   




class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = SignUpForm
    success_message = " Your profile was created successfully"

class LoginViewForm(LoginView):
    template_name =  'registration/login.html'
    success_url =  reverse_lazy('index')
    success_message = '<p class="success_login">You were successfully logged in </p>'