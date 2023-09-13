from django.shortcuts import render
from .models import Logo

def home(request):
    logos = Logo.objects.all()

    context = {'logos':logos}

    return render(request, 'base/home.html', context)

# Create your views here.
