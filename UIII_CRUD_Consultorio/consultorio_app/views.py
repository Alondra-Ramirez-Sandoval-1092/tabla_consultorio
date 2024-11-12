from django.shortcuts import render,redirect
from .models import Consultorio
# Create your views here.

def inicio_vista(request):
    elconsultorio=Consultorio.objects.all()
    return render(request,"gestionarConsultorio.html",{"miconsultorio" :elconsultorio})

def registrarConsultorio(request):
    id_consult=request.POST["skzid"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    doctor=request.POST["skzdoctor"]
    especialidad=request.POST["skzespecialidad"]
    horario=request.POST["skzhorario"]
    cita=request.POST["skzcita"]

    guardarconsultorio=Consultorio.objects.create(id_consult=id_consult,nombre=nombre,telefono=telefono,doctor=doctor,especialidad=especialidad,horario=horario,cita=cita)

    return redirect('/')
    

def seleccionarConsultorio(request,codigo):
    materia=Consultorio.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"mismaterias":materia})

def editarConsultorio(request,codigo):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtmateria"]
    creditos=request.POST["numcreditos"]
    materia=Consultorio.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    materia.save()
    redirect('/')
    

def borrarConsultorio(request,codigo):
    materia=Consultorio.objects.get(codigo=codigo)
    materia.delete()
    
    return redirect('/')

