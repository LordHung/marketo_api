from django.conf import settings
from django.db import models

from .Product import Product

User = settings.AUTH_USER_MODEL


class ProductReview(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    rating = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    comment = models.TextField(default='', blank=True, null=True)
    approved = models.BooleanField(default=True)
    spam = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'product_review'
