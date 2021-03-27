from django.db import models
import uuid
# Create your models here.

class Franquicia(models.Model):
    id = models.BigAutoField(primary_key=True,null=False)
    nombre = models.CharField(verbose_name='Franquicia',null=False,max_length=20)
    expression = models.CharField('Expresion',null=False, max_length=100, default='')

    def __str__(self):
        return self.nombre

    
class Usuario(models.Model):
    id = models.BigAutoField(null=False,primary_key=True)
    nombre = models.CharField(null=False,verbose_name='Nombre',max_length=30)
    apellidos = models.CharField(null=False, max_length=70)
    correo = models.CharField(null=False, verbose_name='Correo',max_length=80)
    vericado = models.BooleanField(null=False,default=False,verbose_name='Verificado')
    token_verificacion = models.CharField(default=uuid.uuid4,auto_created=True,max_length=100,null=True)
    uuid = models.UUIDField(default=uuid.uuid4,auto_created=True)
    fecha_creacion = models.DateTimeField('Fecha Creación',null=False,auto_now=True,auto_created=True)


class Tarjeta(models.Model):
    id = models.BigAutoField(null=False,primary_key=True),
    uuid = models.UUIDField(verbose_name='UUID',blank=False,default = uuid.uuid4,auto_created=True)
    franquiciaid = models.ForeignKey(to=Franquicia,to_field='id',on_delete=models.RESTRICT)
    token = models.CharField(verbose_name='Token',max_length=200,default=None)
    token_fecha_creacion = models.DateTimeField(null=False,auto_now=True,auto_created=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_vencimiento = models.DateField(blank=False)
    usuarioid = models.ForeignKey(Usuario,to_field='id',on_delete=models.RESTRICT,null=True,default=None)


    def __str__(self):
         return self.uuid.hex
