# Generated by Django 4.1.5 on 2023-03-29 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_alter_product_discount"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="discount",
            new_name="discount_persent",
        ),
    ]
