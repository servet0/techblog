from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('gundem/<str:header_name>', views.header_detail, name = 'single'),   
    path('_gundem/<str:pk>', views.header_detail2, name = 'single2'),   
    path('yeni/<str:blog_name>/', views.blog_detail, name = 'singleblog'),   
    path('privacy-policy/', views.privacy, name = 'policy'),   
    path('contact/', views.contact, name = 'contact'),      
]