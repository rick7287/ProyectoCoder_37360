from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def curso(self):

    curso = Curso(nombre = 'Django', comision = 939393)
    curso.save()
    texto = f"Curso creado: {curso.nombre} {curso.comision}"

    return HttpResponse(texto)
