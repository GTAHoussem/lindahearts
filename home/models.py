from django.db import models


# Create your models here.
class Service(models.Model):
    
    picture = models.ImageField(null=True, upload_to="gallery")
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=254)
    duration = models.IntegerField(null=True)
    price = models.CharField(max_length=5, default="19.00")
    category = models.CharField(max_length=64, default="Default")

    def __str__(self):
        return self.name + " - " + self.description + " - " + self.price
