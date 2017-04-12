from __future__ import unicode_literals

import datetime
from time import strftime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=320)
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=320)
    description = models.TextField()
    image = models.TextField()
    menucategory = models.ForeignKey(MenuCategory)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=320)
    address = models.TextField()
    phone = models.TextField()
    history = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=320, null=True, blank=True)
    #active = models.BooleanField(max_length=320, null=True, blank=True)
    order_date = models.DateTimeField('date published', null=True, blank=True)
    customer = models.ForeignKey(Customer)
    payment_type = models.CharField(max_length=100, null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class FoodCategory(models.Model):
    name = models.CharField(max_length=320)
    image = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=320)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    #date = pub_date.date()
    pub_date_string = models.CharField(max_length=320, null=True, blank=True)
    #pub_date_string = date.strftime('%Y-%m-%dT%H:%M')
    description = models.TextField()
    image = models.TextField(null=True, blank=True)
    menu = models.ForeignKey(Menu, null=True, blank=True)
    order = models.ForeignKey(Order, null=True, blank=True)
    foodcategory = models.ForeignKey(FoodCategory, null=True, blank=True)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
     

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'foods'

    def dump(self):
        return {"foodlist":{'name':self.name,
                        'pub_date':self.pub_date,          
                        'description':self.description,
                        'image':self.image,
                        'menu':self.menu.pk,
                        'order':self.order.pk,
                        'foodcategory':self.foodcategory.pk}}

    @property
    def convertdate(self):
        pub_date_string = self.pub_date.date().strftime('%Y-%m-%d')
        return pub_date_string


class Cart(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)

    def add_to_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexisting_order = BookOrder.objects.get(book=book, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except BookOrder.DoesNotExist:
            new_order = BookOrder.objects.create(
                book=book,
                cart=self,
                quantity=1
            )
            new_order.save()

    def remove_from_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexisting_order = BookOrder.objects.get(book=book, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except BookOrder.DoesNotExist:
            pass


class FoodOrder(models.Model):
    food = models.ForeignKey(Food)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField()
