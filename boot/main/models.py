from django.db import models
import random
from django.utils.html import format_html
class Nivel(models.Model):
    numero = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'Nivel {self.numero}'

class Modalidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    regular = models.BooleanField(default=True)
    aprobado = models.BooleanField(default=True)
    electiva = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default='#000000')
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name='materias', null=True, blank=True)
    nombre = models.CharField(max_length=200)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, null=True, blank=True)
    carga_horaria_semanal = models.PositiveIntegerField(default = 5)
    correlativasRegular = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='correlativas_de_regular')
    correlativasAprobadas = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='correlativas_de_aprobadas')
    def color_display(self):
        return format_html('<div style="width: 50px; height: 20px; background-color: {}; border: 1px solid #000;"></div>', self.color)
    
    color_display.short_description = 'Color'
    def random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))
    def save(self, *args, **kwargs):
        if not self.color or self.color == '#000000':
            self.color = self.random_color()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='horarios', null=True, blank=True)
    nombre = models.CharField( max_length=50)

    def __str__(self):
        return f'{self.nombre} - {self.materia.nombre}'

class Horario(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='horarios', null=True, blank=True)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, null=True, blank=True)
    DIAS_SEMANA = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
    ]
    
    dia = models.CharField(
        max_length=3,
        choices=DIAS_SEMANA,
        null=True,
        blank=True
    )
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    def __str__(self):
        return f'{self.dia} - {self.hora_inicio} - {self.hora_fin}'
