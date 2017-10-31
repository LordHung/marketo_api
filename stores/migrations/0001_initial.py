# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 09:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from stores.models.Store import upload_image_path


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to=upload_image_path)),
                ('views_count', models.PositiveIntegerField(default=0, null=True)),
                ('reviews_count', models.PositiveIntegerField(default=0, null=True)),
                ('rating_cache', models.PositiveSmallIntegerField(default=0, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'store',
            },
        ),
        migrations.CreateModel(
            name='StoreReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('comment', models.TextField(blank=True, default='', null=True)),
                ('approved', models.BooleanField(default=1)),
                ('spam', models.BooleanField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'store_review',
            },
        ),
    ]
