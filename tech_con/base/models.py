from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

class Logo(models.Model):
    tittle = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='logo', null=True, blank=True)
    minilogo = models.ImageField(upload_to='minilogo', null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

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
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Footer(models.Model):
    tittle = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='logo', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    twitter = models.URLField(max_length=100, null=True, blank=True)
    instagram = models.URLField(max_length=100, null=True, blank=True)
    google = models.URLField(max_length=100, null=True, blank=True)
    pinterest = models.URLField(max_length=100, null=True, blank=True)
    youtube = models.URLField(max_length=100, null=True, blank=True)
    copyright_name = models.CharField(max_length=1000, null=True, blank=True)
    policy = RichTextField(null=True, blank=True)
    year = models.PositiveIntegerField(default=datetime.now().year)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

class Name(models.Model):
    tittle_main = models.TextField(null=True, blank=True)
    home = models.TextField(null=True, blank=True)
    contact = models.TextField(null=True, blank=True)
    news = models.TextField(null=True, blank=True)
    popular = models.TextField(null=True, blank=True)
    follow = models.TextField(null=True, blank=True)
    privacy = models.TextField(null=True, blank=True)
    alsolike = models.TextField(null=True, blank=True)
    page = models.TextField(null=True, blank=True)
    contactname = models.TextField(null=True, blank=True)
    contactemail = models.TextField(null=True, blank=True)
    contactphone = models.TextField(null=True, blank=True)
    contactsubject = models.TextField(null=True, blank=True)
    contactmessage = models.TextField(null=True, blank=True)
    contactsend = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=21)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class About(models.Model):
    about = RichTextField() 
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)




# Create your models here.
