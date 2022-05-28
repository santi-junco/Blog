from rest_framework_simplejwt import views, serializers
from rest_framework.response import Response
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