from rest_framework import serializers
from .models import *

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class ArticuloListSerializer(serializers.ModelSerializer):
    creado = serializers.DateField(format="%d/%m/%Y")
    autor = serializers.SerializerMethodField('get_autor')
    imagen = serializers.SerializerMethodField('get_imagen')
    class Meta:
        model = Articulo
        fields = ['id','titulo','descripcion','categoria','creado','autor','imagen']

    def get_autor(self, instance):
        autor = Usuario.objects.get(id=instance.usuario.id).userName
        return autor
    
    def get_imagen(self, instance):
        imagen = Imagenes.objects.filter(articulo=instance).values_list('imagen',flat=True).first()
        if imagen:
            return imagen
        else:
            return ''

class ArticuloVerSerializer(ArticuloListSerializer):
    imagenes = serializers.SerializerMethodField('get_imagenes')
    comentarios = serializers.SerializerMethodField('get_comentarios')
    class Meta:
        model = Articulo
        fields = ['id','titulo','descripcion','categoria','creado','autor','texto','imagenes','comentarios']

    def get_imagenes(self, instance):
        imagenes = Imagenes.objects.filter(articulo=instance).values_list('imagen',flat=True)
        return imagenes

    def get_comentarios(self, instance):
        comentarios = Comentario.objects.filter(articulo=instance).values('comentario', 'usuario__userName')
        return comentarios
class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
