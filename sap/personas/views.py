from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio

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

# Metodos CRUD para Domicilios ***************************************

#*** VER, equivale al Read de nuestro CRUD *************
def detalleDomicilio(request, id):
	domicilio = get_object_or_404(Domicilio, pk=id)
	return render(request, 'personas/detalle_domicilio.html', {'domicilio':domicilio})


#*** AGREGAR, equivale al Create de nuestro CRUD *************
def nuevoDomicilio(request):
	if request.method == 'POST':
		formaDomicilio = DomicilioForm(request.POST)
		if formaDomicilio.is_valid():
			formaDomicilio.save()
			return redirect('/domicilios')
	else:
		formaDomicilio = DomicilioForm()

	return render(request, 'personas/nuevo_domicilio.html', {'formaDomicilio':formaDomicilio})

#*** EDITAR, equivale al Update de nuestro CRUD *************
def editarDomicilio(request, id):
	domicilio = get_object_or_404(Domicilio, pk=id)
	if request.method == 'POST':
		formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
		if formaDomicilio.is_valid():
			formaDomicilio.save()
			return redirect('/domicilios')
	else:
		formaDomicilio = DomicilioForm(instance=domicilio)

	return render(request, 'personas/editar_domicilio.html', {'formaDomicilio':formaDomicilio})

#*** ELIMINAR, equivale al Delete de nuestro CRUD *************
def eliminarDomicilio(request, id):
	domicilio = get_object_or_404(Domicilio, pk=id)
	if domicilio:
		domicilio.delete()
	return redirect('/domicilios')