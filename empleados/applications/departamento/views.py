from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from .models import Departamento
from applications.personas.models import Empleado

#! FORM VIEW 
class NewDepartamentoView(FormView):

    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self,form):
        print('******** Estamos en el form valid ********')

        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shor_name'],
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = 1, #administrador
            departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)



class ListDepartamento(ListView):
    model = Departamento
    template_name = "departamento/list_departamento.html"
    context_object_name = 'lista'

    
    