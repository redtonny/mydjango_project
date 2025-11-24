from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutoriales
def index(request):
    return render(request=request,
                  template_name="blog/home.html",
                  context={"tutorials": Tutoriales.objects.all})