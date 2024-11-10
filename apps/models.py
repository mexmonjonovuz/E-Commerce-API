from django.contrib.auth.models import AbstractUser
from django.db.models import Model, FloatField, CharField, ImageField, OneToOneField, CASCADE


class User(AbstractUser):
    pass


class Product(Model):
    name = CharField(max_length=255)
    price = FloatField(db_default=0)


class ProductImage(Model):
    image = ImageField(upload_to='%Y/%m/%d/')
    product = OneToOneField('apps.Product', CASCADE, related_name='product')


class Basket(Model):
    pass


class Payments(Model):
    pass
