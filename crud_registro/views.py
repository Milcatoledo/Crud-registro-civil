from django.shortcuts import render, redirect
from .models import Registro_civil
from .forms import RegistroForm

def index(request):
    index = Registro_civil.objects.filter(is_active=True)
    form = RegistroForm()
    return render(request, 'index.html', {'registros': index, 'form': form})

def create_register(request):
    if request.method == 'GET':
        return render(request, 'create_register.html', 
                        {'form': RegistroForm()})
    else:
        form = RegistroForm(request.POST)
        if form.is_valid():
            Registro_civil.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                lugar_nacimiento=form.cleaned_data['lugar_nacimiento'],
                nacionalidad=form.cleaned_data['nacionalidad'],
                sexo=form.cleaned_data['sexo']
            )
            return redirect('index')
        else:
            return render(request, 'create_register.html', {'form': form})


def delete_register(request, id):
    registro = Registro_civil.objects.get(id=id)
    registro.is_active = False
    registro.save()
    return redirect('index')

def update_register(request, id):
    registro = Registro_civil.objects.get(id=id)
    if request.method == 'GET':
        form = RegistroForm(instance=registro)
        return render(request, 'update_register.html', {'form': form})
    else:
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'update_register.html', {'form': form})
