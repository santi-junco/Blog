from rest_framework import generics, permissions
from .models import *
from .serializers import *

########################### Articulos ##############################
# Crear articulo
class ArticuloCreateApiView(generics.CreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.IsAuthenticated]

# Editar articulo
class ArticuloUpdateApiView(generics.UpdateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.IsAuthenticated]

# Eliminar articulo
class ArticuloDeleteApiView(generics.DestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.IsAuthenticated]

# Obtener un articulo
class ArticuloRetiveApiView(generics.RetrieveAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

# Listado de articulos
class ArticuloListApiView(generics.ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

#################### Comentario #####################
# Crear un comentario
class ComentarioCreateApiView(generics.CreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]

# Editar comentario
class ComentarioUpdateApiView(generics.UpdateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]

# Eliminar comentario
class ComentarioDeleteApiView(generics.DestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]