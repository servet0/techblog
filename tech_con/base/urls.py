from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<str:header_name>/<int:header_id>', views.header_detail, name = 'single'),
]