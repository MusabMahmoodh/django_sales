from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from django.shortcuts import reverse

from .utils import generate_code
# Create your models here.
class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True) #optional
    created = models.DateTimeField(blank=True) #optional
    
    
    #optional
    # def myFun(**kwargs): 
    # for key, value in kwargs.items():
    #     print ("%s == %s" %(key, value))
    
    # def myFun(arg1, *argv):
    # print ("First argument :", arg1)
    # for arg in argv:
    #     print("Next argument through *argv :", arg)
    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)
        
    def __str__(self):
        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}"

class Sale(models.Model):
    transaction_id = models.CharField(max_length=12,blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"Sales for the amount of ${self.total_price}"
    
    def save(self,*args,**kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args,**kwargs)
    
    def get_positions(self):
        return self.positions.all()

    def get_absolute_url(self):
        return reverse('sales:detail', kwargs={'pk':self.pk}) #appname:name
class CSV(models.Model):
    file_name = models.FileField(upload_to='csv')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.file_name)