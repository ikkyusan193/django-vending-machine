from rest_framework import serializers

from app.models import Product, Order, Stock, Machine

MAX_DEPTH = 5

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        ordering = ['name']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        depth = MAX_DEPTH
        
class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'   
        depth = MAX_DEPTH