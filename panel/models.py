from django.db import models

# Create your models here.
class Members(models.Model):
    Name=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Pwd=models.CharField(max_length=150)
    Mobile=models.CharField(max_length=10)
    
class Orders(models.Model):
    product_name= models.CharField(max_length=50)
    product_price=models.TextField(max_length=50)
    customer=models.TextField(max_length=50)
    address=models.TextField(max_length=150,null=True)
    description=models.TextField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Meta:
    db_table="orders"

class Products(models.Model):
    product_name= models.CharField(max_length=50)
    product_price=models.TextField(max_length=50)
    quantity=models.TextField(max_length=50)
    image=models.ImageField(upload_to='images',null=True,blank=True)
    description=models.TextField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Meta:
    db_table="products"