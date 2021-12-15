from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import *
'''
class EspecialistaAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','cedula','correo')
    search_fields=('nombre','apellido','cedula')
admin.site.register(Especialista,EspecialistaAdmin)
'''
class EspecialistaAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'cedula'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('cedula',)
        })
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('cedula',)
        })
    )
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
admin.site.site_header = 'ADMINISTRACION DHARANA'