from django.urls import path
from . import views

urlpatterns = [
    # Propietario CRUD
    path('propietarios/', views.lista_propietarios, name='lista_propietarios'),
    path('propietarios/crear/', views.crear_propietario, name='crear_propietario'),
    path('propietarios/editar/<int:propietario_id>/', views.editar_propietario, name='editar_propietario'),
    path('propietarios/eliminar/<int:propietario_id>/', views.eliminar_propietario, name='eliminar_propietario'),

    # Vehiculo CRUD
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('vehiculos/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<int:vehiculo_id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:vehiculo_id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),

    # Registro CRUD
    path('registros/', views.lista_registros, name='lista_registros'),
    path('registros/ingreso/', views.registrar_ingreso, name='registrar_ingreso'),
    path('registros/salida/<int:registro_id>/', views.registrar_salida, name='registrar_salida'),
]
