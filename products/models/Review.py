from decimal import Decimal

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from ..models import Product

User = settings.AUTH_USER_MODEL

RATING = ((0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5))


class ReviewManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(approved=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0, choices=RATING, blank=True, null=True)
    comment = models.TextField(default='', blank=True, null=True)
    approved = models.BooleanField(default=False)
    spam = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'product_review'


def calculate_avg_rating_receiver(sender, instance, created, *args, **kwargs):
    product = Product.objects.get(id=instance.product.id)
    avg_rating = product.average_rating
    inst_rating = Decimal(instance.rating)

    if avg_rating != 0.0:
        total_rating = 0.0
        for rev in product.review_set.all():  # Need to optimize this instead of re-calculate 
            total_rating += rev.rating
        product.average_rating = total_rating / product.review_set.count()

    elif avg_rating == 0.0:
        product.average_rating = inst_rating
    product.save()

post_save.connect(calculate_avg_rating_receiver, sender=Review)
