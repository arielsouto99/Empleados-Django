from django.db import models
# Importamos los modelos de Departamento para la relacion
from applications.departamento.models import Departamento
# Importamos ckeditor
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return self.habilidad



class Empleado(models.Model):
    """ Modelo para tabla empleado """
    job_choices = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','PROGRAMADOR'),
        ('4','OTRO'),
    )
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajo',max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="empleado",blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField(blank = True)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-id']
        unique_together = ('first_name','departamento')

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
    