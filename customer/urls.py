from django.contrib import admin
from django.urls import path,include
from customer.views import CustomerViewSet,shoping_orderViewSet,deliveriesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"customers",CustomerViewSet)
router.register(r"shoping_orders",shoping_orderViewSet)
router.register(r"deliveries",deliveriesViewSet)

urlpatterns = [
    path('',include(router.urls))

]