from django.http.response import HttpResponse
from django.shortcuts import render
from personas.models import Persona
from personas.models import Domicilio

# Create your views here.
def bienvenido(request):
    num_personas= Persona.objects.count() 
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'num_personas': num_personas, 'personas':personas})

def domicilios(request):
    num_domicilios = Domicilio.objects.count()
    domicilio = Domicilio.objects.order_by('id')
    return render(request, 'domicilios.html', {'num_domicilios': num_domicilios, 'domicilios':domicilio})
