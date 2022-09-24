
import imp
from re import template
from django.urls import path
from AppUser.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login_request, name='AppUserLogin'),
    path('registro/', register, name='AppUserRegister'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='AppUserLogOut'),
    path('editar/', editar_usuario, name='AppUserEditar'),
    path('avatar/', upload_avatar, name='AppUserAvatar')
    ]