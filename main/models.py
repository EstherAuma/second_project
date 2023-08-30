from django.db import models
from django.contrib.auth.models import AbstractUser


from django.urls import reverse_lazy
from django.views.generic import CreateView




# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self): 
        return f'{self.name} of {self.location}'
    
class CountryOfOrigin(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self): 
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self): 
        return self.name
    



    

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    country_of_origin =  models.ForeignKey(CountryOfOrigin, on_delete=models.CASCADE, null=False, blank=False)
    received_quantity = models.PositiveIntegerField(null=False, blank=False)
    unit_price = models.PositiveIntegerField( null=False, blank=False)
    date_received = models.DateTimeField(auto_now=True)
    part_number = models.CharField(max_length=50, null=False, blank=False, unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self): 
        return f'Name: {self.name},  Category: {self.category}, Unit price: {self.unit_price}'
    

class Sale(models.Model):
    buyer_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.PositiveIntegerField(null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    total_amount = models.PositiveIntegerField(null=False, blank=False)
    amount_paid = models.PositiveIntegerField(null=False, blank=False)
    sale_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now_add=True)
    
    def balance(self):
        change = self.total_amount() - self.amount_paid
        
        return int(change)
    
    def __str__(self):
        return  f'Product: {self.product.name}, Quantity: {self.quantity}'
    

class User(AbstractUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.IntegerField(default=0)
    nationality = models.CharField(max_length=10)

    def __str__(self): 
        return self.first_name
        





    

 


