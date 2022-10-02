from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Avatar(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    usuario = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.RESTRICT)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        db_table = 'avatares'