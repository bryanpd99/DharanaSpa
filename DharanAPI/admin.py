from django.contrib import admin
from . models import *
class EspecialistaAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','cedula','correo')
    search_fields=('nombre','apellido','cedula')
admin.site.register(Especialista,EspecialistaAdmin)

class PacienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','cedula','sexo','edad','telefono')
    search_fields=('nombre','apellido','cedula','telefono')
admin.site.register(Paciente,PacienteAdmin)


class TratamientoAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','precio','Imagen')
    search_fields=('nombre','apellido','cedula')
admin.site.register(Tratamiento,TratamientoAdmin)

# Register your models here.
