from decimal import Decimal

from django.db import models
from django.db.models.signals import post_delete, pre_save, post_save


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    item = models.ForeignKey('Product', on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)
    # Tính tiền theo số lượng item: 3 cái ly 20k->60k
    line_item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item.name

    def remove(self):
        return self.item.remove_from_cart()

# Trước khi lưu cartitem thì tính tiền theo sỗ lượng


def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
    qty = instance.quantity
    if qty >= 1:
        price = instance.item.get_price()
        line_item_total = Decimal(qty) * Decimal(price)
        instance.line_item_total = line_item_total


pre_save.connect(cart_item_pre_save_receiver, sender='CartItem')


def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
    instance.cart.update_subtotal()


post_save.connect(cart_item_post_save_receiver, sender='CartItem')

post_delete.connect(cart_item_post_save_receiver, sender='CartItem')
