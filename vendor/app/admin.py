from django.contrib import admin

# Register your models here.
from app.models import Product, Stock, Machine

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Machine)

