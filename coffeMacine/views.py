from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet


class CoffeeMachineFilterSet(FilterSet):
    class Meta:
        model = models.CoffeeMachine
        fields = ['product_type', 'water_line_compatible']


class CoffeeMachineViewset(viewsets.ModelViewSet):
    queryset = models.CoffeeMachine.objects.all()
    serializer_class = serializers.CoffeeMachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CoffeeMachineFilterSet


class CoffeePodFilterSet(FilterSet):
    class Meta:
        model = models.CoffeePod
        fields = ['product_type', 'coffee_flavor', 'pack_size']


class CoffeePodViewset(viewsets.ModelViewSet):
    queryset = models.CoffeePod.objects.all()
    serializer_class = serializers.CoffeePodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CoffeePodFilterSet
