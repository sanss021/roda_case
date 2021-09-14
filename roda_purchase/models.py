import uuid
from django.db import models

# Create your models here.

class Payment(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=5, decimal_places=2)

    

    def __str__(self):
        return str(self.item) + ": $" + str(self.price)


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.CharField(max_length=100)
    products = models.ManyToManyField('Product')
    payment= models.ForeignKey(Payment,on_delete=models.DO_NOTHING, blank=True)
    


    def __str__(self):
        return self.client





