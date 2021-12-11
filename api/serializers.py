from rest_framework import serializers
from base.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','model','brand','color','unit_price','current_stock','details']