from django.urls import path
from .views import *

urlpatterns = [
    ############### Articulo #################
    path('crear/', ArticuloCreateApiView.as_view()),
    path('listar/', ArticuloListApiView.as_view()),
    path('editar/<int:pk>', ArticuloUpdateApiView.as_view()),
    path('eliminar/<int:pk>',ArticuloDeleteApiView.as_view()),
    path('ver/<int:pk>', ArticuloRetiveApiView.as_view()),

    ############### Comentario #################
    path('crear-comentario/', ComentarioCreateApiView.as_view()),
    path('editar-comentario/<int:pk>', ComentarioUpdateApiView.as_view()),
    path('eliminar-comentario/<int:pk>', ComentarioDeleteApiView.as_view()),
    
]