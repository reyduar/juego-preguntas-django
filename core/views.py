from usuario.models import Avatar
from django.shortcuts import render, redirect
from .models import Integrante, Miscelanea
from django.contrib.auth.decorators import login_required
from juego.models import Puntuacion, Nivel, Pregunta, Categoria
from .forms import FormPregunta
# Create your views here.


@login_required(login_url='/login')
def inicio(request):
    usuarioId = request.user.id
    if Avatar.objects.filter(usuario_id=usuarioId).exists():
        avatar = Avatar.objects.get(usuario_id=usuarioId)
        imagen = avatar.nombre
    else:
        imagen = "monster_7"

    puntuaciones = []
    copitas = []
    if Puntuacion.objects.filter(usuario_id=usuarioId).exists():
        puntuaciones = Puntuacion.objects.filter(usuario_id=usuarioId)
        for p in puntuaciones:
            copitas.append(
                {'nivel': p.nivel.nombre, 'categoria': p.categoria.nombre})

    categorias = Categoria.objects.order_by('pk')
    opCategorias = []

    for c in categorias:
        opCategorias.append(
            {'id': c.id, 'nombre': c.nombre, 'key': 'cat' + str(c.id)})
    return render(request, "core/inicio.html", {'categorias': opCategorias, 'puntuaciones': puntuaciones, 'copitas': copitas, 'avatar': imagen})


@login_required(login_url='/login')
def ayuda(request):
    return render(request, "core/ayuda.html")


@login_required(login_url='/login')
def miscelanea(request):
    titulos = Miscelanea.objects.all()
    return render(request, "core/miscelanea.html", {'titulos': titulos})


@login_required(login_url='/login')
def acercade(request):
    integrantes = Integrante.objects.all()
    return render(request, "core/acercade.html", {'integrantes': integrantes})


@login_required(login_url='/login')
def preguntaslista(request):
    formulario = FormPregunta()
    return render(request, "core/preguntaslista.html", {
        'form': formulario
    })


@login_required(login_url='/login')
def crearpregunta(request):
    if request.method == 'POST':
        formulario = FormPregunta(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            pregunta = data_form["pregunta"]
            categoriaId = data_form["categoriaId"]
            nivelId = data_form["nivelId"]
            imagen = data_form["imagen"]

            # El guadado de la pregunta
            c = Categoria.objects.get(pk=categoriaId)
            n = Nivel.objects.get(pk=nivelId)

            preguntaObject = Pregunta(
                categoria=c, nivel=n, pregunta=pregunta, imagen=imagen)
            preguntaObject.save()
        else:
            print("Error")
    else:
        formulario = FormPregunta()
    return render(request, "core/preguntaslista.html", {
        'form': formulario
    })
