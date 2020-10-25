from django.db import models
from users.models import User


class Tops(models.Model):

    id = models.CharField(max_length=15, primary_key=True)
    brand = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    item_url = models.CharField(max_length=150)


class UserTops(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="userTops", null=True
    )
    vector = models.BinaryField(max_length=250, null=True)
    img = models.ImageField(upload_to="userTop")
    meta_top = models.ForeignKey(
        Tops, on_delete=models.SET_NULL, related_name="similarThings", null=True,
    )


class TopsImage(models.Model):

    id = models.CharField(max_length=15, primary_key=True)
    img_url = models.CharField(max_length=150)
    img = models.ImageField(upload_to="top")
    vector = models.BinaryField(max_length=250)
    top = models.ForeignKey(Tops, on_delete=models.CASCADE, related_name="images")
