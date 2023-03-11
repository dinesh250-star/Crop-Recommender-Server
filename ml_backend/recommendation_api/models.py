from django.db import models

# Create your models here.
class CropRecommender(models.Model):
    N = models.CharField(max_length=100)
    P = models.CharField(max_length=100)
    K = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    ph = models.CharField(max_length=100)
    rainfall = models.CharField(max_length=100)