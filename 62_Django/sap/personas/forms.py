from django.forms import ModelForm, widgets
from personas.models import	 Persona
from personas.models import	 Domicilio

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email':widgets.EmailInput(attrs={'type':'email'})
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'num_calle':widgets.TextInput(attrs={'type':'number'})
        }
