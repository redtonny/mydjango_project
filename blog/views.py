from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutoriales, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


def single_slug( request, single_slug):
    categories= [ c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series= TutorialSeries.objects.filter(tutorial_category__category_slug= single_slug)
        
        series_url= {}
        for m in matching_series.all():
            part_one= Tutoriales.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutoriales_published")
            series_url[m]= part_one.tutoriales_slug
        return render(request,
                      "blog/category.html",
                      {"part_one": series_url})
    
    tutorial= [ t.tutoriales_slug for t in Tutoriales.objects.all()]
    if single_slug in tutorial:
        this_tutorial= Tutoriales.objects.get(tutoriales_slug= single_slug)
        tutorials_from_series= Tutoriales.objects.filter(tutorial_series__tutorial_series= this_tutorial.tutorial_series).order_by("tutoriales_published")
        
        this_tutorial_idx= list(tutorials_from_series).index(this_tutorial)
        return render(request,
                      "blog/tutorial.html",
                      {"tutorial": this_tutorial,
                       "sidebar": tutorials_from_series,
                       "this_tutorial_idx": this_tutorial_idx})

    return HttpResponse(f"{single_slug} does not correspond to anything.")

def index(request):
    return render(request=request,
                  template_name="blog/categories.html",
                  context={"categories": TutorialCategory.objects.all})

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