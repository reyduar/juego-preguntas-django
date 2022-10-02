from django.urls import path
from juego import views as juego_views

urlpatterns = [
    path('categoria/', juego_views.categoria, name='categoria'),
    path('preguntas/', juego_views.preguntas, name='preguntas'),
    path('puntuaciones/', juego_views.puntuaciones, name='puntuaciones'),
    path('opcionCorrecta/', juego_views.opcionCorrecta, name='opcionCorrecta'),
    path('puntuacion/', juego_views.guardarPuntuacion, name='puntuacion'),
    path('jugar/?P<int:categoriaId>/?P<int:nivelId>',
         juego_views.juego, name='juego'),
    path('juego/<int:categoriaId>/<int:nivelId>/<int:preguntaId>',
         juego_views.juego, name='juego'),
]
