from django.db import models

# Create your models here.

class TodoItem(models.Model):
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

class NameItem(models.Model):
	name = models.CharField(max_length=256)
	q_ozon = models.CharField(max_length=256)
	q_ym = models.CharField(max_length=256)
	q_sklad = models.CharField(max_length=256)
	barcode = models.CharField(max_length=256)
	price = models.CharField(max_length=256)