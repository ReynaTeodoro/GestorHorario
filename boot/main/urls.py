from django.urls import path
from .views import home_view, cursos_view

main_url_patters = [
    path('',home_view,name='home'),
    path('api/cursos/<int:materia_id>/', cursos_view, name='cursos_view'),
]
