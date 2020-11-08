from django.db import models


class Holiday(models.Model):
	title = models.CharField(max_length=100)
# Create your models here.
