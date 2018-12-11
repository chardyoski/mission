from django.db import models

# Create your models here.
class Wheel(models.Model):

    img=models.CharField(max_length=100)
    img2=models.CharField(max_length=100)


class User(models.Model):
    name=models.CharField(max_length=40)
    password=models.CharField(max_length=256)
    phone=models.CharField(max_length=20)
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'wx_user'
