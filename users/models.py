from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(max_length=10, blank=True)
    birthday = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=20, default="no_name")
    nickname = models.CharField(max_length=20, default="no_name")
    age = models.IntegerField(default=0)

    tops = models.ManyToManyField("tops.Tops", related_name="tops")
    pants = models.ManyToManyField("pants.Pants", related_name="pants")
    shoes = models.ManyToManyField("shoes.Shoes", related_name="shoes")
