from django.db import models


# Create your models here.
class MedicineModel(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    expire_date = models.DateField()
    catagory = models.CharField(max_length=100)
    quantity = models.CharField(max_length=10)


class SalesModel(models.Model):
    customer = models.CharField(max_length=200)
    medicine = models.CharField(max_length=200)
    amount = models.CharField(max_length=10)
    price = models.CharField(max_length=20)
    date = models.DateField()


class CustomerModel(models.Model):
    fullName = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    phoneNumber = models.CharField(max_length=14)
    registerDate = models.DateField()


class LonsModel(models.Model):
    customerName = models.CharField(max_length=300)
    amount = models.CharField(max_length=10)
    date = models.DateField()
