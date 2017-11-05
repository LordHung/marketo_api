from django.db import models
from django.db.models.signals import pre_save

from .Product import Product


class Tag(models.Model):
    product = models.ManyToManyField(Product, blank=True)
    title = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField()

    objects = models.Manager()

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.title
