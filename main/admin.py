from django.contrib import admin
from .models import Branch,CountryOfOrigin,Category,Product,Sale
admin.site.register(Branch)
admin.site.register(CountryOfOrigin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
