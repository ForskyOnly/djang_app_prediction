# Generated by Django 4.1 on 2023-02-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_prediction', '0004_alter_modelprediction_vue_mer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelprediction',
            name='vue_mer',
            field=models.IntegerField(default=0),
        ),
    ]
