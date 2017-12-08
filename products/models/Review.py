from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    comment = models.TextField(default='', blank=True, null=True)
    approved = models.BooleanField(default=True)
    spam = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'product_review'
