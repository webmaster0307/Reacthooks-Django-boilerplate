from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, max_length=100, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

ADMIN = 1
USER = 2

class User(AbstractBaseUser):
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (USER, 'user')
    )

    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=USER, help_text='User type')
    
    # user status
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # timestampes
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []