# Generated by Django 3.0.3 on 2020-07-15 08:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(decimal_places=3, max_digits=7, null=True, verbose_name='Quantity ( in g )'),
        ),
        migrations.AlterField(
            model_name='product',
            name='alcohol_content',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
