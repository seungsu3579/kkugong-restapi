from django.db import models
from users.models import User


class Cody(models.Model):

    id = models.CharField(max_length=15, primary_key=True)
    img = models.ImageField(upload_to="cody/cody")
    jjim = models.BooleanField(default=False)
    cody_top_img = models.ImageField(upload_to="cody/top")
    cody_pants_img = models.ImageField(upload_to="cody/pants")
    cody_shoes_img = models.ImageField(upload_to="cody/shoes")
    form = models.IntegerField(default=0)
