from django.urls import path
from .views import *


urlpatterns = [
    
    path('curso/', curso),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('', inicio),
    
]