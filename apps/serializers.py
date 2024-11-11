from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product, Transaction, Order, ProductImage


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TransactionModelSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
