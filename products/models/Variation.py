import os

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from src.utils import get_filename_ext
from src.settings import MEDIA_ROOT


def upload_image_path(instance, filename):
    user_email = slugify(instance.product.store.user.email)  # test@gmail.com -> testgmailcom
    product_title = slugify(instance.product.title)
    title = slugify(instance.title)  # nike-star-abc
    name, ext = get_filename_ext(filename)  # .png, .jpg
    image_path = f'{MEDIA_ROOT}/{user_email}/store/products/{product_title}/{title}{ext}'
    # REMOVE EXISTS IMAGE DIR
    if os.path.exists(image_path) and instance.image:
        os.remove(image_path)
    return f'{user_email}/store/products/{product_title}/{title}{ext}'


class Variation(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    active = models.BooleanField(default=True)
    inventory = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'variation'
    
    def __str__(self):
        return self.name


def variant_pre_save_receiver(sender, instance, *args, **kwargs):
    current_one = Variation.objects.filter(id=instance.id).first()
    if instance.id and not instance.image:  # PUT method, not changes image
        instance.image = current_one.image

pre_save.connect(variant_pre_save_receiver, sender=Variation)        
