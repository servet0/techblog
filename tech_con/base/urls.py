from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<str:header_name>', views.header_detail, name = 'single'),   
]