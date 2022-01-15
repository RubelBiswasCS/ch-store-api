from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from base.models import Product

class Order(models.Model):
    # fields = [user, full_name, email, address1, address2, city, phone, postcode, created, updated, total_paid, order_key, payment_method, billing_status]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='order_user')
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,blank=True)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    postcode = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5,decimal_places=2)
    order_key = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=200,blank=True)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.full_name

class OrderItem(models.Model):
    #fields = [order, product, price, quantity]

    order = models.ForeignKey(Order,related_name='items',on_delete=CASCADE)
    product = models.ForeignKey(Product,related_name="order_items",on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return str(self.id)

