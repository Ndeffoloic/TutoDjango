from django.shortcuts import HttpResponse, render
from django.views import View

from .models import Produit


# Create your views here.
def index(request, *args, **Kwargs) : 
    liste_produits = Produit.objects.all()
    context  ={
        'liste_produits' : liste_produits,
        'nom' : "Produits de la boutique de Nembutsu",
    }
    return render(request, 'index.html', context)

class CreateProduct(View):
    def get(self, request, *args, **Kwargs):
        return render( request, 'produits/create_product.html')
    
    def post(self, request, *args, **Kwargs):
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')
        image = request.FILES.get('image')
        
        produit = Produit(nom = nom, description = description, prix= prix, image = image) 
        produit.save()
        # ou j'aurais pu faire  : produit = Produit.objects.create(nom = nom, etc...)
        if produit : 
            return HttpResponse('Produit enregistré avec succès')
        else : 
            return HttpResponse("Erreur lors de l'enregistrement du produit")
        
    