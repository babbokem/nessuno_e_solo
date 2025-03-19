from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manifesto/', views.manifesto, name='manifesto'),
    path('diario/', views.diario, name='diario'),
    path('contatto/', views.contatto, name='contatto'),
]
