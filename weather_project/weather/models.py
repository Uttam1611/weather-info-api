# Create your models here.
from django.db import models

class WeatherRecord(models.Model):
    city = models.CharField(max_length=100)
    temp = models.FloatField()
    humidity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)