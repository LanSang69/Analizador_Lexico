from django.urls import path
from . import views

urlpatterns = [
    path('crear_basico/', views.crear_basico, name='crear_basico'),
    path('set_empty/', views.set_empty, name='set_empty'),
    path('get_session_data/', views.get_session_data, name='get_session_data'),
    path('concatenar/', views.concatenate_afns, name='concatenate_afns'),
    path('cerradura_p/', views.cerradura_p, name='cerradura_p'),
    path('cerradura_k/', views.cerradura_k, name='cerradura_k'),
    path('opcional/', views.opcional, name='opcional'),
    path('unir/', views.unir_automatas, name='unir_automatas'),
    path('generar/', views.generar_afn, name='generar_afn'),
    path('regex_to_afn/', views.RegexToAFN, name='RegexToAFN'),
    path('afn_to_afd/', views.createAFD, name='createAFD'),
    path('analizar/', views.analizar, name='analizar'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('eliminate/', views.eliminate, name='eliminate'),
]