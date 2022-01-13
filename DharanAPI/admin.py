from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.checks import messages
from . models import *
from django.contrib import messages

class EspecialistaAdmin(UserAdmin):
    list_display = (
        'cedula','first_name','last_name','titulo', 'username','email',   'is_staff',
        
        )
    search_fields=('cedula','first_name','last_name')

    fieldsets = (
        ('Información  personal del Especialista', {
            'fields': ('first_name', 'last_name', 'email','titulo')
        }),
        ('Permisos del usuario', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups'
                )
        }),
        ('Usuario de la aplicación', {
            'fields': ('username', 'password')
        }),
    )
    add_fieldsets = (
                ('Información  personal del Especialista', {
            'fields': ('cedula','first_name', 'last_name','titulo', 'email')
        }),
                ('Permisos del usuario', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups'
                )
        }),
        ('Datos de registro en la aplicación', {
            'fields': ('username', 'password1', 'password2')
        }),
    )
admin.site.register(Especialista,EspecialistaAdmin)

class PacienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','cedula','sexo','edad','telefono')
    list_filter=('sexo',)
    search_fields=('nombre','apellido','cedula','telefono')
admin.site.register(Paciente,PacienteAdmin)


class TratamientoAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','precio','Imagen')
    search_fields=('nombre','precio')
admin.site.register(Tratamiento,TratamientoAdmin)


class CitaAdmin(admin.ModelAdmin):

    '''def save_model(self, request, obj, form, change):
        messages.add_message(request,messages.INFO,'Cita agregada con éxito')
        super(CitaAdmin,self).save_model(request, obj, form, change)'''
    model=Cita
    list_filter = ('cedula','especialista','estado','fecha', 'hora')
    search_fields=['cedula__cedula','cedula__nombre','cedula__apellido','especialista__first_name','especialista__last_name','especialista__cedula']
    fieldsets=(
        (None, {
            'fields': ('cedula','tratamiento','fecha','hora','especialista','observacion')
        }),
            
        )
    list_display=('cedula','Estado_de_Cita','tratamiento','fecha','hora','especialista','observacion',)
    date_hierarchy=('fecha')
    actions=['set_done','set_cancelled']
    @admin.action(description='Marcar como citas Realizadas')
    def set_done(self,request,queryset):
        queryset.update(estado='r')
    @admin.action(description='Marcar como citas Canceladas')
    def set_cancelled(self,request,queryset):
        queryset.update(estado='c')
    #DEFINIR LISTAR LOS CAMPOS DE ACUERDO AL USUARIO
    def changelist_view(self, request, extra_context=None):
        if not request.user.is_superuser:
            self.list_filter=('cedula','estado','fecha', 'hora')
        else:
            self.list_filter = ('cedula','especialista','estado','fecha', 'hora')
        return super(CitaAdmin, self).changelist_view(request, extra_context)
        #return Cita.objects.all()
    def get_queryset(self, request):
        if not request.user.is_superuser:
            return Cita.objects.filter(especialista__cedula=request.user.cedula)
        else:
            return super(CitaAdmin, self).get_queryset(request)


admin.site.register(Cita,CitaAdmin)

# Register your models here.
admin.site.site_header = 'ADMINISTRACION DHARANA'