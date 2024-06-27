from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request, *args, **Kwargs) : 
    return render(request, 'index.html', {})