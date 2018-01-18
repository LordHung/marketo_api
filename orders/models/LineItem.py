from django.db import models
from django.db.models.signals import post_save

from products.models import Product


class LineItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    refunded = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'line_item'

    def __str__(self):
        return str(self.id)


def calculate_sold_product_receiver(sender, instance, created, *args, **kwargs):
    product = Product.objects.get(id=instance.product.id)
    item_quantity = instance.quantity
    print('DEBUG', product.name)
    product.sold += 1

    if product.quantity == item_quantity:
        product.quantity -= item_quantity
        product.purchasable = False
    elif product.quantity > item_quantity:
        product.quantity -= item_quantity
    else:
        raise Exception('Đã hết hàng!')

    print(product.quantity, product.sold)
    product.save()

post_save.connect(calculate_sold_product_receiver, sender=LineItem)