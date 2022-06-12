from django.http import JsonResponse
import jwt
from rest_framework import generics, permissions
from apps.core.excepciones import Error
from apps.core.funciones import *
from .models import *
from .serializers import *
from blog.settings.base import SECRET_KEY

########################### Articulos ##############################
# Crear articulo
class ArticuloCreateApiView(generics.CreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        articulo = serializer.save()
        imagenes = int(self.request.data.get('imagenes', 0))
        if imagenes > 0:
            for imagen in range(1,imagenes+1):
                try:
                    Imagenes.objects.create(
                        articulo = articulo,
                        imagen = self.request.data.get(f'imagen{imagen}')
                    )
                except Exception as e:
                    raise Error(str(e))
        return super().perform_create(serializer)

# Editar articulo
class ArticuloUpdateApiView(generics.UpdateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user_id = user_token(request)

        try:
            articulo = Articulo.objects.get(id=self.kwargs['pk'])
        except Exception as e:
            raise Error(str(e))
        print(articulo.usuario.id)
        print('-'*50)

        if user_id == articulo.usuario.id:
            return super().update(request, *args, **kwargs)
        else:
            return JsonResponse({'mensaje':"No tiene permiso para editar el articulo"}, status=400)

# Eliminar articulo
class ArticuloDeleteApiView(generics.DestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):

        tokenJWT = request.headers['Authorization'].split()[1]
        tokenDecoded = jwt.decode(tokenJWT, SECRET_KEY, algorithms=["HS256"])
        user_token = tokenDecoded['user_id']
        
        try:
            articulo = Articulo.objects.get(id=self.kwargs['pk'])
        except Exception as e:
            raise Error(str(e))
        
        if articulo.usuario.id == user_token:
            articulo.delete()
        else:
            raise Error("No tiene permiso para eliminar el articulo")
        
        return JsonResponse({'mensaje':'Articulo eliminado'})

# Obtener un articulo
class ArticuloRetiveApiView(generics.RetrieveAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloVerSerializer

# Listado de articulos
class ArticuloListApiView(generics.ListAPIView):
    queryset = Articulo.objects.all().order_by('-creado')
    serializer_class = ArticuloListSerializer

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

    def delete(self, request, *args, **kwargs):

        tokenJWT = request.headers['Authorization'].split()[1]
        tokenDecoded = jwt.decode(tokenJWT, SECRET_KEY, algorithms=["HS256"])
        user_token = tokenDecoded['user_id']
        
        try:
            comentario = Comentario.objects.get(id=self.kwargs['pk'])
            articulo = Articulo.objects.get(id=comentario.articulo.id)
        except Exception as e:
            raise Error(str(e))
        
        if comentario.usuario.id == user_token or articulo.usuario.id == user_token:
            comentario.delete()
        else:
            raise Error("No tiene permiso para eliminar el comentario")
        
        return JsonResponse({'mensaje':'Comentario eliminado'})        


# Hacer que solamente el creador pueda eliminar, editar un post