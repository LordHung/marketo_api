from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

RATING = ((0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5))


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.FloatField(default=0, choices=RATING, blank=True, null=True)
    comment = models.TextField(default='', blank=True, null=True)
    approved = models.BooleanField(default=True)
    spam = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'product_review'
