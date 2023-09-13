from django.db import models

class Logo(models.Model):
    tittle = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='logo', null=True, blank=True)
    minilogo = models.ImageField(upload_to='minilogo', null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)




# Create your models here.
