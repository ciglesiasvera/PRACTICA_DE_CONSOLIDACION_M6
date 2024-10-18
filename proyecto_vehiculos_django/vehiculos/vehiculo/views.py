from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, 'index.html')

@login_required
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})

@login_required
def list_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    condiciones_precio = {
        'bajo': vehiculos.filter(precio__lte=10000),
        'medio': vehiculos.filter(precio__gt=10000, precio__lte=30000),
        'alto': vehiculos.filter(precio__gt=30000),
    }
    return render(request, 'vehiculo/list_vehiculos.html', {'vehiculos': vehiculos, 'condiciones_precio': condiciones_precio})