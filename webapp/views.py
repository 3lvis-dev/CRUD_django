from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona

def home(request):
	no_personas = Persona.objects.count()
	#personas = Persona.objects.all()
	personas = Persona.objects.order_by('id')
	return render(request, 'home.html', {'no_personas':no_personas,'personas': personas})
