from django.shortcuts import render
import json


# Create your views here.



def family(request, x):
    family = {
        'id': 7,
        'name': 3
    }
    context = {
        'family' : family,   
    }
    return render(request, 'family.html', context)
    


with open('animal.json') as animals:
    data = json.load(animals)
    print(data)

def animal(request, x):
    animal = {
            "id": x,
            "name": "",
            "legs": ,
            "weight": ,
            "height":,
            "speed": ,
            "family": 
    }
    context = {
        'animal': animal
    }
    return render(request, 'animal.html', context)



        'family' : family,
        
}
return render(request, 'posts/homepage.html', context)