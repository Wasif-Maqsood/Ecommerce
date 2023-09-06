from django.shortcuts import render
from rest_framework import viewsets
from customer.models import customer,shoping_order,deliveries
from customer.serializers import CustomerSerializer,shoping_orderSerializer,deliveriesSerializer


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=customer.objects.all()
    serializer_class=CustomerSerializer

# shoping view ....!!!!!

class shoping_orderViewSet(viewsets.ModelViewSet):
    queryset=shoping_order.objects.all()
    serializer_class=shoping_orderSerializer

# Deliveries view.....!!!!!

class deliveriesViewSet(viewsets.ModelViewSet):
    queryset=deliveries.objects.all()
    serializer_class=deliveriesSerializer

