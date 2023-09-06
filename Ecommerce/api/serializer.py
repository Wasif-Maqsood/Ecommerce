
from rest_framework import serializers
from api.models import Product,Categories,Seller



class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields ="__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ="__all__"

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields ="__all__"