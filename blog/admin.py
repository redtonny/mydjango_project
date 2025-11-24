from django.contrib import admin
from .models import Tutoriales
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialesAdmin(admin.ModelAdmin):
    fieldsets=[("Title/Date", {"fields":["tutoriales_title","tutoriales_published"]}),
                ("Content",{"fields":["tutoriales_content"]})]
    
    formfield_overrides={
        models.TextField:{'widget': TinyMCE()}
    }
admin.site.register(Tutoriales,TutorialesAdmin)