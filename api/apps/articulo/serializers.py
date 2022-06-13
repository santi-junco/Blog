from rest_framework import serializers
from .models import *

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class ArticuloListSerializer(serializers.ModelSerializer):
    creado = serializers.DateField(format="%d/%m/%Y")
    userName_autor = serializers.CharField(source='usuario.userName')
    imagen = serializers.SerializerMethodField('get_imagen')
    autor_id = serializers.IntegerField(source='usuario.id')
    cant_comentarios = serializers.SerializerMethodField('get_comentario')
    cant_likes = serializers.SerializerMethodField('get_likes')
    class Meta:
        model = Articulo
        fields = [
            'id',
            'titulo',
            'descripcion',
            'categoria',
            'creado',
            'autor_id',
            'userName_autor',
            'cant_likes',
            'cant_comentarios',
            'imagen'
            ]

    def get_comentario(self, instance):
        coment = instance.cant_comentario(instance)
        return coment
    
    def get_likes(self, instance):
        likes = instance.cant_likes(instance)
        return likes
    
    def get_imagen(self, instance):
        imagen = Imagenes.objects.filter(articulo=instance).values_list('imagen',flat=True).first()
        if imagen:
            return imagen
        else:
            return None

class ArticuloVerSerializer(ArticuloListSerializer):
    imagenes = serializers.SerializerMethodField('get_imagenes')
    comentarios = serializers.SerializerMethodField('get_comentarios')
    class Meta:
        model = Articulo
        fields = [
            'id',
            'autor_id',
            'userName_autor',            
            'titulo',
            'descripcion',
            'categoria',
            'creado',
            'texto',
            'cant_likes',
            'cant_comentarios',
            'imagenes',
            'comentarios'
            ]

    def get_imagenes(self, instance):
        imagenes = Imagenes.objects.filter(articulo=instance).values_list('imagen',flat=True)
        return imagenes

    def get_comentarios(self, instance):
        comentarios = Comentario.objects.filter(articulo=instance).values('id','comentario', 'usuario__userName')
        return comentarios
class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
