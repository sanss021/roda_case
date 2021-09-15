from rest_framework import serializers
from roda_purchase import models

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


'''Aqui é onde transformamos dados em um formato que pode ser armazenado ou transmitido'''