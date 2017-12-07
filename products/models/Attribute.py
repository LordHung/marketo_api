from django.db import models


class Option(models.Model):
    name = models.CharField(max_length=50)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        db_table = 'attribute_option'

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=50)

    objects = models.Manager()

    class Meta:
        db_table = 'attribute'

    def __str__(self):
        return self.name
