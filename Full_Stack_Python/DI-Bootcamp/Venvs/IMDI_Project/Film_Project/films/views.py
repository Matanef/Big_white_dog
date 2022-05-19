from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import *
# Create your views here.

def homepage(request):
    
    films = Film.objects.all()
    directors = Director.objects.all()
    context = {'page_title':'homepage', 'films': films, 'directors': directors}

    return render(request, 'homepage.html', context)

class AddFilmView(generic.CreateView):
    template_name = 'films/add_film.html'
    model = Film
    fields = '__all__'

    def get_success_url(self):
        return reverse('homepage')    

class AddDirectorView(generic.CreateView):
    template_name = 'films/add_director.html'
    model = Director
    fields = '__all__'

    def get_success_url(self):
        return reverse('homepage')

"""Add generic views for adding Category, Country"""