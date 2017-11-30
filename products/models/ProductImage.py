import random

from django.db import models
from django.utils.text import slugify

from src.utils import get_filename_ext

from .Product import Product


def upload_image_path(instance, filename):
    random_name = random.randint(1, 3910209312)
    user_email = slugify(instance.product.store.user.email)  # test@gmail.com -> testgmailcom
    title = slugify(instance.product.title)  # nike-star-abc
    name, ext = get_filename_ext(filename)  # .png, .jpg
    return f'{user_email}/store/products/{title}/{random_name}{ext}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to=upload_image_path)

    class Meta:
        db_table = 'product_image'

    def __str__(self):
        return self.product.title
