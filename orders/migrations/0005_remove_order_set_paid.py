# Generated by Django 2.0 on 2017-12-31 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='set_paid',
        ),
    ]