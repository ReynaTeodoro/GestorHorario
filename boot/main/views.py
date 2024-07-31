from django.shortcuts import render
from .models import Materia, Curso, Horario,Modalidad
from django.http import JsonResponse
# Create your views here.
def home_view(request):
    materias = Materia.objects.filter(aprobado=False)
    #materias = Materia.objects.all()
    cursos = Curso.objects.all()
    horarios = Horario.objects.all()
    modalidades = Modalidad.objects.all()
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    horas = ["08:00", "08:45", "09:30", "10:15", "11:00", "11:45", "12:05", "14:00"]
    return render(request, 'home/home.html', {'materias': materias, 'cursos': cursos, 'horarios': horarios, 'dias': dias, 'horas': horas,'modalidades':modalidades})
# views.py



def cursos_view(request, materia_id):
    cursos = Curso.objects.filter(materia_id=materia_id).prefetch_related('horarios')
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
                    for horario in curso.horarios.all()
                ]
            }
            for curso in cursos
        ]
    }
    return JsonResponse(data)
