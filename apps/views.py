from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from apps.models import Category, Product, Order, Transaction
from apps.serializers import CategoryModelSerializer, ProductModelSerializer, OrderModelSerializer


@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


@extend_schema(tags=['product'])
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


@extend_schema(tags=['order'])
class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


@extend_schema(tags=['transaction'])
class TransactionCreateAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = OrderModelSerializer














