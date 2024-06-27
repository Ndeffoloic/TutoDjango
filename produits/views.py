from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request, *args, **Kwargs) : 
    return HttpResponse("<h1> Bienvenue Loïc </h1>")