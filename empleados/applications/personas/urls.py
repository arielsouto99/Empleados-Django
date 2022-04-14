from django.contrib import admin
from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    # Pagina inicio
    path('', views.InicioView.as_view(), name = 'inicio'),
    #LIST VIEW
    path('listar-todo-empleados/',views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar-by-area/<shorname>',views.ListByAreaEmpleado.as_view(), name='empleados_area'),
    path('buscar-empleado/',views.ListEmpleadoByKword.as_view()),
    path('listar-habilidades-empleado/<hability>',views.ListHabilidadesEmpleado.as_view()),
    path('listar-by-job/<job>',views.ListByJob.as_view()),
    path('listar-empleados-admin/',views.ListaEmpleadosAdmin.as_view(), name='empleados_admin'),
    # DETAIL VIEW
    path('ver-empleado/<pk>/',views.DetailEmpleado.as_view(), name='detail_empleado'),
    # CREATE VIEW
    path('add-empleado/',views.CreateEmpleado.as_view(), name='add_empleado'),
    # TEMPLATE VIEW
    path('success/',views.SuccessView.as_view(), name='correcto'),
    # UPDATE VIEW
    path('update-empleado/<pk>/',views.UpdateEmpleado.as_view(), name='modificar_empleado'),
    # DELETE VIEW
    path('delete-empleado/<pk>/',views.DeleteEmpleado.as_view(), name='eliminar_empleado'),
]