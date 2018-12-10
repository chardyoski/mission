from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wheel


def index(request):

    #retrive data from json
    # with open('/home/ban/Desktop/mymission/static/json/lunbotu1.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #     lunbo = Wheel()
    #     lunbo.img = dice['img']
    #     lunbo.img2 = dice['img2']
    #     lunbo.save()

    wheels=Wheel.objects.all()

    data={
        'wheels':wheels
    }
    return render(request, 'index.html',context=data)


def denglu(request):
    return render(request,'denglu.html')


def gouwuche(request):
    return render(request,'gouwuche.html')


def small(request):
    return render(request,'small.html')


def small1(request):
    return render(request,'small1.html')


def zhuce(request):
    return render(request,'zhuce.html')