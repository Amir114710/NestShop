# Generated by Django 4.1.5 on 2023-03-28 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="shop/products",
                verbose_name="عکس اصلی کالا برای صفحه ی فروشگاه",
            ),
        ),
    ]
