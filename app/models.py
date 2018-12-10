from django.db import models

# Create your models here.
class Wheel(models.Model):

    img=models.CharField(max_length=100)
    img2=models.CharField(max_length=100)