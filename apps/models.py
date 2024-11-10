from django.contrib.auth.models import AbstractUser
from django.db.models import Model


class User(AbstractUser):
    pass


class Product(Model):
    pass


class ShoppingCart(Model):
    pass


class Payments(Model):
    pass
