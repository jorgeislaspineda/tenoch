from django.urls import path
from . import views

urlpatterns = [
    path('jornadas/', views.listar_jornadas, name='listar_jornadas'),
    path('jornadas/<int:jornada_id>/', views.ver_partidos_jornada, name='ver_partidos_jornada'),
    path('partidos/<int:partido_id>/prediccion/', views.realizar_prediccion, name='realizar_prediccion'),
    path('jornadas/<int:jornada_id>/ganadores/', views.ver_ganadores_jornada, name='ver_ganadores_jornada'),
]