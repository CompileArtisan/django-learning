from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)