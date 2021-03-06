from django.forms import ModelForm, EmailInput, TextInput
from personas.models import Persona, Domicilio


class PersonaForm(ModelForm):
	"""docstring for PersonaForm"""
	class Meta():
		model = Persona
		fields = '__all__'
		widgets = {
			'email': EmailInput(attrs={'type':'email'})
		}


class DomicilioForm(ModelForm):
	"""docstring for PersonaForm"""
	class Meta():
		model = Domicilio
		fields = '__all__'
		widgets = {
			'no_calle': TextInput(attrs={'type':'number'})
		}
