from django.db import models

# Create your models here.
# auto(Seccion , Descripcion , imagen)
class autoGaleria(models.Model):
    Nombre=models.CharField(max_length=100,primary_key=True)
    Descripcion=models.CharField(max_length=100)
    Imagen=models.ImageField(upload_to='autosGaleria',null=True)
    
    def __str__(self):
        return self.Descripcion

class autoInicio(models.Model):
    Nombre=models.CharField(max_length=100,primary_key=True)
    Descripcion=models.CharField(max_length=100)
    Imagen=models.ImageField(upload_to='autosInicio',null=True)
    
    def __str__(self):
        return self.Descripcion
    
class MisionVision(models.Model):
    ident=models.CharField(max_length=40,primary_key=True)
    mision=models.TextField()
    vision=models.TextField()
    
    def __str__(self):
        return self.ident

class Insumos(models.Model):
    nombre = models.CharField(max_length=120,primary_key=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre