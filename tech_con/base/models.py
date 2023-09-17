from django.db import models
from ckeditor.fields import RichTextField

class Logo(models.Model):
    tittle = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='logo', null=True, blank=True)
    minilogo = models.ImageField(upload_to='minilogo', null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)

class Header(models.Model):
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    adversiment1 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver1 = models.URLField(null=True, blank=True)
    adversiment2 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver2 = models.URLField(null=True, blank=True)
    adversiment3 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver3 = models.URLField(null=True, blank=True)
    adversiment4 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver4 = models.URLField(null=True, blank=True)
    view = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self): 
        return self.name
    
class Header2(models.Model):
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    adversiment1 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver1 = models.URLField(null=True, blank=True)
    adversiment2 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver2 = models.URLField(null=True, blank=True)
    adversiment3 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver3 = models.URLField(null=True, blank=True)
    adversiment4 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver4 = models.URLField(null=True, blank=True)
    view = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self): 
        return self.name
    
class MainAdversiment(models.Model):
    name = models.TextField(null=True, blank=True)
    adsnavbar = models.ImageField(upload_to='ads', null=True, blank=True)
    urlnavbar = models.URLField(null=True, blank=True)
    adsheader = models.ImageField(upload_to='ads', null=True, blank=True)
    urlheader = models.URLField(null=True, blank=True)
    ads = models.ImageField(upload_to='ads', null=True, blank=True)
    urlads = models.URLField(null=True, blank=True)
    ads2 = models.ImageField(upload_to='ads', null=True, blank=True)
    urlads2 = models.URLField(null=True, blank=True)
    ads3 = models.ImageField(upload_to='ads', null=True, blank=True)
    urlads3 = models.URLField(null=True, blank=True)
    ads4 = models.ImageField(upload_to='ads', null=True, blank=True)
    urlads4 = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    def __str__(self): 
        return self.name
    
class Blog(models.Model):
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    adversimenthome = models.ImageField(upload_to='ads', null=True, blank=True)
    urladverhome = models.URLField(null=True, blank=True)
    adversiment1 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver1 = models.URLField(null=True, blank=True)
    adversiment2 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver2 = models.URLField(null=True, blank=True)
    adversiment3 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver3 = models.URLField(null=True, blank=True)
    adversiment4 = models.ImageField(upload_to='ads', null=True, blank=True)
    urladver4 = models.URLField(null=True, blank=True)
    view = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self): 
        return self.name
    
class AllSingleAdversiment(models.Model):
    name = models.TextField(null=True, blank=True)    
    ads1 = models.ImageField(upload_to='ads', null=True, blank=True)
    urlads1 = models.URLField(null=True, blank=True)
    ads2 = models.ImageField(upload_to='ads', null=True, blank=True)
    urlads2 = models.URLField(null=True, blank=True)
    ads3 = models.ImageField(upload_to='ads', null=True, blank=True)
    urlads3 = models.URLField(null=True, blank=True)
    ads4 = models.ImageField(upload_to='ads', null=True, blank=True)
    urlads4 = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self): 
        return self.name

class Suggestion(models.Model):
    title = models.CharField(max_length=100, null=True)
    suggest = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

# Create your models here.
