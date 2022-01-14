from django.test import TestCase
from .models import Color,Product,Cart,CartManager
from users.models import CustomUser


class TestColorModel(TestCase):
    def setUp(self):
        self.color1 = Color.objects.create(name="Red")

    def test_color_model_entry(self):
        color1 = self.color1
        self.assertTrue(isinstance(color1,Color))
        self.assertEqual(str(color1),"Red")

class TestProductModel(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name="Chair 1", model="GX 3201", brand="Noopol", color="Red", unit_price= 300.99, current_stock=5, details="all the details about  product 1")
        self.product2 = Product.objects.create(name="Chair 2", model="GX 3202", brand="Noopol", color="Red", unit_price= 150.99, current_stock=5, details="all the details about  product 2")

    def test_product_model_entry(self):
        product1 = self.product1
        product2 = self.product2

        self.assertTrue(isinstance(product1,Product))
        self.assertTrue(isinstance(product2,Product))
        self.assertEqual(str(product1),'Chair 1')
        self.assertEqual(str(product2),'Chair 2')

class TestCartModel(TestCase):
    def setUp(self):
        self.user1=CustomUser.objects.create(name="admin")
        #check 
        self.product1 = Product.objects.create(name="Chair 1", model="GX 3201", brand="Noopol", color="Red", unit_price= 300.99, current_stock=5, details="all the details about  product 1")
        self.product2 = Product.objects.create(name="Chair 2", model="GX 3202", brand="Noopol", color="Red", unit_price= 150.99, current_stock=5, details="all the details about  product 2")
        self.cart1 = Cart.objects.create(user=self.user1,product=self.product1,quantity=2,completed=False)
        self.cart2 = Cart.objects.create(user=self.user1,product=self.product2,quantity=2,completed=True)
        self.cart3 = Cart.objects.create(product=self.product2,quantity=2,completed=True)
        
    def test_custom_cart_manager(self):
        carts = Cart.items.all()
        self.assertEqual(carts.count(),1)

    def test_cart_model_entry(self):
        cart1=self.cart1
        cart2=self.cart2
        cart3=self.cart3
        self.assertTrue(isinstance(cart1,Cart))
        self.assertEqual(cart1.quantity,2)
        self.assertNotEqual(cart2.completed,False)
        self.assertEqual(str(cart3),'Anonymous')
        self.assertEqual(str(cart1),'admin')

        






    