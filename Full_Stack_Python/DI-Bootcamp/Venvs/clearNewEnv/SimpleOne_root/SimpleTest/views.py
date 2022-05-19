from django.shortcuts import render
from .models import SimplePerson, Person

# Create your views here.

def index(request):
    persons = SimplePerson.objects.all()
    context = {
        "persons": persons,
        "matan" : [1,2,3],
    }
    return render(request, 'base.html', context)

def newPerson(request):
    newpersons = Person.objects.all()
    context = {
        "newViewpersons": newpersons,
        "numbersView": [1,2,3,4,5,6,7,8]
    }
    return render(request, 'base.html', context)



