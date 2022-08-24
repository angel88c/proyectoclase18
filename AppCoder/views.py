from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.
def curso(request):
    curso = Curso(nombre="Python", comision=31105)
    curso2 = Curso(nombre="Fisica", comision=31105)
    curso3 = Curso(nombre="Calculo", comision=31105)
    curso.save()
    curso2.save()
    curso3.save()
    texto = f'Curso {curso.nombre} creado, comision: {curso.comision}'

    return HttpResponse(texto)

def inicio(request):
    return render(request, 'AppCoder/index.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')