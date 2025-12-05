from django.db import models
from datetime import datetime

class TutorialCategory(models.Model):
    tutorial_category= models.CharField(max_length=200)
    category_summary= models.CharField(max_length=200)
    category_slug= models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural= "Categories"
        
    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series= models.CharField(max_length=200)
    tutorial_category= models.ForeignKey(TutorialCategory, default=1, verbose_name="Categories", on_delete= models.CASCADE)
    series_summary= models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural="Series"
    
    def __str__(self):
        return self.tutorial_series

class Tutoriales(models.Model):
    tutoriales_title= models.CharField(max_length=200)
    tutoriales_content= models.TextField()
    tutoriales_published= models.DateTimeField("Date published", default=datetime.now)
    tutorial_series= models.ForeignKey(TutorialSeries,default=1, verbose_name="Series", on_delete= models.CASCADE)
    tutoriales_slug= models.CharField(max_length=200, default=1)
    
    def __str__(self):
        return self.tutoriales_title
