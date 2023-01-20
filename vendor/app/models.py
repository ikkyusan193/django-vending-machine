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

class Machine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MAX_CHAR_LENGHT)
    location = models.CharField(max_length=MAX_CHAR_LENGHT)
    is_active = models.BooleanField(default=True)

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    class Meta:
        constraints = [
          models.UniqueConstraint(fields=['machine', 'product'], name='machine_product')
        ]








