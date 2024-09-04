# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Propietario, Vehiculo, Registro
from django.utils import timezone

# Propietario CRUD
def lista_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'lista_propietarios.html', {'propietarios': propietarios})

def crear_propietario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_apartamento = request.POST.get('numero_apartamento')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')

        Propietario.objects.create(
            nombre=nombre,
            numero_apartamento=numero_apartamento,
            telefono=telefono,
            email=email
        )
        return redirect('lista_propietarios')
    return render(request, 'crear_propietario.html')

def editar_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    if request.method == 'POST':
        propietario.nombre = request.POST.get('nombre')
        propietario.numero_apartamento = request.POST.get('numero_apartamento')
        propietario.telefono = request.POST.get('telefono')
        propietario.email = request.POST.get('email')
        propietario.save()
        return redirect('lista_propietarios')
    return render(request, 'editar_propietario.html', {'propietario': propietario})

def eliminar_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    propietario.delete()
    return redirect('lista_propietarios')

# Vehiculo CRUD
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method == 'POST':
        propietario_id = request.POST.get('propietario')
        matricula = request.POST.get('matricula')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        color = request.POST.get('color')

        propietario = get_object_or_404(Propietario, id=propietario_id)
        Vehiculo.objects.create(
            propietario=propietario,
            matricula=matricula,
            marca=marca,
            modelo=modelo,
            color=color
        )
        return redirect('lista_vehiculos')
    propietarios = Propietario.objects.all()
    return render(request, 'crear_vehiculo.html', {'propietarios': propietarios})

def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        vehiculo.matricula = request.POST.get('matricula')
        vehiculo.marca = request.POST.get('marca')
        vehiculo.modelo = request.POST.get('modelo')
        vehiculo.color = request.POST.get('color')
        vehiculo.save()
        return redirect('lista_vehiculos')
    propietarios = Propietario.objects.all()
    return render(request, 'editar_vehiculo.html', {'vehiculo': vehiculo, 'propietarios': propietarios})

def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    vehiculo.delete()
    return redirect('lista_vehiculos')

# Registro CRUD
def lista_registros(request):
    registros = Registro.objects.all()
    return render(request, 'lista_registros.html', {'registros': registros})

def registrar_ingreso(request):
    if request.method == 'POST':
        vehiculo_id = request.POST.get('vehiculo')
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        Registro.objects.create(vehiculo=vehiculo)
        return redirect('lista_registros')
    vehiculos = Vehiculo.objects.all()
    return render(request, 'registrar_ingreso.html', {'vehiculos': vehiculos})

def registrar_salida(request, registro_id):
    registro = get_object_or_404(Registro, id=registro_id)
    if request.method == 'POST':
        registro.fecha_hora_salida = timezone.now()
        registro.save()
        return redirect('lista_registros')
    return render(request, 'registrar_salida.html', {'registro': registro})
