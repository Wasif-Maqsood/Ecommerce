from django.shortcuts import render
from rest_framework import viewsets
from api.models import Product,Categories
from api.serializer import ProductSerializer,CategoriesSerializer

# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoriesViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

