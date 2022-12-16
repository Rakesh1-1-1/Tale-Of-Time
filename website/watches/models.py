from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.FileField()
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=60)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=8)


class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.IntegerField()
    type = models.IntegerField()


class Product(models.Model):
    pname = models.CharField(max_length=40)
    model = models.CharField(max_length=50)
    image = models.FileField()
    price = models.IntegerField()


class Buy(models.Model):
    username = models.ForeignKey(Register, on_delete=models.CASCADE)
    pname = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.CharField(max_length=35)


class Contact(models.Model):
    name = models.CharField(max_length=25)
    phonenumber = models.IntegerField()
    email = models.CharField(max_length=60)
    message = models.CharField(max_length=100)
