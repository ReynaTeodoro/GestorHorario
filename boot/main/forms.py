from django import forms
from .models import Horario, Modalidad

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['dia', 'hora_inicio', 'hora_fin', 'modalidad']
        widgets = {
            'dia': forms.Select(choices=Horario.DIAS_SEMANA, attrs={'class': 'form-control'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'modalidad': forms.Select(attrs={'class': 'form-control'}),
        }
