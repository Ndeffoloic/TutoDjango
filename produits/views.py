from django.shortcuts import HttpResponse, render
from django.views import View

from .form import ProduitForm
from .models import Produit


# Create your views here.
def index(request, *args, **Kwargs) : 
    liste_produits = Produit.objects.all()
    context  ={
        'liste_produits' : liste_produits,
        'nom' : "Produits de la boutique de Nembutsu",
    }
    return render(request, 'index.html', context)

# class CreateProduct(View):
#     def get(self, request, *args, **Kwargs):
#         return render( request, 'produits/create_product.html')
    
#     def post(self, request, *args, **Kwargs):
#         try:
#             nom = request.POST.get('nom')
#             description = request.POST.get('description')
#             prix = request.POST.get('prix')
#             image = request.FILES.get('image')
            
#             produit = Produit(nom = nom, description = description, prix= prix, image = image) 
#             produit.save()
#             # ou j'aurais pu faire  : produit = Produit.objects.create(nom = nom, etc...)
#             if produit : 
#                 return HttpResponse('Produit enregistré avec succès')
#         except Exception as e : 
#             return HttpResponse("Erreur lors de l'enregistrement du produit")
        

class CreateProduct(View):
    def get(self, request, *args, **Kwargs):
        form  = ProduitForm()
        return render( request, 'produits/create_product.html', {'form' : form}) # j'envoie mon formulaire dans le contexte
    
    def post(self, request, *args, **Kwargs):
        
        form = ProduitForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponse('Produit enregistré avec succès')
        else : 
            return render(request, 'produits/create_product.html', {'form': form})
        
    
    