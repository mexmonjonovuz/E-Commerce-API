from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from apps.views import CategoryListCreateAPIView, ProductListCreateAPIView,OrderListCreateAPIView

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category_list'),
    path('products/', ProductListCreateAPIView.as_view(), name='product_list'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order_list'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
