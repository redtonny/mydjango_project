from django.contrib import admin
from .models import Tutoriales, TutorialCategory, TutorialSeries
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialesAdmin(admin.ModelAdmin):
    fieldsets=[("Title/Date", {"fields":["tutoriales_title","tutoriales_published"]}),
               ("URL",{"fields":["tutoriales_slug"]}),
               ("Series",{"fields":["tutorial_series"]}),
                ("Content",{"fields":["tutoriales_content"]})]
    
    formfield_overrides={
        models.TextField:{'widget': TinyMCE()}
    }
    
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)

admin.site.register(Tutoriales,TutorialesAdmin)