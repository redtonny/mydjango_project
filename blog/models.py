from django.db import models
from datetime import datetime

class Tutoriales(models.Model):
    tutoriales_title= models.CharField(max_length=200)
    tutoriales_content= models.TextField()
    tutoriales_published= models.DateTimeField("Date published", default=datetime.now)
    
    def __str__(self):
        return self.tutoriales_title
