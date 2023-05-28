from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError 


def home(request):
    return render(request,'index.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })
    
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'],
                email =request.POST['mail'])
                user.save()

                login(request, user)
                return redirect('homepage')
            
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    'error': 'el usuario ya existe'
                })
                

        return render(request, 'signup.html',{
            'form': UserCreationForm,
            'error': 'las contrasenas no coinciden'
        })

def homepage(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], 
                            password = request.POST['password1'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'Usuario o contrasena incorrecta'
        })
        else:
            login(request, user)
            return redirect('homepage')


def signout(request):
    logout(request)
    return redirect('/')



