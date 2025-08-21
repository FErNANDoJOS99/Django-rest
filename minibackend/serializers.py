# serializers.py
from rest_framework import serializers
from minibackend.models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = "__all__"


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = "__all__"