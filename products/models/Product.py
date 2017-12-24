from django.db import models
from django.urls import reverse
from django.db.models import Q


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(purchasable=True)

    def search(self, query):
        lookups = (Q(name__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(tag__name__icontains=query)
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


STATUS = (
    ('available', 'Available'),
    ('out-of-stock', 'Out of stock'),
)


class Product(models.Model):
    name = models.CharField(max_length=120)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    attributes = models.ManyToManyField('Attribute', blank=True)

    price = models.DecimalField(max_digits=20, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS)

    purchasable = models.BooleanField(default=True)
    reviews_allowed = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(blank=True, unique=True)

    objects = ProductManager()

    class Meta:
        db_table = 'product'
        ordering = ['-name']

    def __str__(self):
        return self.name

    def get_image_url(self):
        img = self.image_set.first()
        if img:
            return img.image.url
        return img  # None


# Tạo variation default nếu user không nhập variation
def product_post_saved_receiver(sender, instance, created, *args, **kwargs):
    from .Variation import Variation
    product = instance
    variations = product.variation_set.all()
    if variations.count() == 0:
        default_variation = Variation(product=product, name='Default', price=product.price)
        default_variation.save()

# post_save.connect(product_post_saved_receiver, sender=Product)
