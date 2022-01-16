from http import client
import re
from urllib import response
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from users.models import CustomUser
from base.models import Product

class CartListTest(APITestCase):
    def setUp(self):
        self.url = reverse("api:cartlist")
        self.user1 = CustomUser.objects.create_superuser(email="supertester@a.com", name="super_tester",password='1234')
        self.user2 = CustomUser.objects.create_superuser(name='Dhony Jepp',email='jepp@gmail.com',password='1234567')
     
        self.client = APIClient()
        login_response = self.client.login(email=self.user1.email,password='1234')
        print("Login response:",login_response)
        self.product1 = Product.objects.create(name="Chair 1", model="GX 3201", brand="Noopol", color="Red", unit_price= 300.99, current_stock=5, details="all the details about  product 1")
        self.product2 = Product.objects.create(name="Chair 2", model="GX 3202", brand="Noopol", color="Red", unit_price= 150.99, current_stock=5, details="all the details about  product 2")
    
    def test_cartlist_get(self):
        url = self.url
        client = self.client
       
        self.assertEqual(CustomUser.objects.all().count(),2)
        response = client.get(url)
        print("Response: ",response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_cartlist_post(self):
        # fields = ['user','product','quantity']
        data={
            'user':1,
            'product':1,
            'quantity':3,
        }
        response1 = self.client.post(self.url,data,format='json')
        print(response1.data)
        response2 = self.client.post(self.url,{'user':1,'product':"invalid product"},format='json')
        self.assertEqual(response1.data['unit_price'],self.product1.unit_price)
        self.assertEqual(response1.data,{'id': 1, 'name': 'Chair 1', 'quantity': 3, 'unit_price': 300.99})
        self.assertEqual(response1.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        
class CartDetailTest(APITestCase):
    def setUp(self):
        
        self.user1 = CustomUser.objects.create_superuser(email="supertester@a.com", name="super_tester",password='1234')
        self.client = APIClient()
        self.client.login(email=self.user1.email,password='1234')
        self.product1 = Product.objects.create(name="Chair 1", model="GX 3201", brand="Noopol", color="Red", unit_price= 300.99, current_stock=5, details="all the details about  product 1")
        self.client.post(reverse("api:cartlist"),{'user':1,'product':1,'quantity':3},format='json')
        self.url1 = reverse("api:cartdetail",kwargs={'pk':1})
        self.url2 = reverse("api:cartdetail",kwargs={'pk':20})
    def test_cartdetail_patch(self):
        response1 = self.client.patch(self.url1,{'quantity':2},format='json')
        response2 = self.client.patch(self.url1,{'quantity':'two'},format='json')
        self.assertEqual(response1.status_code,status.HTTP_206_PARTIAL_CONTENT)
        self.assertEqual(response2.status_code,status.HTTP_400_BAD_REQUEST)

    def test_cartdetail_delete(self):
        response3 = self.client.delete(self.url1)
        response4 = self.client.delete(self.url2)
        # print(response4)
        self.assertEqual(response3.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response4.status_code,status.HTTP_404_NOT_FOUND)

# class OrderListTests(APITestCase):
#     def setUp(self):
#         pass

#     def test_order_create(self):
#         url = reverse('api:placeorder')
#         self.user1 = CustomUser.objects.create_superuser(name='Dhony Jepp',email='jepp@gmail.com',password='1234567')
#         data = {
#             'full_name':"User 1",
#             'email':"testuser1@gmail.com",
#             'address1':"12 LA Row",
#             'address2':"Pinsolo",
#             'city':"Hesico",
#             'phone':"0139373847",
#             'postcode':"1202",
#             'total_paid': 150.99,
#             'order_key':"Rsk93278",
#             'payment_method':"Strip",
#             'billing_status':1,
#         }

#         self.client.login(email=self.user1.email,password='1234567')
#         response = self.client.post(url, data, format='json')
#         print(response)
#         self.assertEqual(response.status_code,status.HTTP_201_CREATED)
