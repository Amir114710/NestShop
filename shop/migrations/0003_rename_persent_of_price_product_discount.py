# Generated by Django 4.1.5 on 2023-03-28 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_product_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="persent_of_price",
            new_name="discount",
        ),
    ]
