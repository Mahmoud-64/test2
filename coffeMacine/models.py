from django.db import models


class CoffeeMachine(models.Model):
    sku = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    water_line_compatible = models.BooleanField()


class CoffeePod(models.Model):
    sku = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    coffee_flavor = models.CharField(max_length=100)
    pack_size = models.SmallIntegerField()
