from django.contrib import admin

from .models import Order, LineItem


class LineItemInline(admin.TabularInline):
    model = LineItem
    can_delete = False
    readonly_fields = ('order', 'product', 'quantity', 'refunded', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('customer', 'status', 'active', 'payment_method', 'payment_method_title',
              'billing_address', 'shipping_address', 'shipping_total', 'total', 'customer_note', 'currency')
    readonly_fields = ('shipping_total', 'total', 'payment_method',
                       'customer_note', 'billing_address', 'shipping_address', )
    list_display = ('id', 'customer', 'status', 'payment_method', 'total', 'updated', 'timestamp', )
    list_display_links = ('id', 'customer', )
    inlines = (LineItemInline, )
    ordering = ('-updated', )
