from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

'Creating Merchant model'

class Merchant(models.Model):
    address = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    pincode = models.IntegerField()
    



'Creating CLient model'

class Client(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    merchant = models.ForeignKey(Merchant,on_delete=models.CASCADE,default = None)
    
    def __str__(self):
        return self.first_name
    
    
