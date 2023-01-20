from rest_framework import serializers

from app.models import Product, Order, Stock, Machine

MAX_DEPTH = 5

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]
        ordering = ['-name']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["product", "quantity"]     
        depth = MAX_DEPTH   

class StockSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many = True, read_only=True)
    class Meta:
        model = Stock
        fields = ["id", "products", "order"]
        depth = MAX_DEPTH
        
class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ["id", "name", "stock"]    
        depth = MAX_DEPTH