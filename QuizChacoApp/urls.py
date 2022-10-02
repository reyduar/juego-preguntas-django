from django import urls
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views


urlpatterns = [
    path('', core_views.inicio, name='inicio'),
    path('inicio/', core_views.inicio, name='inicio'),
    path('preguntaslista/', core_views.crearpregunta, name='preguntaslista'),
    path('acercade/', core_views.acercade, name='acercade'),
    path('ayuda/', core_views.ayuda, name='ayuda'),
    path('miscelanea/', core_views.miscelanea, name='miscelanea'),

    path('', include('juego.urls')),
    path('', include('usuario.urls')),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('core/img/favicon.ico')))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
