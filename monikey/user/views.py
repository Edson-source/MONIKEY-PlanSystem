from django.shortcuts import render, redirect
from django.urls import path, include
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from user.serializer import UserSerializer
from rest_framework import routers, serializers, viewsets
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
def register_user(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        form_usuario.fields['username'].widget.attrs['style'] = "background:#FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
        form_usuario.fields['password1'].widget.attrs['style'] = "background:#FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
        form_usuario.fields['password2'].widget.attrs['style'] = "background:#FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
        
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/planos/')
    else:
        form_usuario = UserCreationForm()
        form_usuario.fields['username'].widget.attrs['style'] = "background:#FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
        form_usuario.fields['password1'].widget.attrs['style'] = "background:#FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
        form_usuario.fields['password2'].widget.attrs['style'] = "background: #FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
        
    return render(request, 'register.html', {'form_usuario': form_usuario})

def login_user(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect(f'/{usuario.username}/admin/')
        else:
            form_login = AuthenticationForm()
            form_login.fields['username'].widget.attrs['style'] = "background:#FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
            form_login.fields['password'].widget.attrs['style'] = "background:#FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
    else:
        form_login = AuthenticationForm()
        form_login.fields['username'].widget.attrs['style'] = "background:#FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
        form_login.fields['password'].widget.attrs['style'] = "background:#FFFFFF; height: calc(3.5rem + 2px); padding: 1rem 0.75rem; display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: #6C7293; background-color: #FFFFFF; background-clip: padding-box; border: 1px solid #000; appearance: none; border-radius: 5px; transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;"
        
    return render(request, 'login.html', {'form_login': form_login})


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/login')
def change_password(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form_senha': form_senha})


def user_view(request, pk):
    user = {}
    user = User.objects.get(pk=pk)
    return render(request, 'user.html', {'user': user})

def profile_view(request, username):
    user = {}
    user = User.objects.get(username=username)
    return render(request, 'index.html', {'user': user})
