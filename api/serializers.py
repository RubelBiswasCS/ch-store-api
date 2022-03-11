from rest_framework import serializers
from base.models import Product,Cart
from orders.models import Order,OrderItem
from users.models import Address

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','model','brand','color','unit_price','current_stock','details']

class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        fields = ['user','product','quantity']

class CartCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        fields = ['user','product','quantity']
        depth=1

class AddressSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Address
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_items = serializers.SerializerMethodField(method_name='get_order_items')
    class Meta:
        model = Order
        fields = ['user','full_name','email','address1','address2','city','phone','postcode','total_paid','order_key','payment_method','billing_status','order_items']

    def get_order_items(self,obj):
        return OrderItemSerializer(obj.get_order_items,many=True).data

class OrderItemSerializer(serializers.ModelSerializer):
    # order = OrderSerializer()
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'price', 'quantity']
       

