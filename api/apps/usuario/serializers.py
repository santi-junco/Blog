from dataclasses import field
from rest_framework import serializers
from .excepciones import *
from .models import *
from apps.articulo.models import *

class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%d/%m/%Y")
    class Meta:
        model = Usuario
        fields = [
            'id',
            'first_name',
            'last_name',
            'date_joined',
            'email',
            'userName'
            ]

class UsuarioVerSerializer(UsuarioSerializer):
    articulos = serializers.SerializerMethodField('get_articulos')
    class Meta:
        model = Usuario
        fields = [
            'id',
            'first_name',
            'last_name',
            'date_joined',
            'email',
            'userName',
            'articulos'
            ]

    def get_articulos(self, instance):

        try:
            articulos = Articulo.objects.filter(usuario=instance.id).values('id','titulo','descripcion','categoria')
        except Exception as e:
            raise Error(str(e))
        
        return articulos