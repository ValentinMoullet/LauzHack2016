from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stat(models.Model):
	avg_happiness = models.DecimalField(max_digits=9, decimal_places=8)
	avg_sadness = models.DecimalField(max_digits=9, decimal_places=8)
	avg_surprise = models.DecimalField(max_digits=9, decimal_places=8)
	# In seconds
	timestamp = models.IntegerField()

class Video(models.Model):
	url = models.CharField(max_length=200)
	# In seconds
	length = models.IntegerField()
	stats = models.ManyToManyField(Stat)
	nb_views = models.IntegerField(default=0)
	avg_age = models.DecimalField(max_digits=5, decimal_places=3, default=0.0)
