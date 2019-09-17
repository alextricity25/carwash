from django.db import models

class Towels(models.Model):
    name = models.CharField(max_length = 50)
    material = models.CharField(max_length = 50)
    gsm = models.IntegerField()
    origin = models.CharField(max_length = 50)
    blend_ratio = models.CharField(max_length = 50)
