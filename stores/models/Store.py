import random
import os
import shutil

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.text import slugify

from src.settings import MEDIA_ROOT
from src.utils import get_filename_ext

# Dùng AUTH_USER_MODEL để set quan hệ, ko dùng get_user_model()
# reason: https://stackoverflow.com/questions/24629705/django-using-get-user-model-vs-settings-auth-user-model
User = settings.AUTH_USER_MODEL


def upload_image_path(instance, filename):
    user_email = slugify(instance.user.email)  # test@gmail.com -> testgmailcom
    name = slugify(instance.name)  # nike-star-abc
    name, ext = get_filename_ext(filename)  # .png, .jpg
    # email là unique
    image_path = f'{MEDIA_ROOT}/{user_email}/store/icon/'
    # REMOVE EXISTS IMAGE DIR
    if os.path.exists(image_path):
        shutil.rmtree(image_path)
    return f'{user_email}/store/icon/{name}{ext}'


class StoreQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = Q(name__icontains=query)  # Q(tag__name__icontains=query))
        # shop abc, xyz, quan ao, giay dep
        return self.filter(lookups).distinct()


class StoreManager(models.Manager):
    def get_queryset(self):
        return StoreQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Store.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Store(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=None)
    active = models.BooleanField(default=True)
    icon = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0, null=True)
    reviews_count = models.PositiveIntegerField(default=0, null=True)
    rating_cache = models.PositiveSmallIntegerField(default=0, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = StoreManager()

    class Meta:
        db_table = 'store'

    def __str__(self):
        return self.name
