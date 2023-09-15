from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<str:header_name>', views.header_detail, name = 'single'),   
    path('haber/<str:pk>', views.header_detail2, name = 'single2'),   
    path('blog/<str:blog_name>', views.blog_detail, name = 'singleblog'),   
]