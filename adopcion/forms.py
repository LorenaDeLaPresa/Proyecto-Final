from django import forms
from adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos':'Apellidos',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio':'Domicilio',
        }
        widgets = {
            
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.Textarea(attrs={'class':'form-control'}),
        }


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'numero_animales',
            'razones',
        ]
        labels = {
            'numero_animales': 'Numero de animales',
            'razones':'Razones para adoptar',
        }
        widgets = {            
            'numero_animales':forms.TextInput(attrs={'class':'form-control'}),
            'razones':forms.Textarea(attrs={'class':'form-control'}),
        }