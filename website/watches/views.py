from datetime import date

from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def regview(request):
    name = request.POST['name']
    age = request.POST['age']
    image = request.FILES['image']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    data = Register(name=name, age=age, image=image, address=address, phone=phone, email=email, username=username)
    data.save()
    data1 = Login(username=username, password=password, type=1)
    data1.save()
    return render(request, "last.html")


def index(request):
    return render(request, "index.html")


def register(request):
    return render(request, "register.html")


def last(request):
    return render(request, "last.html")


def userview(request):
    data3 = Register.objects.all()
    data4 = Login.objects.all()
    return render(request, "display.html", {"re": data3, "lo": data4})


def check(request):
    username = request.POST['username']
    password = request.POST['password']
    data2 = Login.objects.get(username=username, password=password)
    if data2.type == 1:
        request.session['username'] = data2.username
        data8 = Product.objects.all
        return render(request, "user.html", {"pr": data8})
    elif data2.type == 0:
        request.session['username'] = data2.username
        return render(request, "adm.html")


def login(request):
    return render(request, 'login.html')


def adm(request):
    return render(request, "adm.html")


def user(request):
    return render(request, "user.html")


def display(reqeust):
    return render(reqeust, "display.html")


def pro(request):
    pname = request.POST['pname']
    model = request.POST['model']
    image = request.FILES['image']
    price = request.POST['price']
    data5 = Product(pname=pname, model=model, image=image, price=price)
    data5.save()
    return render(request, "last.html")


def proview(request):
    data6 = Product.objects.all()
    return render(request, "ptable.html", {"pr": data6})


def pform(request):
    return render(request, "pform.html")


def ptable(request):
    return render(request, "ptable.html")


def delete(request, id):
    data7 = Product.objects.get(id=id)
    data7.delete()
    return HttpResponseRedirect(reverse("proview"))


def buy(request):
    username = request.session['username']
    pname = request.POST['pname']
    today = date.today()
    user = Register.objects.get(username=username)
    product = Product.objects.get(id=pname)
    data9 = Buy(username=user, pname=product, date=today)
    data9.save()
    value = Product.objects.all()
    return render(request, "user.html", {"pr": value})


def show(request):
    value1 = Buy.objects.all()
    return render(request, "btable.html", {"bu": value1})


def btable(request):
    return render(request, "btable.html")


def pf(request):
    us = request.session['username']
    reg = Register.objects.get(username=us)
    return render(request, "prtable.html", {"re": reg})


def prtable(request):
    return render(request, "prtable.html")


def order(request):
    va = request.session['username']
    ord = Register.objects.get(username=va)
    bud = Buy.objects.filter(username=ord)
    return render(request, "ortable.html", {"bu": bud})


def ortable(request):
    return render(request, "ortable.html")


def logout(request):
    return render(request, "logout.html")


def con(request):
    name = request.POST['name']
    phonenumber = request.POST['phonenumber']
    email = request.POST['email']
    message = request.POST['message']
    co = Contact(name=name, phonenumber=phonenumber, email=email, message=message)
    co.save()
    return render(request, "last.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def glasses(request):
    return render(request, "glasses.html")
