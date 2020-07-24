from django.db import models


class Shoes(models.Model):

    _id = models.CharField(max_length=15)
    brand = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    item_url = models.CharField(max_length=150)
