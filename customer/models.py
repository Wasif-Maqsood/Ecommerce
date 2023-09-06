from django.db import models

# Create your models here.

# Creating customer model ...!!!!

class customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=35)
    contect_add=models.CharField(max_length=50)
    address=models.CharField(max_length=70)

# Creating Shoping_order model ....!!!!
class shoping_order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(customer, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)

# Creating categories model ....!!!!
class categories(models.Model):
    categories_id=models.AutoField(primary_key=True)
    categories_name=models.CharField(max_length=40)
    categories_type=models.CharField(max_length=25)

# Creating Deliveries model ....!!!!
class deliveries(models.Model):
    deliveries_id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)    

 # Creating Payment model ....!!!!
class payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    categories_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)     