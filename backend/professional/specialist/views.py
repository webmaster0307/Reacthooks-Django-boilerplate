from django.shortcuts import render
from rest_framework import viewsets
from specialist.serializers import CategorySerializer, SubCategorySerializer
from specialist.models import Category, SubCategory

class CategoryViewSet(viewsets.ModelViewSet):
  queryset =  Category.objects.all()
  serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
  queryset =  SubCategory.objects.all()
  serializer_class = SubCategorySerializer

# Create your views here.
