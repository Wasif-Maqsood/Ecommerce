from django.contrib import admin
from django.urls import path,include
from api.views import ProductViewset,CategoriesViewset
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'product', ProductViewset)
router.register(r'categories', CategoriesViewset)

urlpatterns = [
    path('', include(router.urls))
]
