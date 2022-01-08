from django.shortcuts import get_object_or_404, redirect, render
from personas.models import Persona, Domicilio
from personas.forms import PersonaForm, DomicilioForm

# Create your views here.
def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona':persona})

def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'personas/detalle_domicilio.html', {'domicilio':domicilio})

#PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formPersona = PersonaForm(request.POST)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('index')
    else:
        formPersona = PersonaForm()
    
    return render(request, 'personas/nuevo.html', {'formPersona':formPersona})

def nuevoDomicilio(request):
    if request.method == 'POST':
        formDomicilio = DomicilioForm(request.POST)
        if formDomicilio.is_valid():
            formDomicilio.save()
            return redirect('domicilios')
    else:
        formDomicilio = DomicilioForm()

    return render(request, 'personas/nuevo_domicilio.html', {'formDomicilio':formDomicilio})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)

    if request.method == 'POST':
        formPersona = PersonaForm(request.POST, instance=persona)
        if formPersona.is_valid():
            formPersona.save()
            return redirect('index')
    else:
        formPersona = PersonaForm(instance=persona)
    
    return render(request, 'personas/editar.html', {'formPersona':formPersona})

def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)

    if request.method == 'POST':
        formDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formDomicilio.is_valid():
            formDomicilio.save()
            return redirect('domicilios')
    else:
        formDomicilio = DomicilioForm(instance=domicilio)
    
    return render(request, 'personas/editar_domicilio.html', {'formDomicilio':formDomicilio})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)

    if persona:
        persona.delete()

    return redirect('index')

def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)

    if domicilio:
        domicilio.delete()

    return redirect('domicilios')


