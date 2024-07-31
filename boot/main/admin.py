from django.contrib import admin
from .models import *
import random

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def reasignar_colores(modeladmin, request, queryset):
    for obj in queryset:
        obj.color = random_color()
        obj.save()

reasignar_colores.short_description = "Reasignar colores aleatorios a los seleccionados"

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'color_display','nivel', 'regular', 'aprobado', 'modalidad', 'carga_horaria_semanal')
    list_filter = ('nivel', 'modalidad')
    search_fields = ('nombre',)
    filter_horizontal = ('correlativasRegular', 'correlativasAprobadas')
    actions = [reasignar_colores]
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'materia')
    list_filter = ('materia',)
    search_fields = ('nombre', 'materia__nombre')
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id','modalidad','dia', 'hora_inicio', 'hora_fin', 'curso')
    list_filter = ('modalidad','dia', 'curso__materia__nombre')
    search_fields = ('dia', 'curso__nombre')
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Nivel)
admin.site.register(Modalidad)


# Register your models here.
