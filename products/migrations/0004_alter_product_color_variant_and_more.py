# Generated by Django 4.1.5 on 2023-02-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_colorvariant_sizevariant_product_color_variant_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="color_variant",
            field=models.ManyToManyField(blank=True, to="products.colorvariant"),
        ),
        migrations.AlterField(
            model_name="product",
            name="size_variant",
            field=models.ManyToManyField(blank=True, to="products.sizevariant"),
        ),
    ]
