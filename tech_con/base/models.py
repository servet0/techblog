from django.db import models
from ckeditor.fields import RichTextField

class Logo(models.Model):
    tittle = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='logo', null=True, blank=True)
    minilogo = models.ImageField(upload_to='minilogo', null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)

class Header(models.Model):
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    view = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self): 
        return self.name
    
class Header2(models.Model):
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self): 
        return self.name
    

# Create your models here.
