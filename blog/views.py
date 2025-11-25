from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutoriales
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
def index(request):
    return render(request=request,
                  template_name="blog/home.html",
                  context={"tutorials": Tutoriales.objects.all})

def register(request):
   if request.method == "POST":
       form=UserCreationForm(request.POST)
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
   else:
        form = UserCreationForm()
     
   return render (request,
                   "blog/register.html",
                   context={"form": form})