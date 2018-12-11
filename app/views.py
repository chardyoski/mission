import hashlib
import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Wheel, User


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
    token = request.session.get('token')

    data = {}

    if token:
        user = User.objects.get(token=token)
        data['name'] = user.name
        # data['img'] = user.img
        # data['rank'] = user.rank
    wheels=Wheel.objects.all()

    data={
        'wheels':wheels
    }
    return render(request, 'index.html',context=data)


def denglu(request):
    return render(request,'denglu.html')




def small(request):
    return render(request,'small.html')


def small1(request):
    return render(request,'small1.html')



import time
def generate_token():
    md5 = hashlib.md5()
    temp = str(time.time()) + str(random.random())
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()


# def generate_password(param):
#     md5 = hashlib.md5()
#     md5.update(param.encode('utf-8'))
#     return md5.hexdigest()



def zhuce(request):

    if request.method == 'GET':
        return render(request, 'zhuce.html')
    elif request.method == 'POST':
        user = User()
        user.password =request.POST.get('password')
        user.name = request.POST.get('name')
        user.phone = request.POST.get('phone')

        # 状态保持
        user.token = generate_token()
        user.save()
        request.session['token'] = user.token

        return redirect('mymission:index')
    # if request.method=='GET':
    #     return render(request,'zhuce.html')
    # if request.method=='POST':
    #     customer=request.POST.get('customer')
    #     print(customer)
    #     return HttpResponse('registering')




def gouwuche(request):
    token = request.session.get('token')
    data = {}
    if token:
        user = User.objects.get(token=token)
        data['name'] = user.name
        data['img'] = user.img

    return render(request,'gouwuche.html', context=data)


# def mine(request):
#     return None