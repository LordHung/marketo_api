from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, pre_save

from stores.models import Store

from .Category import Category


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(tag__title__icontains=query)
                   )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField(max_length=120)
    store = models.ForeignKey(Store)
    categories = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(blank=True, unique=True)
    # default = models.ForeignKey('Subcategories', related_name='default_category', blank=True, null=True)
    # featured = models.BooleanField(default=False)
    # subcategories = models.ManyToManyField(Subcategory, blank=True)

    objects = ProductManager()

    class Meta:
        db_table = 'product'
        ordering = ['-title']

    def __str__(self):
        return self.title

    def get_image_url(self):
        img = self.productimage_set.first()
        if img:
            return img.image.url
        return img  # None


# Tạo variant default nếu user không nhập variant
def product_post_saved_receiver(sender, instance, created, *args, **kwargs):
    from .Variant import Variant
    product = instance
    variants = product.variant_set.all()
    if variants.count() == 0:
        default_variant = Variant(product=product, title='Default', price=product.price)
        default_variant.save()

post_save.connect(product_post_saved_receiver, sender=Product)


# Tạo category nếu user không nhập category
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    product = instance
    category = Category.objects.filter(title__startswith='Default')
    if not category:
        category = Category(title='Default')
    if not product.categories:
        product.categories = category

pre_save.connect(product_post_saved_receiver, sender=Product)
