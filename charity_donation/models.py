# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

INSTITUTION = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna")
)

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=INSTITUTION, default=1)
    categories = models.ManyToManyField(Category)

    @property
    def categories_id(self):
        array = []
        category_list = ''
        for n in self.categories.all():
            category_list = category_list + ',' + str(n.id)
        return category_list

    def __str__(self):
        return self.name

class Donation(models.Model):
    quantity = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE,)
    adress = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)