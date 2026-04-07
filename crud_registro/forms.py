from django import forms
from .models import Registro_civil

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro_civil
        fields = ['nombre', 
                    'apellido', 
                    'fecha_nacimiento', 
                    'lugar_nacimiento', 
                    'nacionalidad', 
                    'sexo'
                ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
