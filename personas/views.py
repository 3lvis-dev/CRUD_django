from django.shortcuts import render, get_object_or_404, redirect
from personas.models import Persona
from personas.forms import PersonaForm
from django.forms import modelform_factory

# Create your views here.

'''
Aqui se encuentran los metodos CRUD (Create - Read - Update - Delete)
para nuestra app SAP (Sistema de Administración de Personas)
'''

#*** Metodo de ver que equivale al Read de nuestro CRUD *************
def detallePersona(request, id):
	#persona = Persona.objects.get(pk=id)
	persona = get_object_or_404(Persona, pk=id)
	return render(request, 'personas/detalle.html', {'persona':persona})

#*** Metodo de agregar que equivale al Create de nuestro CRUD *************
def nuevaPersona(request):
	if request.method == 'POST':
		formaPersona = PersonaForm(request.POST)
		if formaPersona.is_valid():
			formaPersona.save()
			return redirect('home')
	else:
		formaPersona = PersonaForm()

	return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})

#*** Metodo de ver que equivale al Update de nuestro CRUD *************
def editarPersona(request, id):
	persona = get_object_or_404(Persona, pk=id)
	if request.method == 'POST':
		formaPersona = PersonaForm(request.POST, instance=persona)
		if formaPersona.is_valid():
			formaPersona.save()
			return redirect('home')
	else:
		formaPersona = PersonaForm(instance=persona)

	return render(request, 'personas/editar.html', {'formaPersona':formaPersona})

#*** Metodo de ver que equivale al Delete de nuestro CRUD *************
def eliminarPersona(request, id):
	persona = get_object_or_404(Persona, pk=id)
	if persona:
		persona.delete()
	return redirect('home')

	