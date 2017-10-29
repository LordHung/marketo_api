import os
import random
from django.db import models
from django.conf import settings

# Dùng AUTH_USER_MODEL để set quan hệ, ko dùng get_user_model()
# reason: https://stackoverflow.com/questions/24629705/django-using-get-user-model-vs-settings-auth-user-model
User = settings.AUTH_USER_MODEL


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'stores/{new_filename}/{final_filename}'


class Store(models.Model):
    title = models.CharField(max_length=255)
    user = models.OneToOneField(User)
    active = models.BooleanField(default=True)
    icon = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0, null=True)
    reviews_count = models.PositiveIntegerField(default=0, null=True)
    rating_cache = models.PositiveSmallIntegerField(default=0, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'store'
