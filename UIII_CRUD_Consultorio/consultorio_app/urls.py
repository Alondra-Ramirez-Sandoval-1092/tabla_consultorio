from django.urls import path
from consultorio_app import views
urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarConsultorio/",views.registrarConsultorio,name="registrarConsultorio"),
    path("seleccionarConsultorio/<codigo>",views.seleccionarConsultorio,name="seleccionarConsultorio"),
    path("editarConsultorio/",views.editarConsultorio,name="editarConsultorio"),
    path("borrarConsultorio/<codigo>",views.borrarConsultorio,name="borrarConsultorio")
]