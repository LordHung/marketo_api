# Generated by Django 2.0 on 2017-12-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20171213_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(blank=True, choices=[(1, 0.5), (2, 1), (3, 1.5), (4, 2), (5, 2.5), (6, 3), (7, 3.5), (8, 4), (9, 4.5), (10, 5)], default=0, null=True),
        ),
    ]
