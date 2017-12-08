import random

from django.db import models
from django.utils.text import slugify

from src.utils import get_filename_ext
from src.settings import MEDIA_URL


def upload_image_path(instance, filename):
    random_name = random.randint(1, 3910209312)
    user_email = slugify(instance.product.store.user.email)  # test@gmail.com -> testgmailcom
    name = slugify(instance.product.name)  # nike-star-abc
    name, ext = get_filename_ext(filename)  # .png, .jpg
    return f'{user_email}/store/products/{name}/{random_name}{ext}'


class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path)

    class Meta:
        db_table = 'product_image'

    def __str__(self):
        # return self.product.title
        return self.image.url
