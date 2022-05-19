from multiprocessing import context
from django.shortcuts import render
from .models import Animal, Family

# Create your views here.

def displayAllAnimals(request, id):
    myAnimal = Animal.objects.filter(animalid=id)
    context = {
        "myanimal": myAnimal,
        }
    return render(request, 'base.html', context)

def family(request, x):
    familyObject = Family.objects.filter(familyid = x)
    
    context = {
        "AnimalFamily": familyObject,
    }
    return render(request, 'base.html', context)