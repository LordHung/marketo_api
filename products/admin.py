from django.contrib import admin

from .models import Product, Image, Variation, Category, Attribute, Option, Tag, Review


class ProductImageInline(admin.StackedInline):
    max_num = 10  # max img is 10
    extra = 1  # default show 1 img
    model = Image


class AttributeOptionInline(admin.StackedInline):
    max_num = 10
    extra = 3
    model = Option


class ProductAttributeInline(admin.StackedInline):
    model = Product.attributes.through


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    inlines = (AttributeOptionInline, )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('store', 'name', ('price', 'on_sale', 'sale_price'), 'quantity', 'status', 'purchasable',
              'reviews_allowed', ('description', 'short_description'), 'categories', 'attributes', 'tags', )
    # filter_horizontal = ('attributes', )  # select, filter
    list_display = ('id', 'name', 'store', 'price', 'sale_price',
                    'quantity', 'status', 'sold', 'purchasable', 'reviews_allowed', )
    list_display_links = ('id', 'name', )
    empty_value_display = '--empty--'
    inlines = (ProductImageInline, )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'parent', 'store', 'active', 'image', 'description', 'slug', )
    list_display = ('id', 'name', 'store', 'parent', 'active', )
    list_display_links = ('id', 'name')


@admin.register(Review)
class ProductReviewAdmin(admin.ModelAdmin):
    fields = ('user', 'product', 'rating', 'approved', 'spam', 'comment')
    list_display = ('id', 'user', 'product', 'rating', 'approved', 'spam')
    list_display_links = ('id', 'user', )
