from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#MODELS
from .models import Empleado
#FORM
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = 'inicio.html'

#! LIST VIEW
# 1.- Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    """ Lista todos los empleados """
    # model = Empleado  Ya no es necesario porque estamos sobreescribiendo el metodo get_queryset
    template_name = "persona/list_all.html"
    paginate_by = 6
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        ) 
        return lista

# 1.5 - Trae todos los empleados sin filtro
class ListaEmpleadosAdmin(ListView):
    model = Empleado  
    template_name = "persona/crud_empleados.html"
    paginate_by = 8
    context_object_name = 'lista'


# 2.- Listar todos los empleados que pertenecen a un area de la empresa
class ListByAreaEmpleado(ListView):
    """ Lista empleado de un area """
    template_name = "persona/list_by_area.html"
    context_object_name = 'filtro_area'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista
# 3.- Listar los empleados por palabra clave
class ListEmpleadoByKword(ListView):
    """ Lista empleado por palabra clave (buscador) """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        ) 
        return lista
# 4.- Listar habilidades de un empleado
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=self.kwargs['hability'])
        return empleado.habilidades.all()
    
# 5.- Listar empleados por trabajo  
class ListByJob(ListView):
    """ Lista empleado de un trabajo """
    template_name = "persona/list_by_job.html"
    context_object_name = 'filtro_job'
    # El job choice el value es numerico y no textual por eso no encuentra con el nombre del job
    def get_queryset(self):
        empleado = self.kwargs['job']
        filtro_job = Empleado.objects.filter(job=empleado)
        return filtro_job
    

#! DETAIL VIEW
class DetailEmpleado(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes'
        return context


#! TEMPLATE VIEW
class SuccessView(TemplateView):
    template_name = "persona/success.html"


#! CREATE VIEW
class CreateEmpleado(CreateView):
    template_name = "persona/add_empleado.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self,form):
        empleado = form.save(commit=False) 
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name 
        return super(CreateEmpleado, self).form_valid(form)


#! UPDATE VIEW
class UpdateEmpleado(UpdateView):
    template_name = "persona/update_empleado.html"
    model = Empleado
    fields = ['first_name','last_name','job','departamento','habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')


#! DELETE VIEW
class DeleteEmpleado(DeleteView):
    model = Empleado
    template_name = "persona/delete_empleado.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


#! FORM VIEW (app Departamento)
