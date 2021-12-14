from django.contrib import admin
from .models import Product,Color,Cart
# Register your models here.

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Cart)