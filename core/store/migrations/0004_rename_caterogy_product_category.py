# Generated by Django 4.1.6 on 2023-02-28 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='caterogy',
            new_name='category',
        ),
    ]
