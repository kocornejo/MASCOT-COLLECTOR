from django.db import models

# Create your models here.

class Mascot(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()