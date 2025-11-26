from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutoriales
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

def index(request):
    return render(request=request,
                  template_name="blog/home.html",
                  context={"tutorials": Tutoriales.objects.all})

def register(request):
   if request.method == "POST":
       form=NewUserForm(request.POST)
       if form.is_valid():
           user = form.save()
           username= form.cleaned_data.get('username')
           messages.success(request, f"New account created: {username}")
           login(request, user)
           messages.info(request, f"You are now logged is a: {username}")
           return redirect('blog:index')
       else:
           for msg in form.error_messages:
               messages.error(request, f"{msg}:{form.error_messages}")
   
   form = NewUserForm()
     
   return render (request,
                   "blog/register.html",
                   context={"form": form})
   
def logout_view(request):
    logout(request)
    messages.info(request, "You are logged out succesfully!")
    return redirect('blog:index')

def login_view(request):
    if request.method== "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Account created with success!, Pseudo:{username}")
                return redirect('blog:index')
            else:
                messages.error(request, "Invalid username or password")
        else:
                messages.error(request, "Invalid username or password")
            
            
    form = AuthenticationForm
    return render(request,
                  "blog/login.html",
                  {"form": form})