from django.shortcuts import render
from .models import Logo, Header, Header2, MainAdversiment, Blog, AllSingleAdversiment, Suggestion
from django.core.paginator import Paginator

def home(request):
    logos = Logo.objects.all()
    headers = Header.objects.all().order_by('-date')
    header2s = Header2.objects.all().order_by('-date')
    adses = MainAdversiment.objects.all().order_by('-date')
    blogs = Blog.objects.all().order_by('-date')
    suggests = Suggestion.objects.all().order_by('date')

    paginator = Paginator(blogs, 12) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'logos':logos, 'headers':headers, 'header2s':header2s, 'adses':adses, 'blogs':blogs, 'page_obj':page_obj, 'suggests':suggests}

    return render(request, 'base/home.html', context)

def header_detail(request, header_name):
    logos = Logo.objects.all()
    allsingles = AllSingleAdversiment.objects.all().order_by('-date')
    header_d = Header.objects.get( name=header_name)
    suggests = Suggestion.objects.all().order_by('date')
    alsolikes = Blog.objects.all().order_by('-date')[0:6]
    
       

    context = {'header_d':header_d, 'logos':logos, 'allsingles':allsingles, 'suggests':suggests, 'alsolikes':alsolikes}

    return render(request, 'base/single.html', context)

def header_detail2(request, pk):
    logos = Logo.objects.all()
    allsingles = AllSingleAdversiment.objects.all().order_by('-date')
    header_d2 = Header2.objects.get( name=pk)
    suggests = Suggestion.objects.all().order_by('date')
    alsolikes = Blog.objects.all().order_by('-date')[0:6]

    context = {'header_d2':header_d2, 'logos':logos, 'allsingles':allsingles, 'suggests':suggests, 'alsolikes':alsolikes}

    return render(request, 'base/single2.html', context)

def blog_detail(request, blog_name):
    logos = Logo.objects.all()
    allsingles = AllSingleAdversiment.objects.all().order_by('-date')
    blog_d = Blog.objects.get( name=blog_name)
    suggests = Suggestion.objects.all().order_by('date')
    alsolikes = Blog.objects.all().order_by('-date')[0:6]

    

    
    context = {'blog_d':blog_d, 'logos':logos, 'allsingles': allsingles, 'suggests':suggests, 'alsolikes':alsolikes}

    return render(request, 'base/singleblog.html', context)


# Create your views here.
