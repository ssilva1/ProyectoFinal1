from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from AppUser.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Create your views here.



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'inicio de sesion fallido!')
        else:
            messages.info(request, 'inicio de sesion fallido!')

        return redirect('AppLavatresInicio')

    contexto = {
        'form': AuthenticationForm(),
        'nombre_form': 'Login'
    }
    return render(request, 'AppUser/login.html', contexto)




def register(request):
    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.info(request,'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request,'Tu usuario no pudo ser registrado!')
        return redirect('AppLavatresInicio')

    contexto = {
        #'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'nombre_form': 'Registrarse'
    }

    return render(request, 'AppUser/login.html', contexto)


@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
        

            usuario.email = data.get('email')
            usuario.password = data.get('password')
            # usuario.password2 = data.get('password2')
            usuario.last_name = data.get('last_name')
            usuario.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
             messages.info(request, 'Tu usuario no pudo ser registrado!')
        return redirect('AppLavatresInicio')
    contexto = {
            'form': UserEditForm(
            initial={
                'username': usuario.username,
                'email': usuario.email,
                'password' : usuario.password,
                #'last_name': usuario.last_name
            }),
        'nombre_form': 'editar',
    }
    return render(request, 'AppUser/editarperfil.html', contexto)
    # usuario = request.user
    # contexto = {
    #         'form': UserRegisterForm(
    #         initial ={
    #         'username': usuario.username,
    #         'email': usuario.email,
    #         'last_name': usuario.last_name
    #         }),
    #     'nombre_form': 'editar'
    # }   

    




def upload_avatar(request):
    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=data.get("user"), imagen=data.get("imagen"))
                avatar.save()

        return redirect("AppLavatresInicio")

    contexto = {
        "form": AvatarForm(),
        'nombre_form': 'Crear'
    }
    return render(request, 'AppUser/login.html', contexto)



