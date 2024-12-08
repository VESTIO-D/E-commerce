from django.db import models

# Create your models here.

class servicedb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)


class regdb(models.Model):
    uname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    p_img = models.ImageField(upload_to="profile Images",null=True, blank=True)



class cartdb(models.Model):
    uname = models.CharField(max_length=50, null=True, blank=True)
    pname = models.CharField(max_length=50, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)


class billingDB(models.Model):
    uname = models.CharField(max_length=50 , null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)