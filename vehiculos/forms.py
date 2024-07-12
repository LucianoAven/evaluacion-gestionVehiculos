from django import forms
from .models import Marca, Auto, Anio, Combustible, Pais

# Formularios para establecer el tipo de información que recibirá la base de datos 
# por parte del usuario.
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class AnioForm(forms.ModelForm):
    class Meta:
        model = Anio
        fields = '__all__'

class CombustibleForm(forms.ModelForm):
    class Meta:
        model = Combustible
        fields = '__all__'

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        # Se almacenan las columnas del modelo y se especifica el tipo de información que contendrán.
        fields = ['name', 'mark', 'price', 'year', 'fuel', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'mark': forms.Select(attrs={'class': 'form-control custom-class'}),
            'price': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            'year': forms.Select(attrs={'class': 'form-control custom-class'}),
            'fuel': forms.Select(attrs={'class': 'form-control custom-class'}),
            'country': forms.Select(attrs={'class': 'form-control custom-class'}),
        }
