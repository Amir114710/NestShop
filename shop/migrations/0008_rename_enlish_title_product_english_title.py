# Generated by Django 4.1.7 on 2023-04-05 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_like_comments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="enlish_title",
            new_name="english_title",
        ),
    ]
