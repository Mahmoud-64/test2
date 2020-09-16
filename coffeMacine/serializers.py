from rest_framework import serializers
from . import models


class CoffeeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoffeeMachine
        fields = ('sku', 'product_type', 'water_line_compatible')


class CoffeePodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoffeePod
        fields = ('sku', 'product_type', 'coffee_flavor', 'pack_size')
