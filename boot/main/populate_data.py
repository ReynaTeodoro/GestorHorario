from main.models import Nivel, Modalidad, Materia, Curso, Horario

# Crear niveles
nivel1 = Nivel.objects.create(numero=1)
nivel2 = Nivel.objects.create(numero=2)
nivel3 = Nivel.objects.create(numero=3)
nivel4 = Nivel.objects.create(numero=4)
nivel5 = Nivel.objects.create(numero=5)

# Crear modalidades
modalidad_a = Modalidad.objects.create(nombre="A")
modalidad_1c_cc = Modalidad.objects.create(nombre="1C – CC")
modalidad_2c_cc = Modalidad.objects.create(nombre="2C – CC")
modalidad_null = Modalidad.objects.create(nombre="***")

# Datos de materias (Nivel, Nombre, Modalidad, Carga Horaria, Correlativas Regular, Correlativas Aprobadas)
materias = [
    (nivel1, "Análisis Matemático 1", modalidad_a, 5, [], []),
    (nivel1, "Álgebra y Geometría Analítica", modalidad_a, 5, [], []),
    (nivel1, "Física 1", modalidad_a, 5, [], []),
    (nivel1, "Inglés 1", modalidad_a, 2, [], []),
    (nivel1, "Lógica y Estructuras Discretas", modalidad_1c_cc, 3, [], []),
    (nivel1, "Algoritmos y Estructuras de Datos", modalidad_a, 5, [], []),
    (nivel1, "Arquitectura de Computadoras", modalidad_2c_cc, 4, [], []),
    (nivel1, "Sistemas y Procesos de Negocio", modalidad_1c_cc, 3, [], []),
    (nivel1, "Ingeniería y Sociedad", modalidad_2c_cc, 2, [], []),
    (nivel2, "Análisis Matemático 2", modalidad_a, 5, ["Análisis Matemático 1", "Álgebra y Geometría Analítica"], []),
    (nivel2, "Física 2", modalidad_a, 5, ["Física 1"], []),
    (nivel2, "Inglés 2", modalidad_a, 2, ["Inglés 1"], []),
    (nivel2, "Sintaxis y Semántica de los Lenguajes", modalidad_1c_cc, 4, ["Algoritmos y Estructuras de Datos"], []),
    (nivel2, "Paradigmas de Programación", modalidad_2c_cc, 4, ["Algoritmos y Estructuras de Datos"], []),
    (nivel2, "Sistemas Operativos", modalidad_a, 4, [], []),
    (nivel2, "Análisis de Sistemas de Información", modalidad_a, 6, [], []),
    (nivel2, "Probabilidad y Estadísticas", modalidad_1c_cc, 3, [], []),
    (nivel3, "Economía", modalidad_2c_cc, 3, [], []),
    (nivel3, "Bases de Datos", modalidad_1c_cc, 4, [], []),
    (nivel3, "Desarrollo de Software", modalidad_1c_cc, 4, [], []),
    (nivel3, "Comunicación de Datos", modalidad_a, 4, [], []),
    (nivel3, "Análisis Numérico", modalidad_2c_cc, 3, [], []),
    (nivel3, "Diseño de Sistemas de Información", modalidad_a, 6, [], []),
    (nivel3, "Seminario Integrador (Analista)", modalidad_2c_cc, 4, [], []),
    (nivel4, "Legislación", modalidad_2c_cc, 2, [], []),
    (nivel4, "Ingeniería y Calidad de Software", modalidad_2c_cc, 3, [], []),
    (nivel4, "Redes de Datos", modalidad_a, 4, [], []),
    (nivel4, "Investigación Operativa", modalidad_a, 4, [], []),
    (nivel4, "Simulación", modalidad_1c_cc, 3, [], []),
    (nivel4, "Tecnologías para la Automatización", modalidad_2c_cc, 3, [], []),
    (nivel4, "Administración de Sistemas de Información", modalidad_a, 6, [], []),
    (nivel5, "Inteligencia Artificial", modalidad_a, 3, [], []),
    (nivel5, "Ciencia de Datos", modalidad_2c_cc, 3, [], []),
    (nivel5, "Sistemas de Gestión", modalidad_a, 4, [], []),
    (nivel5, "Gestión Gerencial", modalidad_1c_cc, 3, [], []),
    (nivel5, "Seguridad en los Sistemas de Información", modalidad_1c_cc, 3, [], []),
    (nivel5, "Proyecto Final (Integradora)", modalidad_a, 6, [], []),
]

# Crear materias y establecer correlativas
for nivel, nombre, modalidad, carga_horaria, correlativas_regular_nombres, correlativas_aprobadas_nombres in materias:
    correlativas_regular = Materia.objects.filter(nombre__in=correlativas_regular_nombres)
    correlativas_aprobadas = Materia.objects.filter(nombre__in=correlativas_aprobadas_nombres)
    materia = Materia.objects.create(nivel=nivel, nombre=nombre, modalidad=modalidad, carga_horaria_semanal=carga_horaria)
    materia.correlativasRegular.set(correlativas_regular)
    materia.correlativasAprobadas.set(correlativas_aprobadas)
    materia.save()

