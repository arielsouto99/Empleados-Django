from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre',max_length=50) # mc
    shor_name = models.CharField('Nombre corto', max_length=50, unique=True) # mc
    anulate = models.BooleanField('Anulado', default=False) #mb

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['id']
        unique_together = ('name','shor_name')

    def __str__(self):
        # return str(self.id) + ' - ' + self.shor_name MUESRTA NUMERO DE DEPARTAMENTO Y SU NOMBRE CORTO
        return self.shor_name
    