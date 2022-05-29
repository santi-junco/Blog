from rest_framework import serializers
from .models import *

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
