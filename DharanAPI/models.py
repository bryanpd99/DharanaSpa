from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import DateField
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from DharanAPI.ValidarCi import vcedula
from DharanAPI.ValidarFecha import ValidarFecha
from DharanAPI.ValidarHora import horasAtencion
from django.utils.html import format_html


from DharanAPI.ValidarHora import ValidarHora
def nombreCompleto(nombre,apellido,cedula):
        cadena="{0},{1}  ({2})"
        return cadena.format(nombre,apellido,cedula)

def urlimg(self,filename):
    ruta="static/img/tratamientos/%s/%s"%(self.nombre,str(filename))
    return ruta
#ENTIDAD  ESPECIALISTA

#ENTIDAD ESPECIALISTA -PERSONAL
class Especialista(AbstractUser):
    class Meta:
        verbose_name='Especialista'
    cedula=models.CharField(
        max_length=10,
        blank=False,
        primary_key=True,
        verbose_name='Cédula de ciudadanía')
    titulo=models.CharField(
        max_length=50,
        blank=False,
        verbose_name='Título o especialidad'
    )
    def clean(self):
        if (vcedula(self.cedula)==0):
            raise ValidationError('Cedula de identidad no válida')
    def __str__(self):
        return "{0} {1} ,{2}".format(self.first_name,self.last_name,self.titulo)
#ENTIDAD TRATAMIENTO
class Tratamiento(models.Model):
    def Imagen(self):
        return mark_safe('<a href="/%s"><img src="/%s" width=150px /> </a>'%(self.foto,self.foto))
    nombre= models.CharField(
        max_length=45,
        blank=False,
        verbose_name='Nombre del tratamiento'
        )
    descripcion=models.CharField(
        max_length=300,
        blank=False,
        verbose_name='Descripción del tratamiento'
        )
    precio=models.DecimalField(
        blank=False,
        verbose_name='Precio(USD)',
        decimal_places=2,
        max_digits=4,
        )
    def __str__(self):
        return self.nombre
    foto=models.ImageField(
        verbose_name='Foto referencial',
        upload_to=urlimg,
        default='static/img/tratamientos/default.jpg')
#ENTIDAD PACIENTE
class Paciente(models.Model):
    cedula=models.CharField(
        max_length=10,
        blank=False,
        primary_key=True,
        verbose_name='Cédula de ciudadanía'
        )
    nombre= models.CharField(
        max_length=45,
        blank=False,
        verbose_name='Nombres completos'
        )
    apellido=models.CharField(
        max_length=45,
        blank=False,
        verbose_name='Apellidos Completos'
        )
    sexos=(
        ('m', 'masculino'),
        ('f','femenino'),
        ('n/d','no definido')
        )
    sexo=models.CharField(
        max_length=10,
        choices=sexos,
        default='n/d'
        )
    edad=models.IntegerField(
        blank=False,
        verbose_name='Edad(Años)',
    validators=[MaxValueValidator(125), MinValueValidator(1)])
    telefono=models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Teléfono móvil')
    def __str__(self): 
        return nombreCompleto(self.nombre,self.apellido,self.cedula) 
    def clean(self):
        if (vcedula(self.cedula)==0):
            raise ValidationError('Cedula de identidad no válida')

class Cita(models.Model):
    class Meta:
        '''error_messages={
            'especialista':{
                'unique':'El especialista tiene turno'
            },
            'fecha':{
                'unique':'La fecha  está reservada'
            },
            'hora':{
                'unique':'La hora ya está tomada'
            },
        }'''
        unique_together=('especialista','fecha','hora')
        ordering=('fecha','hora',)
    cedula=models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        verbose_name='Cliente',
        )
    especialista=models.ForeignKey(
        Especialista,
        on_delete=models.CASCADE,
        verbose_name='Especialista encargado',
    )
    tratamiento=models.ForeignKey(
        Tratamiento,
        on_delete=models.CASCADE,
        verbose_name='Tratamiento a realizar'
    )
    fecha=models.DateField(
        verbose_name='Fecha asignada de cita',
        blank=False,
        )
    
    hora=models.TimeField(
        verbose_name='Hora de la cita',
        blank=False,
        choices=horasAtencion
    )
    observacion=models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Observacion de la cita',
        default='Ninguna'
        )
    estados_cita=(
        ('p', 'pendiente'),
        ('c','cancelada'),
        ('r','realizada')
        )
    estado=models.CharField(
        max_length=15,
        verbose_name='Estado de la cita',
        choices=estados_cita,
        default='p'
        
    )
    def Estado_de_Cita(self):
        tag='Pendiente'
        c='ffd700'
        if self.estado=='r':
            c='008f39'
            tag='Realizada'
        if self.estado=='c':
            c='fe0000'
            tag='Cancelada'
        return format_html(
            '<span style="color:#{};">{}</span>',
            c,
            tag,
        )
    def __str__(self):
        return "{0} , con cita para  el : {1}".format(self.cedula,self.fecha)
    def clean(self):
        if(not ValidarFecha(self.fecha)):
            raise ValidationError('Fecha no disponible')



