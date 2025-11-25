from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutoriales
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
def index(request):
    return render(request=request,
                  template_name="blog/home.html",
                  context={"tutorials": Tutoriales.objects.all})

def register(request):
   if request.method == "POST":
       form=UserCreationForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('blog:index')
       else:
           print(form.errors)
    
   else:
        form = UserCreationForm()
     
   return render (request,
                   "blog/register.html",
                   context={"form": form})