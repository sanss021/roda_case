from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from roda_purchase.api import viewsets as purchaseviewsets

'''Determinar automaticamente a URL conf através de routers'''

route = routers.DefaultRouter()
route.register(r'purchases', purchaseviewsets.PurchaseViewSet, basename="Purchases")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
