# Generated by Django 4.1.6 on 2023-03-17 13:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_rename_image_post_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
    ]