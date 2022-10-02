from django.contrib import admin
from .models import Opcion, Pregunta
from .models import Categoria
from .models import Nivel
from .models import Opcion

# Register your models here.
class PreguntaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Pregunta, PreguntaAdmin)
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Categoria, CategoriaAdmin)

class NivelAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Nivel, NivelAdmin)

class OpcionAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Opcion, OpcionAdmin)
