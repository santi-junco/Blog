from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .excepciones import *
from django.contrib.auth.hashers import make_password

# Creacion de usuario
class UsuarioCreateApiView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def perform_create(self, serializer):
        try:
            nombre = self.request.data['nombre']
            apellido = self.request.data['apellido']
            email = self.request.data['email']
            password = self.request.data['password']
        except:
            raise ErrorReguistro

        usuario = serializer.save()
        # valores del registro
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.username = email
        usuario.password = make_password(password)
        # campo opcional
        usuario.userName = self.request.data.get('userName', None)
        # valores por defecto
        usuario.is_superuser = False
        usuario.is_staff = False
        usuario.is_active = False
        
        usuario.save()

        return Response({
            'status': 200,
            'mensaje': 'Usuario creado exitosamente',
            'data': usuario
        })

# Listado de usuarios
class UsuarioListApiView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Edicion de usuario
class UsuarioUpdateApiView(UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

# Eliminar usuario
class UsuairoDeleteApiView(DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

# Obtener un usuario
class UsuarioRetriveApiView(RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer