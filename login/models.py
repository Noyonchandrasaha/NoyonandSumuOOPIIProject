from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=100,null=False)
    passw = models.CharField(max_length=100,null=False)
    re_pass= models.CharField(max_length=100,null=False)
