# Generated by Django 2.0 on 2017-12-31 09:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20171231_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineitem',
            name='refunded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lineitem',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='order',
            name='set_paid',
            field=models.BooleanField(default=True),
        ),
    ]
