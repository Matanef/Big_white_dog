from django.shortcuts import render
import json

# Create your views here.

def family(request, x):
    family = {
            "id": ,
            "name": 
            }

def animal(request, x):
{
    return render(request, 'animal.html', {})
}



    context = {
        'family' : family,
        'animal': animal
    }
    return render(request, 'posts/homepage.html', context)