from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "How to setup Django",
            'author': "Maria"
        },
        {
            'title' : "How to cake an amazing pie",
            'author' : "Chef Mark"
        }
    ]
    
    choice = 'Maria'
    
    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'posts/homepage.html', context)


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def About(request, name, last_name):
    context = {'name': name, 'last_name': last_name}
    # return HttpResponse("so this is the About page")
    return render(request, 'about.html', context)


def profile(request):

    context = {'name': 'Matan', 'age': '38', 'gender': 'M', 'favorite_books': ['1984', 'when Harry met Sally', 'LOTR']}
    return render(request, 'profile/profile_user.html', context)