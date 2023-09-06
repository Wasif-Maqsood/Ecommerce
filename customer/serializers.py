from rest_framework import serializers 
from customer.models import customer,shoping_order,deliveries,categories,payment

#Creat serializers Here.
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = customer
        fields='__all__'        


# Creating Shoping_Order_Serializer ....!!!!
class shoping_orderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= shoping_order
        fields="__all__"


#Creating categories_Serializer ....!!!!
class categoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= categories
        fields="__all__"


#Creating Deliveries Serializer .......!!!!!!
class deliveriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= deliveries
        fields="__all__"

#Creating Payment Serializer .......!!!!!!
class paymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= payment
        fields="__all__"