from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
def nombreCompleto(nombre,apellido):
        cadena="{0} , {1}"
        return cadena.format(nombre,apellido)

def urlimg(self,filename):
    ruta="static/img/tratamientos/%s/%s"%(self.nombre,str(filename))
    return ruta
#ENTIDAD  ESPECIALISTA
def vcedula(texto):
    # sin ceros a la izquierda
    nocero = texto.strip("0")
    
    cedula = int(nocero,0)
    verificador = cedula%10
    numero = cedula//10
    
    # mientras tenga números
    suma = 0
    while (numero > 0):
        
        # posición impar
        posimpar = numero%10
        numero   = numero//10
        posimpar = 2*posimpar
        if (posimpar  > 9):
            posimpar = posimpar-9
        
        # posición par
        pospar = numero%10
        numero = numero//10
        
        suma = suma + posimpar + pospar
    
    decenasup = suma//10 + 1
    calculado = decenasup*10 - suma
    if (calculado  >= 10):
        calculado = calculado - 10

    if (calculado == verificador):
        validado = 1
    else:
        validado = 0
        
    return (validado)
#ENTIDAD ESPECIALISTA -PERSONAL
class Especialista(AbstractUser):
    cedula=models.CharField(
        max_length=10,
        blank=False,
        primary_key=True,
        verbose_name='Cédula de ciudadanía')
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
    def clean(self):
        if vcedula(self.cedula==0):
            raise ValidationError('Cedula de identidad no válida')
'''
class Cita(models.Model):
    Fecha=models.DateTimeField(verbose_name='Fecha asignada de cita',blank=False,primary_key=True)

'''