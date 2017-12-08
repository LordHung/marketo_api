import os
from django.db import models
from django.utils.text import slugify
from src.utils import get_filename_ext
from src.settings import MEDIA_ROOT


def upload_image_path(instance, filename):
    user_email = slugify(instance.product.store.user.email)  # test@gmail.com -> testgmailcom
    name = slugify(instance.name)  # nike-star-abc
    name, ext = get_filename_ext(filename)  # .png, .jpg
    image_path = f'{MEDIA_ROOT}/{user_email}/store/categories/{name}{ext}'
    # REMOVE EXISTS IMAGE DIR
    if os.path.exists(image_path) and instance.image:
        os.remove(image_path)
    return f'{user_email}/store/categories/{name}{ext}'


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name
