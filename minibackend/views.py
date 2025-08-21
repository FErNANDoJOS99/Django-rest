from django.shortcuts import render

# views.py
from rest_framework import viewsets
from minibackend.models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
