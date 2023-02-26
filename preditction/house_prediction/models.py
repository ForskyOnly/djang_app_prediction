from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ModelPrediction(models.Model):
    srf_de_vie = models.IntegerField(default=0)
    chambres = models.IntegerField(default=0)
    qual_global = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(13)])
    qual_vue =  models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    adresse = models.CharField(max_length=255)
    lat = models.FloatField(default=0.0)
    long = models.FloatField(default=0.0)
    vue_mer = models.IntegerField(default=0)
    prix_predit = models.FloatField(default=0.0)
