from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from apps.models import Category
from apps.serializers import CategoryModelSerializer

@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    pass


class OrderListApiView(ListCreateAPIView):
    pass
