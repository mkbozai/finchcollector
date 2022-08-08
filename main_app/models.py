from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    habitat = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
