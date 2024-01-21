from django.db import models

# Create your models here.
class Path(models.Model):
    alt = models.CharField(max_length=50)
    endpoint = models.CharField(max_length=500)