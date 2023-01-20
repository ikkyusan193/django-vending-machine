from django.contrib import admin

# Register your models here.
from app.models import Product, Order, Stock, Machine

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Stock)
admin.site.register(Machine)

