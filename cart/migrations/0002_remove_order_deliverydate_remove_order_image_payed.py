# Generated by Django 4.1.7 on 2023-04-08 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="DeliveryDate",
        ),
        migrations.RemoveField(
            model_name="order",
            name="image_payed",
        ),
    ]