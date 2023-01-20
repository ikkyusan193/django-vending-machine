from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app.serializers import ProductSerializer, OrderSerializer, StockSerializer, MachineSerializer
from app.models import Product, Order, Stock, Machine

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer 