"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home, name="Home"),
    path('crear/Insert/', views.Insert, name='Insert'),
    path('crear/', views.crear, name="crear"),
    path('Select/', views.Select, name="Select"),
    path('home/Delete/', views.Delete, name="Delete"),
    path('actualizar_evento/<int:evento_id>/', views.detalles, name='actualizar_evento'),
    path('update/', views.actualizar_evento, name='update'),    
]
