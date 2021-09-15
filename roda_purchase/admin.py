from django.contrib import admin

''' configurar nossa inteface de administração'''

from .models import Purchase

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'price','id')
    list_display_links = ('item', 'price','id')


admin.site.register(Purchase)
admin.site.register(Product, ProductAdmin)


