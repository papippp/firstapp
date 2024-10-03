from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=100)
class order(models.Model):
    item_name = models.CharField(max_length=100)
    item_category = models.CharField(max_length=100)
    item_price = models.IntegerField()
    customer = models.OneToOneField(customer,on_delete=models.PROTECT, related_name='order')

class Application(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    