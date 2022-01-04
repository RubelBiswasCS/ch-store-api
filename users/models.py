from django.db import models
from django.contrib.auth.models import (
                            AbstractBaseUser,
                            BaseUserManager,
                            PermissionsMixin
                            )

class CustomUserManager(BaseUserManager):
    def create_superuser(self,email,name,password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True')
        return self.create_user(email,name,password,**other_fields)
    
    def create_user(self,email, name, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20,blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name

class Address(models.Model):
    customer = models.ForeignKey(CustomUser, verbose_name="Customer", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    address_line = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.full_name+"'s Address"