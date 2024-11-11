from django.contrib.auth.models import AbstractUser
from django.db.models import Model, FloatField, CharField, CASCADE, ForeignKey, SlugField, DateTimeField, OneToOneField, \
    ImageField
from django.utils.text import slugify


class User(AbstractUser):
    pass


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(TimeBaseModel):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name, allow_unicode=True)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)


class Product(TimeBaseModel):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    price = FloatField(db_default=0)
    discount_price = FloatField(db_default=0)
    category = ForeignKey('apps.Category', CASCADE, related_name='product')


class ProductImage(Model):
    image = ImageField(upload_to='products/%Y/%m/%d/')
    product = OneToOneField('apps.Product', CASCADE, related_name='product')


class Order(Model):
    pass

class Transaction(TimeBaseModel):
    pass
