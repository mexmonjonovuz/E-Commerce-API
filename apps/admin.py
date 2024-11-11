from django.contrib.admin import ModelAdmin, register

from apps.models import Product, Category


@register(Product)
class ProductAdminModel(ModelAdmin):
    pass


@register(Category)
class ProductAdminModel(ModelAdmin):
    pass
