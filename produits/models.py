from django.db import models


# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description  = models.TextField()
    prix  = models.FloatField()
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return self.nom