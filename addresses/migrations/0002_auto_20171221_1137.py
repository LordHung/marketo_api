# Generated by Django 2.0 on 2017-12-21 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='state',
            new_name='district',
        ),
    ]
