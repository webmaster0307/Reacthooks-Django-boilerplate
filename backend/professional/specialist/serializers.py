from rest_framework import serializers
from specialist.models import Category, SubCategory, User

class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = ['id', 'name']

class SubCategorySerializer(serializers.ModelSerializer):
  category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)

  class Meta:
    model = SubCategory
    fields = ['id', 'name', 'category']

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['id', 'email', 'first_name', 'last_name', 'country', 'city', 'role', 'category', 'sub_category', 'password']
    extra_kwargs = {'password': {'write_only': True}}