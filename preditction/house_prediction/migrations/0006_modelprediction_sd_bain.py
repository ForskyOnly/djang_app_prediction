# Generated by Django 4.1 on 2023-02-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_prediction', '0005_alter_modelprediction_vue_mer'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelprediction',
            name='sd_bain',
            field=models.FloatField(default=0.0),
        ),
    ]