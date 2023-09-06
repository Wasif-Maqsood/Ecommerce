from django.db import models

# Create your models here.
# Create Product models here.

class Categories(models.Model):
    Category_ID = models.AutoField(primary_key = True)
    Category_Name = models.CharField(max_length=50)
    Category_Type = models.CharField(max_length=100)


class Product(models.Model):
    Product_ID = models.IntegerField(primary_key = True)
    Category_ID = models.ForeignKey(Categories, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=30)


class Seller(models.Model):
    Seller_ID = models.IntegerField(primary_key=True)
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)

   
def __str__(self):
    return self.Product_name

    

    
