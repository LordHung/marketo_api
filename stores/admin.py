from django.contrib import admin

from .models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields = ('name', 'user', 'active', 'icon', 'views_count', 'reviews_count', 'rating_cache', )
    list_display = ('id', 'user', 'name', 'active', 'views_count', 'reviews_count', )
    readonly_fields = ('views_count', 'reviews_count', 'rating_cache', )
