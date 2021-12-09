from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator
def nombreCompleto(nombre,apellido):
        cadena="{0} , {1}"
        return cadena.format(nombre,apellido)

def urlimg(self,filename):
    ruta="static/img/tratamientos/%s/%s"%(self.nombre,str(filename))
    return ruta
#ENTIDAD  ESPECIALISTA
class Especialista (models.Model):
    cedula=models.CharField(
        max_length=10,
        blank=False,
        primary_key=True,
        verbose_name='Cédula de ciudadanía')
    nombre= models.CharField(
        max_length=45,
        blank=False,
        verbose_name='Nombres completos'
        )
    apellido=models.CharField(
        max_length=45,
        blank=True,
        verbose_name='Apellidos Completos'
        )
    correo=models.EmailField(
        blank=False,
        verbose_name='Correo electrónico'
        )
    def __str__(self): 
        return nombreCompleto(self.nombre,self.apellido) 
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
        return nombreCompleto(self.nombre,self.apellido) 

