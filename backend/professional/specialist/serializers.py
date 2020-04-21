from rest_framework import serializers
from specialist.models import Category, SubCategory

class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = ['id', 'name']

class SubCategorySerializer(serializers.ModelSerializer):
  category = CategorySerializer(many=False)

  class Meta:
    model = SubCategory
    fields = ['id', 'name', 'category']