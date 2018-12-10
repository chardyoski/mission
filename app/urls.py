from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^denglu/$',views.denglu,name='login'),
    url(r'^gouwuche/$',views.gouwuche,name='cart'),
    url(r'^small/$',views.small,name='small'),
    url(r'^small1/$',views.small1,name='small1'),
    url(r'^zhuce/$',views.zhuce,name='register')
]