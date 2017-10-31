from django.db import models
from django.conf import settings
from . import Store

User = settings.AUTH_USER_MODEL


#
# Combine Rating and Comment in One Table
# reason: https://maxoffsky.com/code-blog/laravel-shop-tutorial-1-building-a-review-system/
#
class StoreReview(models.Model):
    user = models.ForeignKey(User)
    store = models.ForeignKey(Store)
    rating = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    comment = models.TextField(default='', blank=True, null=True)
    approved = models.BooleanField(default=1)
    spam = models.BooleanField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'store_review'
