# Generated by Django 3.2.25 on 2024-07-29 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20240729_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='curso',
            name='modalidad',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='hora_fin',
        ),
        migrations.RemoveField(
            model_name='horario',
            name='hora_inicio',
        ),
        migrations.RemoveField(
            model_name='modalidad',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='horario',
            name='dia_fin',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='dia_inicio',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='semana_fin',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='semana_inicio',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='materia',
            name='carga_horaria_semanal',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='materia',
            name='correlativasAprobadas',
            field=models.ManyToManyField(blank=True, related_name='correlativas_de_aprobadas', to='main.Materia'),
        ),
        migrations.AddField(
            model_name='materia',
            name='correlativasRegular',
            field=models.ManyToManyField(blank=True, related_name='correlativas_de_regular', to='main.Materia'),
        ),
        migrations.AddField(
            model_name='materia',
            name='modalidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.modalidad'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='materia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='main.materia'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='materia',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='modalidad',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='materia',
            name='nivel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='main.nivel'),
        ),
    ]
