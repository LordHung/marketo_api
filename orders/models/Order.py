from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

PAYMENT_METHOD_CHOICES = (
    ('cod', 'COD'),
    ('stripe', 'Stripe'),
    ('paypal', 'Paypal'),
)

CURRENCY_CHOICES = (
    ('vnd', 'VND'),
    ('usd', 'USD'),
)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=ORDER_STATUS_CHOICES, default='created')
    payment_method = models.CharField(max_length=120, default='COD', choices=PAYMENT_METHOD_CHOICES)
    payment_method_title = models.CharField(max_length=50, blank=True, null=True)
    billing_address = models.ForeignKey(
        'addresses.Address', on_delete=models.CASCADE, related_name='billing_address', blank=True, null=True)
    shipping_address = models.ForeignKey(
        'addresses.Address', on_delete=models.CASCADE, related_name='shipping_address', blank=True, null=True)
    customer_note = models.TextField(max_length=250, blank=True, null=True)
    shipping_total = models.DecimalField(
        default=20000.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    currency = models.CharField(max_length=50, default='VND')
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # set_paid = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        db_table = 'order'
