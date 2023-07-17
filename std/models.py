from django.db import models


class Students(models.Model):
    roll=models.IntegerField(null=True)
    name=models.CharField(max_length=100) 
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    phone=models.IntegerField(null=True)
