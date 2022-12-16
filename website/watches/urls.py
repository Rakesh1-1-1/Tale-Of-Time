"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('register', views.register, name="register"),
    path('last', views.last, name="last"),
    path('regview', views.regview, name="regview"),
    path('userview', views.userview, name="userview"),
    path('check', views.check, name="check"),
    path('login', views.login, name="login"),
    path('adm', views.adm, name="adm"),
    path('user', views.user, name="user"),
    path('display', views.display, name="display"),
    path('pro', views.pro, name="pro"),
    path('proview', views.proview, name="proview"),
    path('pform', views.pform, name="pform"),
    path('ptable', views.ptable, name="ptable"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('buy', views.buy, name="buy"),
    path('show', views.show, name="show"),
    path('btable', views.btable, name="btable"),
    path('pf', views.pf, name="pf"),
    path('prtable', views.prtable, name="prtable"),
    path('order', views.order, name="order"),
    path('ortable', views.ortable, name="ortable"),
    path('logout', views.logout, name="logout"),
    path('contact', views.contact, name="contact"),
    path('con', views.con, name="con"),
    path('about', views.about, name="about"),
    path('glasses', views.glasses, name="glasses"),
]
