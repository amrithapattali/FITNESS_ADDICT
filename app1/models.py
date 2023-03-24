from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=150, null=True)
    amount = models.CharField(max_length=15, null=True)
    duration = models.CharField(max_length=15, null=True)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=2083, blank=True)

    def _str_(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=2083, blank=True)

    def _str_(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    Emailid = models.CharField(max_length=50)
    Age = models.CharField(max_length=40)
    Gender = models.CharField(max_length=10, default="")
    plan = models.CharField(max_length=50)
    Joindate = models.DateField(max_length=40)
    Expiredate = models.DateField(max_length=40)
    Initialamount = models.CharField(max_length=10)

    def _str_(self):
        return self.name

class MyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    bio = models.CharField(max_length=200)
    Plans = models.ManyToManyField(Plan)
    address = models.TextField(null=True, blank=True)


class Enquiry(models.Model):
    name = models.CharField(max_length=150, null=True)
    mobile = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=10, null=True)


    def __str__(self):
        return self.name
