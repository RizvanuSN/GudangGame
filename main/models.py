from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=256)
    developer = models.CharField(max_length=255)
    price = models.IntegerField()
    genre = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
