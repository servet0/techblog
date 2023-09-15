from django.shortcuts import render
from .models import Logo, Header, Header2, MainAdversiment, Blog

def home(request):
    logos = Logo.objects.all()
    headers = Header.objects.all().order_by('-date')
    header2s = Header2.objects.all().order_by('-date')
    adses = MainAdversiment.objects.all().order_by('-date')
    blogs = Blog.objects.all().order_by('-date')

    context = {'logos':logos, 'headers':headers, 'header2s':header2s, 'adses':adses, 'blogs':blogs}

    return render(request, 'base/home.html', context)

def header_detail(request, header_name):
    logos = Logo.objects.all()
    header_d = Header.objects.get( name=header_name)
    
    context = {'header_d':header_d, 'logos':logos}

    return render(request, 'base/single.html', context)

def header_detail2(request, pk):
    logos = Logo.objects.all()
    header_d2 = Header2.objects.get( name=pk)

    context = {'header_d2':header_d2, 'logos':logos}

    return render(request, 'base/single2.html', context)

def blog_detail(request, blog_name):
    logos = Logo.objects.all()
    blog_d = Blog.objects.get( name=blog_name)
    
    context = {'blog_d':blog_d, 'logos':logos}

    return render(request, 'base/singleblog.html', context)


# Create your views here.
