from django.test import TestCase
from .models import CustomUser, Address, CustomUserManager

class TestCustomUserModel(TestCase):
    def setUp(self):
        self.user1=CustomUser.objects.create(name="jeff",email='c@c.com',phone="01387283434", is_active=True, is_staff=True)
        self.user2=CustomUser.objects.create(name="hopp",email='d@d.com',phone="01387283434", is_active=True, is_staff=False)
        self.superuser1 = CustomUser.objects.create(name="hopp",email='a@a.com',phone="01387283434", is_active=True, is_staff=True,is_superuser=True)

        self.user3= CustomUser.objects.create_user(email="test@a.com", name="tester",password='1234')
        self.user5= CustomUser.objects.create_superuser(email="supertester@a.com", name="super_tester",password='1234')
        

    def test_customuser_model(self):
        user1= self.user1
        self.assertEqual(str(user1),'jeff')

    def test_customuser_superuser(self):
        superuser1 = self.superuser1
        self.assertTrue(superuser1.is_superuser)

    def test_customuser_manager(self):
        user3 = self.user3
        user5 = self.user5
        self.assertEqual(str(user3),'tester')

        self.assertEqual(str(user5),'super_tester')
        self.assertTrue(user5.is_superuser)

        with self.assertRaisesMessage(ValueError,expected_message='Superuser must be assigned to is_staff=True'):
            self.user6 = CustomUser.objects.create_superuser(email="invalidsupertester@a.com", name="invalid_super_tester",password='1234',is_staff=False)
        with self.assertRaisesMessage(ValueError,expected_message='Superuser must be assigned to is_superuser=True'):
            self.user6 = CustomUser.objects.create_superuser(email="falsesupertester@a.com", name="false_super_tester",password='1234',is_superuser=False)
        with self.assertRaises(ValueError) as e:
            #print("Error: ", e)
            self.user4= CustomUser.objects.create_user(email="",name="tester",password='1234')

            #print("Test exception: ",exception)
            #self.assertEqual(the_exception 3)


class TestAddressModel(TestCase):
    def setUp(self):
        self.user1=CustomUser.objects.create(name="jeff",email='c@c.com',phone="01387283434", is_active=True, is_staff=True)
        self.address1 = Address.objects.create(customer=self.user1, full_name="c tirk", phone='01387283434', postcode='1299', address_line="12 RA", address_line2="Wisnconsie", city="New Barlin",default=True)

    def test_address_model(self):
        address1 = self.address1
        self.assertEqual(str(address1),"c tirk"+"'s Address")

# class TestCustomUserManager(TestCase):
#     def setUp(self):
#         customuser_manager = CustomUserManager()
#         user3= customuser_manager.create_user(email="test@a.com", name="tester",password='1234')
#     def test_customuser_manager(self):
#         user3= self.user3
#         self.assertEqual(str(user3),'test er')




