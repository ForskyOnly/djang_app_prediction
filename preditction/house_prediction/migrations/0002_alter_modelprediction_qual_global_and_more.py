# Generated by Django 4.1 on 2023-02-26 20:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_prediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelprediction',
            name='qual_global',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(13)]),
        ),
        migrations.AlterField(
            model_name='modelprediction',
            name='qual_vue',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
