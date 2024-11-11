from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product


class ProductImageModelSerializer(ModelSerializer):
    pass


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'name', 'slug',


class OrderModelSerializer(ModelSerializer):
    pass


class Transaction(ModelSerializer):
    pass
