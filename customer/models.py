from django.db import models

# Create your models here.

# Creating customer model ...!!!!

class customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=35)
    contect_add=models.CharField(max_length=50)
    address=models.CharField(max_length=70)

# Creating payment model ....!!!!
class shoping_order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(customer, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)

# Creating Deliveries model ....!!!!
class deliveries(models.Model):
    deliveries_id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)

    