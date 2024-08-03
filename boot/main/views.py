from django.shortcuts import render, get_object_or_404, redirect
from .models import Materia, Curso, Horario,Modalidad,Nivel
from .forms import HorarioForm
from django.urls import reverse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.forms import formset_factory
# Create your views here.
def home_view(request):
    materias = Materia.objects.filter(aprobado=False).distinct()
    aprobadas = Materia.objects.filter(aprobado=True)
    #materias = Materia.objects.all()
    #obtener solo los cursos que tienen horarios relacionados
    cursos = Curso.objects.all().prefetch_related('horarios')
    horarios = Horario.objects.all()
    modalidades = Modalidad.objects.all()
    niveles = Nivel.objects.all()
    #dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes","Sabado"]
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
                'materia': curso.materia.nombre if curso.materia else 'Desconocido',  # Maneja posibles None
                'modalidad': curso.horarios.first().modalidad.nombre if curso.horarios.first() and curso.horarios.first().modalidad else 'Desconocida',
                'color': curso.materia.color if curso.materia else '#FFFFFF',  # Maneja posibles None
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


def manage_course_schedule(request):
    CursoFormSet = formset_factory(HorarioForm, extra=1)

    if request.method == 'POST':
        if 'course_select' in request.POST:
            curso_id = request.POST.get('curso')
            curso = Curso.objects.get(id=curso_id)
            horarios = Horario.objects.filter(curso=curso)
            form = HorarioForm()
            return render(request, 'manage_course_schedule.html', {
                'curso': curso,
                'horarios': horarios,
                'form': form,
                'curso_form': CursoFormSet(),
                'cursos': Curso.objects.all().order_by('nombre')
            })
        elif 'add_schedule' in request.POST:
            curso_id = request.POST.get('curso_id')
            curso = Curso.objects.get(id=curso_id)
            form = HorarioForm(request.POST)
            if form.is_valid():
                horario = form.save(commit=False)
                horario.curso = curso
                horarios = Horario.objects.filter(curso=curso)
                horario.save()
                return render(request, 'manage_course_schedule.html', {
                    'curso': curso,
                    'horarios': horarios,
                    'form': form,  # Limpiar el formulario después de agregar
                    'curso_form': CursoFormSet(),
                    'cursos': Curso.objects.all().order_by('nombre')
                })
        elif 'next_course' in request.POST or 'previous_course' in request.POST:
            curso_id = int(request.POST.get('curso_id'))
            cursos = Curso.objects.order_by('nombre')
            current_index = next((i for i, c in enumerate(cursos) if c.id == curso_id), -1)
            if 'next_course' in request.POST:
                next_index = (current_index + 1) % len(cursos)
            elif 'previous_course' in request.POST:
                next_index = (current_index - 1) % len(cursos)
            next_curso = cursos[next_index]
            horarios = Horario.objects.filter(curso=next_curso)
            form = HorarioForm()
            return render(request, 'manage_course_schedule.html', {
                'curso': next_curso,
                'horarios': horarios,
                'form': form,
                'curso_form': CursoFormSet(),
                'cursos': cursos
            })
    else:
        form = HorarioForm()
        curso_form = CursoFormSet()

    return render(request, 'manage_course_schedule.html', {
        'curso': None,
        'horarios': [],
        'form': form,
        'curso_form': curso_form,
        'cursos': Curso.objects.all().order_by('nombre')
    })
