from django.contrib import admin
from .models import Integrante, Miscelanea

class IntegranteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Integrante, IntegranteAdmin)

class MiscelaneaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Miscelanea, MiscelaneaAdmin)
