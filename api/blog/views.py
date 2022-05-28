from rest_framework_simplejwt import views, serializers, tokens
from rest_framework import status, generics, response
from apps.usuario.models import *

class ObtenerToken(serializers.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # no hago validaciones si esta activo o si existe porque ya los hace django
        usuario = Usuario.objects.get(email=user)
        token = super().get_token(user)
        token['nombre'] = usuario.get_full_name()
        token['email'] = usuario.email
        return token

class Login(views.TokenObtainPairView):
    serializer_class = ObtenerToken

class Logout(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        print(request.data.get('usuario',''))
        print('-'*50)
        user = Usuario.objects.filter(id=request.data.get('usuario',''))
        if user.exists():
            tokens.RefreshToken.for_user(user.first())
            return response.Response({'mensaje':'Sesion cerrada'}, status=status.HTTP_200_OK)
        return response.Response({'Error':'No se pudo cerrar sesion'}, status=status.HTTP_400_BAD_REQUEST)
