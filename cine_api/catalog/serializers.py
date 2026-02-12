from rest_framework import serializers
from .models import Marca, Cine

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ["id", "nombre"]

class CineSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.CharField(source="marca.nombre", read_only=True)

    class Meta:
        model = Cine
        fields = ["id", "marca", "marca_nombre", "modelo", "anio", "placa", "color", "creado_en"]