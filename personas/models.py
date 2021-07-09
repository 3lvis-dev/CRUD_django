from django.db import models

# Create your models here.

class Domicilio(models.Model):
	"""docstring for Domicilio"""
	calle = models.CharField(max_length=255)
	no_calle = models.IntegerField()
	pais = models.CharField(max_length=255)

	def __str__(self):
		return f'''Domicilio {self.id}: 
		Calle: {self.calle} 
		N° de Calle: {self.no_calle} 
		País: {self.pais}'''


class Persona(models.Model):
	"""docstring for Persona"""
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
		
	def __str__(self):
		return f'''Persona {self.id}: 
		Nombre: {self.nombre} 
		Apellido: {self.apellido} 
		Email: {self.email} '''