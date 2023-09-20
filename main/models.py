from django.db import models
import datetime

class Product(models.Model):
    name = models.CharField(max_length=256)
    developer = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    price = models.IntegerField(default="")
    amount = models.IntegerField(default="")
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)