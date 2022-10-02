from django.urls import path
from .views import Registro
from usuario import views as usuario_views

urlpatterns = [
    path('registro/', Registro.as_view(), name="registro"),
    path('login', usuario_views.login,  name="login"),
    path('salir', usuario_views.salir, name="salir"),
    path('guardarAvatar/<str:nombre>', usuario_views.guardarAvatar, name="guardarAvatar" )
]
