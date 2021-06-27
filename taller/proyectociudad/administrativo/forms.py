from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo_edificio']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese la dirección por favor'),
            'ciudad': _('Ingrese la ciudad por favor'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        palabra = (valor[0])

        if (palabra == "L"):
            raise forms.ValidationError("No puede contener un 'L' en el nombre de la ciudad")
        return valor


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_prop', 'costo_depart', 'numero_cuartos', 'edificio']

    def clean_costo_depart(self):
        valor = self.cleaned_data['costo_depart']

        if valor > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a 100000")
        return valor

    def clean_numero_cuartos(self):
        valor = self.cleaned_data['numero_cuartos']

        if (valor == 0 or valor > 7):
            raise forms.ValidationError("El número de cuartos no puede ser 0 ni mayor a 7")
        return valor

    def clean_nombre_prop(self):
        valor = self.cleaned_data['nombre_prop']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese más de dos nombres por favor")
        return valor

    

class EdificioDepartamentoForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(EdificioDepartamentoForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombre_prop', 'costo_depart', 'numero_cuartos', 'edificio']
        
    def clean_costo_depart(self):
        valor = self.cleaned_data['costo_depart']

        if valor > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a 100000")
        return valor

    def clean_numero_cuartos(self):
        valor = self.cleaned_data['numero_cuartos']

        if (valor == 0 or valor > 7):
            raise forms.ValidationError("El número de cuartos no puede ser 0 ni mayor a 7")
        return valor


    def clean_nombre_prop(self):
        valor = self.cleaned_data['nombre_prop']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese más de dos nombres por favor")
        return valor