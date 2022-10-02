from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Categoria(models.Model):
    nombre = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'categorias'
        verbose_name = 'categoria'
        ordering = ['nombre']

    def __str__(self) -> str:
        return self.nombre


class Nivel(models.Model):
    nombre = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'niveles'
        verbose_name = 'nivele'
        ordering = ['pk']

    def __str__(self) -> str:
        return self.nombre


class Pregunta(models.Model):
    pregunta = models.TextField()  # TextField nos permite escribir grandes textos
    categoria = models.ForeignKey(
        Categoria, null=False, blank=False, on_delete=models.RESTRICT)
    nivel = models.ForeignKey(
        Nivel, null=False, blank=False, on_delete=models.RESTRICT)
    imagen = models.URLField(null=True, blank=True,
                             verbose_name='Link de la imagen')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'preguntas'
        verbose_name = 'pregunta'
        ordering = ['pk']

    def __str__(self) -> str:
        return self.pregunta


class Opcion(models.Model):
    opcion = models.TextField()
    correcto = models.BooleanField(null=False, blank=False)
    pregunta = models.ForeignKey(
        Pregunta, null=False, blank=False, on_delete=models.RESTRICT)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'opciones'
        verbose_name = 'opcione'
        ordering = ['opcion']

    def __str__(self) -> str:
        return self.opcion


class Puntuacion(models.Model):
    usuario = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.RESTRICT)
    categoria = models.ForeignKey(
        Categoria, null=False, blank=False, on_delete=models.RESTRICT)
    nivel = models.ForeignKey(
        Nivel, null=False, blank=False, on_delete=models.RESTRICT)
    cantidad_preguntas = models.IntegerField(blank=True, null=True)
    cantidad_respuestas = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'puntuaciones'
    


