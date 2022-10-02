from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Categoria, Nivel, Opcion, Pregunta, Puntuacion
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


@login_required(login_url='/login')
def juego(request, categoriaId, nivelId, preguntaId=None):
    categoria = Categoria.objects.get(pk=categoriaId)
    nivel = Nivel.objects.get(pk=nivelId)
    if preguntaId:
        pregunta = Pregunta.objects.get(pk=preguntaId)
        opciones = Opcion.objects.raw(
            f"SELECT * FROM opciones WHERE pregunta_id='{preguntaId}'")
    else:
        pregunta = Pregunta.objects.order_by('id').filter(
            categoria_id=categoriaId, nivel_id=nivelId)[0]
        opciones = Opcion.objects.raw(
            f"SELECT * FROM opciones WHERE pregunta_id='{pregunta.id}'")
    return render(request, "juego/juego.html", {'pregunta': pregunta, 'categoria': categoria, 'opciones': opciones, 'nivel': nivel})


def categoria(request):
    preguntas = None
    categoriaId = request.GET.get('categoriaId', None)
    nivelId = request.GET.get('nivelId', None)
    if Pregunta.objects.filter(categoria_id=categoriaId, nivel_id=nivelId).exists():
        preguntas = list(Pregunta.objects.filter(
            categoria_id=categoriaId, nivel_id=nivelId).values())

    json_response = {'preguntas': preguntas}
    return JsonResponse(json_response)


def puntuaciones(request):
    usuarioId = request.user.id
    puntuaciones = None
    categoriaId = request.GET.get('categoriaId', None)

    if Puntuacion.objects.filter(usuario_id=usuarioId, categoria_id=categoriaId).exists():
        puntuaciones = list(Puntuacion.objects.filter(
            usuario_id=usuarioId, categoria_id=categoriaId).order_by('nivel_id').values())
    json_response = {'puntuaciones': puntuaciones}
    return JsonResponse(json_response)


def opcionCorrecta(request):
    opciones = None
    preguntaId = request.GET.get('preguntaId', None)
    if Opcion.objects.filter(pregunta_id=preguntaId).exists():
        opciones = Opcion.objects.filter(pregunta_id=preguntaId).values()

    json_response = {'opciones': list(opciones)}
    return JsonResponse(json_response)


def preguntas(request):
    preguntas = None
    categoriaId = request.GET.get('categoriaId', None)
    preguntaId = request.GET.get('preguntaId', None)
    nivelId = request.GET.get('nivelId', None)
    siguientesPreguntas = []
    if Pregunta.objects.filter(categoria_id=categoriaId, nivel_id=nivelId).exists():
        preguntas = list(Pregunta.objects.filter(
            categoria_id=categoriaId, nivel_id=nivelId).values())

    json_response = {'preguntas': preguntas}
    return JsonResponse(json_response)


def guardarPuntuacion(request):
    if request.method == 'POST':
        import json
        datosDeLaPuntuacion = json.loads(request.body.decode("utf-8"))
        usu = datosDeLaPuntuacion["usuarioId"]
        cat = datosDeLaPuntuacion["categoriaId"]
        niv = datosDeLaPuntuacion["nivelId"]
        totalPreguntas = datosDeLaPuntuacion["cantidadPreguntas"]
        totalRespondidas = datosDeLaPuntuacion["cantidadRespuestas"]
        usuario = User.objects.get(pk=usu)
        categoria = Categoria.objects.get(pk=cat)
        nivel = Nivel.objects.get(pk=niv)
        if Puntuacion.objects.filter(usuario_id=usuario.id, categoria_id = categoria.id, nivel_id = nivel.id).exists():
            puntos_a_editar = Puntuacion.objects.get(usuario_id=usuario.id, categoria_id = categoria.id, nivel_id = nivel.id)
            Puntuacion.objects.filter(id=puntos_a_editar.id).update(cantidad_respuestas=totalRespondidas)
        else:
            puntuacion = Puntuacion(usuario=usuario, categoria=categoria, nivel=nivel,
                                 cantidad_preguntas=totalPreguntas, cantidad_respuestas=totalRespondidas)
            puntuacion.save()
    return redirect('inicio')
