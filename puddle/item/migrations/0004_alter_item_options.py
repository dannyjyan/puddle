# Generated by Django 5.0.1 on 2024-01-29 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_rename_categy_item_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',)},
        ),
    ]
