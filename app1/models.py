from django.db import models
from django.urls import reverse

class Product(models.Model):
    name=models.CharField(max_length=100)
    discriptoion=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
      ordering=['name']

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):    
        return reverse("product_details",kwargs={"pk":self.pk})    