import hashlib
import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Wheel, User, Books, Cart


def index(request):

    #retrive data from json
    # with open('/home/ban/Desktop/mymission/static/json/lunbotu1.json', 'r', encoding='utf8') as qf:
    #     contents = qf.read()
    #     contents = eval(contents)
    # for dice in contents:
    #     lunbo = Books()
    #     # lunbo.productid = dice['productid']
    #     lunbo.productimg = dice['productimg']
    #     lunbo.productname = dice['productname']
    #     lunbo.price = dice['price']
    #     lunbo.marketprice = dice['marketprice']
    #     lunbo.save()
    token = request.session.get('token')
    wheels = Wheel.objects.all()
    books=Books.objects.all()
    book1=Books.objects.first()
    book2=Books.objects.filter(id=2)[0]
    data = {'wheels':wheels,
            'books':books,
            'book1':book1,
            'book2':book2,}

    if token:
        user = User.objects.get(token=token)
        data['name'] = user.name

    # wheels=Wheel.objects.all()
    #
    # data={
    #     'wheels':wheels
    # }
    return render(request, 'index.html',context=data)


def denglu(request):
    if request.method == 'GET':
        return render(request, 'denglu.html')

    elif request.method == 'POST':

        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=name)
            if user.password == password:
                user.token = generate_token()
                user.save()
                request.session['token'] = user.token
                return redirect('mymission:index')
            else:
                return render(request, 'denglu.html', context={'p_error': 'username/password error'})
        except:
                return render(request, 'denglu.html', context={'u_error': 'username/password error'})




def small(request):
    token = request.session.get('token')
    # carts = []
    book1 = Books.objects.first()
    print(book1.id)
    # productid = request.GET.get('productid')
    # print(productid)



    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).first()
        name = user.name

    data = {'book1': book1,
            'carts': carts,
            'name':name,
            }
    return render(request,'small.html',context=data)


def small1(request):

    token = request.session.get('token')
    book2 = Books.objects.filter(id=2)[0]
    print(book2.id)
    # carts = []

    # productid = request.GET.get('productid')
    # print(productid)



    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).filter(id=2)
        name = user.name

    data = {'book2': book2,
            'carts': carts,
            'name':name,
            }

    return render(request,'small1.html',context=data)



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
    # token = request.session.get('token')
    #
    # if token:
    #     data = {}
    #     user = User.objects.get(token=token)
    #     data['name'] = user.name
    #     # data['img'] = user.img
    #
    # return render(request,'gouwuche.html', context=data)

    token = request.session.get('token')
    carts = []
    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(number=0)

        data = {
            'carts': carts
        }

        return render(request, 'gouwuche.html', context=data)
    else:
        return redirect('mymission:login')


# def mine(request):
#     return None
def checkname(request):
    name=request.GET.get('name')
    print(name)
    # return JsonResponse({'msg': '用户名可以使用'})
    users=User.objects.filter(name=name)
    if users.exists():
        return JsonResponse({'msg':'用户名不可以使用','status':0})
    else:
        return JsonResponse({'msg':'用户名可以使用','status':1})


def logout(request):
    request.session.flush()
    return redirect('mymission:index')


def addcart(request):
    booksid=request.GET.get('booksid')
    token=request.session.get('token')
    print(booksid)
    data={}
    if token:
        user=User.objects.get(token=token)
        books = Books.objects.get(pk=booksid)
        carts=Cart.objects.filter(user=user).filter(books=books)
        if carts.exists():

            cart=carts.first()
            cart.number=cart.number+1
            cart.save()

        else:
            cart=Cart()
            cart.user=user
            cart.books=books
            cart.number=1
            cart.save()
        return JsonResponse({'msg':'{},添加购物车成功'.format(books.productname),'number':cart.number,'status':1})

    else:
        data['msg']="please login!"
        data['status']=-1
        return JsonResponse(data)


def subcart(request):
    token = request.session.get('token')
    booksid = request.GET.get('booksid')

    user = User.objects.get(token=token)
    books = Books.objects.get(pk=booksid)

    # 找到对应的购物车 商品信息
    cart = Cart.objects.filter(user=user).filter(books=books).first()
    cart.number = cart.number - 1
    cart.save()

    data = {
        'msg': '购物车删减成功',
        'status': 1,
        'number': cart.number
    }

    return JsonResponse(data)