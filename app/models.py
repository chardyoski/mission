from django.db import models

# Create your models here.
class Wheel(models.Model):

    img=models.CharField(max_length=100)
    img2=models.CharField(max_length=100)


class User(models.Model):
    name=models.CharField(max_length=40,unique=True)
    password=models.CharField(max_length=256)
    phone=models.CharField(max_length=20)
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'wx_user'


class Books(models.Model):

    # 商品ID
    productid = models.CharField(max_length=10, default='0')
    # 商品图片
    productimg = models.CharField(max_length=100)
    # 商品名字
    productname = models.CharField(max_length=100)
    # 价格
    price = models.DecimalField(max_digits=6, decimal_places=1)
    # 本店价格
    marketprice = models.DecimalField(max_digits=6, decimal_places=1)
    # img=models.CharField(max_length=100)
    # span
    #
    # smallImg=models.CharField(max_length=100)
    # bigImg=models.CharField(max_length=100)
class Cart(models.Model):
    # 购物车　模型类
    # 用户
    user = models.ForeignKey(User)
    # 商品
    books = models.ForeignKey(Books)
    # 商品个数
    number = models.IntegerField()
    # 是否选中
    isselect = models.BooleanField(default=True)

    # 选择颜色
    # 选择内存
    # 选择版本

    class Meta:
        db_table = 'app_cart'