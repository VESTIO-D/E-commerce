from django.db import models

# Create your models here.


class Category(models.Model):
    cname = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    c_img = models.ImageField(upload_to="Category Images",null=True, blank=True)


class productdb(models.Model):
    cname = models.CharField(max_length=100, null=True, blank=True)
    pname = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    c_img = models.ImageField(upload_to="Category Images",null=True, blank=True)