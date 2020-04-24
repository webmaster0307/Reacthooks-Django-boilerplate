from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from specialist.serializers import CategorySerializer, SubCategorySerializer, UserSerializer, SignupSerializer, EnquirerySerializer
from specialist.models import Category, SubCategory, User, Enquirery
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
  queryset =  Category.objects.all()
  serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
  queryset =  SubCategory.objects.all()
  serializer_class = SubCategorySerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class SignupView(generics.CreateAPIView):
  serializer_class = SignupSerializer
  permission_classes = [AllowAny,]


class EnquireryViewSet(viewsets.ModelViewSet):
  pagination_class = None
  queryset = Enquirery.objects.all()
  serializer_class = EnquirerySerializer

  def get_serializer_class(self):
    if self.action == 'create':
      return EnquireryCreateSerializer
    else:
      return EnquirerySerializer
