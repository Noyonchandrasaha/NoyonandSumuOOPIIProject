from django.db import models

# Create your models here.
class Sellpost(models.Model):
    category = models.CharField(max_length=100,null=True)
    pirce = models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    description = models.TextField(max_length=800, null=True)
    name = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)