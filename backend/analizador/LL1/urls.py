from django.urls import path
from . import views

urlpatterns = [
    path('get_reglas/', views.getReglas, name='get_reglas'),
    path('get_lexico/', views.getLexico, name='get_lexico'),
    path('get_tabla/', views.getTablaAnalisis, name='getTablaAnalisis'),
]