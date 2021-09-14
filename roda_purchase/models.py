import uuid
from django.db import models

# Create your models here.


class Product(models.Model):
    item= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=5, decimal_places=2)

    
    def __str__(self):
        return str(self.item) + ": $" + str(self.price)


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.CharField(max_length=100)
    products = models.ManyToManyField('Product')
    
    
    def __str__(self):
        return self.client





