from django.db import models

class Logo(models.Model):
    tittle = models.CharField(max_length=100)
    image = models.ImageField(upload_to='logo')

# Create your models here.
