# Generated by Django 3.0.3 on 2020-07-05 19:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200705_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='six_digit_code',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)]),
        ),
    ]
