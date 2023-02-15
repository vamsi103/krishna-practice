from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    ProductBrandName = models.CharField(max_length=30)
    ProductBrandModel = models.CharField(max_length=30)
    ProductBrandPrice = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Product',args={self.pk})





# Create your models here.
