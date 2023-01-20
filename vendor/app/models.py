from django.db import models

# Create your models here.

# Table settings
MAX_CHAR_LENGHT = 50
MAX_DIGIT = 9
MAX_DECIMAL_PLACE = 2
DEFAULT_DECIMAL_PLACE = 0

# Product settings
DEFAULT_QUANTITY = 1

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MAX_CHAR_LENGHT)
    price = models.DecimalField(max_digits=MAX_DIGIT, decimal_places=MAX_DECIMAL_PLACE, default=DEFAULT_DECIMAL_PLACE)

# intermediate table
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=DEFAULT_QUANTITY)

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    product =  models.ManyToManyField(Order)

class Machine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MAX_CHAR_LENGHT)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)








