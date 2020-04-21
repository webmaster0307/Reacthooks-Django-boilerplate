from django.shortcuts import render
from rest_framework import viewsets
from specialist.serializers import CategorySerializer, SubCategorySerializer, UserSerializer
from specialist.models import Category, SubCategory, User

class CategoryViewSet(viewsets.ModelViewSet):
  queryset =  Category.objects.all()
  serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
  queryset =  SubCategory.objects.all()
  serializer_class = SubCategorySerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
# Create your views here.
