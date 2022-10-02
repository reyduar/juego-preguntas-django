# Create your models here.
from django.db import models

class Integrante(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    perfil = models.TextField()
    avatar = models.URLField(null = True, blank = True, verbose_name = 'Link de la imagen')
    linkedin = models.URLField(null = True, blank = True, verbose_name = 'Link de Linkedin')
    created = models.DateTimeField(auto_now_add = True, verbose_name= 'Fecha de Creación')
    updated = models.DateTimeField(auto_now = True, verbose_name= 'Fecha de Edición')
    
    class Meta:
        db_table = 'integrantes'
        verbose_name = 'integrante'
        ordering = ['created']

    def __str__(self) -> str:
        return self.nombre

class Miscelanea(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.URLField(null = True, blank = True, verbose_name = 'Link de la imagen')
    informe = models.TextField()
    link_informe = models.URLField(verbose_name = 'Link del informe')
    created = models.DateTimeField(auto_now_add = True, verbose_name= 'Fecha de Creación')
    updated = models.DateTimeField(auto_now = True, verbose_name= 'Fecha de Edición')
    
    class Meta:
        db_table = 'titulos'
        verbose_name = 'titulo'
        ordering = ['created']

    def __str__(self) -> str:
        return self.titulo
