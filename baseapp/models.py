from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    text = models.TextField(blank=False, default='')
