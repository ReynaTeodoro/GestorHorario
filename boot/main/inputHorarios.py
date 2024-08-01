import django
from django.utils import timezone
from datetime import datetime
import os
# Inicializar Django si es necesario
django.setup()

from main.models import Curso, Horario  # Asegúrate de importar los modelos correctos
def input_time(prompt):
    while True:
        time_str = input(prompt)
        if time_str == '0':
            return None
        try:
            return datetime.strptime(time_str, '%H%M').time()
        except ValueError:
            print("Formato de hora no válido. Debe ser en el formato HHMM (ej. 1900 para 19:00).")


cursos = Curso.objects.all()
for curso in cursos:
    print(f'\nCurso: {curso.nombre} - {curso.materia.nombre}')
    print('Horarios actuales:')
    for horario in curso.horarios.all():
        print(f'  {horario.dia} - {horario.hora_inicio} - {horario.hora_fin}')
    
    while True:
        dia = input('Ingrese el día (LUN, MAR, MIE, JUE, VIE, SAB) o "0" para finalizar: ')
        if dia == '0':
            break
        hora_inicio = input_time('Ingrese la hora de inicio (HHMM) o "0" para finalizar: ')
        if hora_inicio is None:
            break
        hora_fin = input_time('Ingrese la hora de fin (HHMM) o "0" para finalizar: ')
        if hora_fin is None:
            break
        
        nuevo_horario = Horario(
            curso=curso,
            dia=dia,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            modalidad=5
        )
        nuevo_horario.save()
        print(f'Horario agregado: {dia} - {hora_inicio} - {hora_fin}')

print("Proceso completado.")
