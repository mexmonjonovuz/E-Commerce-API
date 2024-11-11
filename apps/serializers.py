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
        extends = 'slug',


class OrderModelSerializer(ModelSerializer):
    pass


class Transaction(ModelSerializer):
    pass

