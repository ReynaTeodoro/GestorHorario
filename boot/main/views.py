from django.shortcuts import render
from .models import Materia, Curso, Horario
# Create your views here.
def home_view(request):
    materias = Materia.objects.filter(aprobado=False)
    cursos = Curso.objects.all()
    horarios = Horario.objects.all()
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    horas = ["08:00", "08:45", "09:30", "10:15", "11:00", "11:45", "12:05", "14:00"]
    return render(request, 'home/home.html', {'materias': materias, 'cursos': cursos, 'horarios': horarios, 'dias': dias, 'horas': horas})
# views.py


from django.http import JsonResponse
from .models import Curso, Horario

def cursos_view(request, materia_id):
    cursos = Curso.objects.filter(materia_id=materia_id).prefetch_related('horario_set')
    data = {
        'cursos': [
            {
                'nombre': curso.nombre,
                'horarios': [
                    {
                        'dia': horario.dia,
                        'hora_inicio': horario.hora_inicio.strftime('%H:%M'),
                        'hora_fin': horario.hora_fin.strftime('%H:%M'),
                    }
                    for horario in curso.horario_set.all()
                ]
            }
            for curso in cursos
        ]
    }
    return JsonResponse(data)
