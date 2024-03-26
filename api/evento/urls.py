# Definir rutas url
from django.urls import path
# importa el modulo views
from . import views

#llamando las vistas en views.py
urlpatterns = [
    path('select/', views.select),  
    path('insert/', views.insert),
    path('delete/', views.delete),
    path('detalle/<int:evento_id>/',views.detalle_evento),
    path('update/',views.update),
    ]