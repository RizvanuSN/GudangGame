from django.db import models
from django.contrib.auth.models import User
import datetime

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    developer = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    price = models.IntegerField(default="")
    amount = models.IntegerField(default="")
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    img_url = models.TextField()