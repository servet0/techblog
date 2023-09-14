from django.shortcuts import render
from .models import Logo, Header, Header2

def home(request):
    logos = Logo.objects.all()
    headers = Header.objects.all().order_by('-date')
    header2s = Header2.objects.all().order_by('-date')

    context = {'logos':logos, 'headers':headers, 'header2s':header2s}

    return render(request, 'base/home.html', context)

def header_detail(request, header_id, header_name):
    logos = Logo.objects.all()
    header_d = Header.objects.get(id=header_id, name=header_name) 

    context = {'header_d':header_d, 'logos':logos}

    return render(request, 'base/single.html', context)

# Create your views here.
