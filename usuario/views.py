from usuario.models import Avatar
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django import forms
from .forms import UserCreationFormWithEmail
from django.contrib.auth.models import User


def login(request):
    dic = request.GET.copy()
    registro = False
    if dic:
        if 'registro' in dic:
            registro = dic['registro']
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            avatar = request.GET.get('av', None)
            if avatar is not None:
                avatar = Avatar(nombre=avatar, usuario=user)
                avatar.save()
            elif not Avatar.objects.filter(usuario_id=user.id).exists():
                avatar = Avatar(nombre="monster_1", usuario=user)
                avatar.save()

            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "usuario/login.html", {'form': form, 'registro': registro})


def salir(request):
    do_logout(request)
    return redirect('/login')


class Registro(CreateView):
    avatar_ids = list(range(1, 7))
    avartar_prefix = "monster_"
    avartar_sufix = "svg"
    import random
    avatar_al_azar = random.choice(avatar_ids)
    nombre_del_avatar = f"{avartar_prefix}{avatar_al_azar}"
    avatar = f"{avartar_prefix}{avatar_al_azar}.{avartar_sufix}"

    form_class = UserCreationFormWithEmail

    template_name = 'usuario/registro.html'

    def get_context_data(self, **kwargs):
        ctx = super(Registro, self).get_context_data(**kwargs)
        ctx['avatar'] = self.avatar
        return ctx

    def get_success_url(self):
        return reverse_lazy('login')+'?registro=True&av='+self.nombre_del_avatar

    def get_form(self, form_class=None):
        form = super(Registro, self).get_form()
        # Modificamos en tiempo real
        form.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'El nombre es opcional'})
        form.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'El apellido es opcional'})
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Su usuario es requerido y debe contener 150 carácteres como máximo. Únicamente letras, dígitos y @/./+/-/_'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'El email es requerido y debe contener 254 carácteres como máximo y debe ser válido'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Su contraseña es requerida y debe contener al menos 8 caracteres'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Para verificar, introduzca la misma contraseña anterior'})
        return form


def guardarAvatar(request, nombre):
    usuario = request.user
    avatar = Avatar(nombre=nombre, usuario=usuario)
    avatar.save()

    return redirect("inicio")
