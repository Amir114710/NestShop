# Generated by Django 4.1.5 on 2023-03-29 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_rename_discount_product_discount_persent"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="discount",
            field=models.SmallIntegerField(
                blank=True, default=0, null=True, verbose_name="قیمت با تخفیف"
            ),
        ),
    ]