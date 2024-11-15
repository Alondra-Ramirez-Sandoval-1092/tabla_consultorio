from django.shortcuts import render,redirect
from .models import Consultorio
# Create your views here.

def inicio_vista(request):
    elconsultorio=Consultorio.objects.all()
    return render(request,"gestionarConsultorio.html",{"miconsultorio":elconsultorio})

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
    

def seleccionarConsultorio(request,id_consult):
    consultorio=Consultorio.objects.get(id_consult=id_consult)
    return render(request,"editarConsultorio.html",{"miconsultorio":consultorio})

def editarConsultorio(request,id_consult):
    id_consult=request.POST["skzid"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    doctor=request.POST["skzdoctor"]
    especialidad=request.POST["skzespecialidad"]
    horario=request.POST["skzhorario"]
    cita=request.POST["skzcita"]
    consultorio=Consultorio.objects.get(id_consult=id_consult)
    consultorio.nombre=nombre
    consultorio.telefono=telefono
    consultorio.doctor=doctor
    consultorio.especialidad=especialidad
    consultorio.horario=horario
    consultorio.cita=cita
    consultorio.save()
    redirect('/')
    

def borrarConsultorio(request,id_consult):
    consultorio=Consultorio.objects.get(id_consult=id_consult)
    consultorio.delete()
    
    return redirect('/')

