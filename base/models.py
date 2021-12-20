from django.db import models
from django.contrib.auth.models import User

class Color(models.Model):
    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    options = (
        ('red', 'Red'),
        ('black', 'Black'),
        ('blue','Blue'),
    )

    name = models.CharField(max_length=100)
    model = models.CharField(null=True,blank=True,max_length=50)
    brand = models.CharField(null=True,blank=True,max_length=50)
    color = models.CharField(max_length=20,choices=options, default='black')
    unit_price = models.FloatField()
    current_stock = models.IntegerField(default=10,null=True,blank=True)
    image = models.FileField(blank=True,null=True,upload_to='products')
    details = models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    #quantity = models.IntegerField(blank=False)
    # date_created = models.DateTimeField(auto_now_add=True,blank=True)
    # date_modified = models.DateTimeField(blank=True)
    # completed = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        unique_together = ["user", "product", "quantity"]
    def __str__(self):
        if not self.user:
            return "Anonymous"
        obj_name = self.user.username
        return obj_name
