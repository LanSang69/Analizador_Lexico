from django.urls import path
from . import views

urlpatterns = [
    path('crear_basico/', views.crear_basico, name='crear_basico'),
]