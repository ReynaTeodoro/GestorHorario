from django.urls import path
from .views import home_view, cursos_view,manage_course_schedule

main_url_patters = [
    path('',home_view,name='home'),
    path('cursos-y-horarios/<int:materia_id>/', cursos_view, name='cursos_view'),
    path('gestionar-horarios/', manage_course_schedule, name='manage_course_schedule'),
]
