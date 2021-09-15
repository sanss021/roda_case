from rest_framework import viewsets
from roda_purchase.api import serializers
from roda_purchase import models

'''Visualização baseada em classes'''

class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PurchaseSerializer
    queryset = models.Purchase.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    

    