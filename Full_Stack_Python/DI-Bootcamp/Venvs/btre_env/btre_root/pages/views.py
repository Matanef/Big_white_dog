from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, '../templates/home.html')

def about(request):
    return render(request, 'C:/DIgitfolder/Full_Stack_Python/DI-Bootcamp/Venvs/btre_env/btre_root/templates/about.html')