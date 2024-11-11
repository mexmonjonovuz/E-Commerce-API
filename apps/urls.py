from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from apps.views import CategoryListCreateAPIView, ProductListCreateAPIView

urlpatterns = [
    path('categoryies/', CategoryListCreateAPIView.as_view(), name='category_list'),
    path('products/', ProductListCreateAPIView.as_view(), name='product_list'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
