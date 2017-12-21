from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL


class BillingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='billing')
    customer_id = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = 'billing_profile'

    def __str__(self):
        return str(self.user)


def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email and instance.phone:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email, phone=instance.phone)

post_save.connect(user_created_receiver, sender=User)
