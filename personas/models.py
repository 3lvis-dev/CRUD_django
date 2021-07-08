from django.db import models

# Create your models here.

class Persona(models.Model):
	"""docstring for Persona"""
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
		