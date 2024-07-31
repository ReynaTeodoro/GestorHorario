from django.shortcuts import render
from .models import Materia, Curso, Horario,Modalidad,Nivel
from django.http import JsonResponse
from django.core.serializers import serialize
# Create your views here.
def home_view(request):
    materias = Materia.objects.filter(aprobado=False)
    aprobadas = Materia.objects.filter(aprobado=True)
    #materias = Materia.objects.all()
    cursos = Curso.objects.all()
    horarios = Horario.objects.all()
    modalidades = Modalidad.objects.all()
    niveles = Nivel.objects.all()
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes","Sabado"]
    materias_no_aprobadas = serialize('json', materias)
    materias_aprobadas = serialize('json', aprobadas)
    return render(request, 'home/home.html', {'materias': materias, 'cursos': cursos,
                                               'horarios': horarios, 'dias': dias,
                                                'modalidades':modalidades,
                                                'niveles':niveles,'aprobadas':aprobadas,
                                                'materias_no_aprobadas':materias_no_aprobadas,
                                                'materias_aprobadas':materias_aprobadas})
# views.py



def cursos_view(request, materia_id):
    cursos = Curso.objects.filter(materia_id=materia_id).prefetch_related('horarios')
    data = {
        'cursos': [
            {
                'nombre': curso.nombre,
                'materia': curso.materia.nombre,
                'modalidad': curso.horarios.first().modalidad.nombre,
                'color': curso.materia.color,
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
