from django.contrib import admin

from .models import BillingProfile
from addresses.models import Address


class AddressInline(admin.StackedInline):
    model = Address


@admin.register(BillingProfile)
class BillingAdmin(admin.ModelAdmin):
    inlines = (AddressInline, )
    fields = ('user', 'email', 'phone', 'customer_id', )
    list_display = ('id', 'user', 'email', 'phone', 'active', )
    ordering = ('id', )
