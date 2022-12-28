from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=False,blank=False)
    description = models.TextField(max_length=250,null=True,blank=True)
    price = models.FloatField(default=0)
    
    def __str__(self):
        return self.name

