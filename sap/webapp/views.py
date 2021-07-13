from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona, Domicilio

def home(request):
	no_personas = Persona.objects.count()
	#personas = Persona.objects.all()
	personas = Persona.objects.order_by('id')
	return render(request, 'home.html', {'no_personas':no_personas,'personas':personas})

def domicilios(request):
	no_domicilios = Domicilio.objects.count()
	#domicilios = Domicilio.objects.all()
	domicilios = Domicilio.objects.order_by('id')
	return render(request, 'domicilios.html', {'no_domicilios':no_domicilios, 'domicilios':domicilios})
