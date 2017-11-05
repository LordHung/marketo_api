from django.db import models
from django.db.models.signals import post_save


class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.title


# class Subcategory(models.Model):
#     category = models.ForeignKey(Category)
#     title = models.CharField(unique=True, max_length=120)
#     description = models.TextField(blank=True, null=True)
#     active = models.BooleanField(default=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     # slug = models.SlugField(unique=True)

#     objects = models.Manager()

#     class Meta:
#         db_table = 'subcategory'

#     def __str__(self):
#         return self.title


# def category_post_saved_receiver(sender, instance, created, *args, **kwargs):
#     category = instance
#     subcategories = category.subcategory_set.all()
#     if subcategories.count() == 0:
#         default_subcategory = Subcategory()
#         default_subcategory.save()

# post_save.connect(category_post_saved_receiver, sender=Category)
