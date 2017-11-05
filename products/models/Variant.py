import os

from django.db import models
from django.utils.text import slugify

from src.utils import get_filename_ext
from src.settings import MEDIA_ROOT


def upload_image_path(instance, filename):
    user_email = slugify(instance.user.email)  # test@gmail.com -> testgmailcom
    product_title = slugify(instance.product.title)
    title = slugify(instance.title)  # nike-star-abc
    name, ext = get_filename_ext(filename)  # .png, .jpg
    image_path = f'{MEDIA_ROOT}/{user_email}/store/products/{product_title}/{title}{ext}'
    # REMOVE EXISTS IMAGE DIR
    if os.path.exists(image_path):
        os.remove(image_path)
    return f'{user_email}/store/products/{product_title}/{title}{ext}'


class Variant(models.Model):
    from .Product import Product
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    active = models.BooleanField(default=True)
    inventory = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'variant'
    
    def __str__(self):
        return self.title
