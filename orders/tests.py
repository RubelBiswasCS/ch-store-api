import email
from django.test import TestCase
from .models import Order,OrderItem
from users.models import CustomUser
from base.models import Product

class TestOrderModel(TestCase):
    def setUp(self):
        self.user1=CustomUser.objects.create(name="jeff",email='c@c.com')
        self.user2=CustomUser.objects.create(name="hopp",email='d@d.com')
        self.order1 = Order.objects.create(
            user=self.user1, full_name="cool jeff", email="c@c.com", address1="121 Park Street", address2="Borlon", city="Dhikov", phone="0191834747", postcode="1211", total_paid=129.00, order_key="reddfuie", payment_method="Strip", billing_status=True
            )
        self.order2 = Order.objects.create(
            user=self.user2, full_name="hot hopp", email='hhop@gmail.com', address1="101 Park Street", address2="Borlon", city="Dhikov", phone="018934747", postcode="1211", total_paid=129.00, order_key="reddfie33", payment_method="Stripe", billing_status=True
            )
        

    def test_order_model(self):
        order1 = self.order1
        order2 = self.order2
        self.assertIsInstance(order1,Order)
        self.assertIsInstance(order2,Order)
        self.assertEqual(str(order1),'cool jeff')
        self.assertEqual(str(order2),'hot hopp')
class TestOrderItemModel(TestCase):
    def setUp(self):
        self.user1=CustomUser.objects.create(name="jeff",email='c@c.com')
        self.order1 = Order.objects.create(
            user=self.user1, full_name="cool jeff", email="c@c.com", address1="121 Park Street", address2="Borlon", city="Dhikov", phone="0191834747", postcode="1211", total_paid=300.99, order_key="reddfuie", payment_method="Strip", billing_status=True
            )
        self.product1 = Product.objects.create(
            name="Chair 1", model="GX 3201", brand="Noopol", color="Red", unit_price= 300.99, current_stock=5, details="all the details about product 1"
            )
        self.order_item1 = OrderItem.objects.create(order=self.order1, product=self.product1, price=300.99, quantity=1)
        self.all_order_items = OrderItem.objects.all()
    
    def test_order_item_model(self):
        order_item1 = self.order_item1
        self.assertEqual(self.order1.total_paid,300.99)
        self.assertEqual(order_item1.price*order_item1.quantity,300.99)
        self.assertTrue(self.order1.total_paid == order_item1.price*order_item1.quantity)
        self.assertIsInstance(order_item1,OrderItem)
        self.assertIsNotNone(order_item1)
        self.assertIs(order_item1.order, self.order1)
        self.assertIn(order_item1,self.all_order_items)
        self.assertEqual(str(order_item1),str(1))


