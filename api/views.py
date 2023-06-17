from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from dashboard.models import *
from .serializers import *
# Create your views here.

class CuentaView(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

class KeyView(viewsets.ModelViewSet):
    queryset = KeyAlumno.objects.all()
    serializer_class = KeySerializer

class AlumnoView(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class InscripcionView(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
class CursoView(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer