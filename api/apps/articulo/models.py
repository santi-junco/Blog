from django.db import models
from django.core.validators import FileExtensionValidator
from apps.usuario.models import Usuario

CATEGORIA_CHOICES = (
    ('Deporte','Deporte'),
    ('Cientifico','Cientifico'),
    ('Ciencia y Tecnologia','Ciencia y Tecnologia'),
    ('Musica','Musica'),
    ('Arte','Arte'),
    ('Entretenimiento','Entretenimiento'),
    ('Opinion','Opinion')
)

class Articulo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    titulo = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.CharField(max_length=300, null=False, blank=False)
    texto = models.TextField(null=False, blank=False)
    categoria = models.CharField(max_length=50, null=False, choices=CATEGORIA_CHOICES)
    estado = models.BooleanField(default=True)
    creado = models.DateField(auto_now=True)


class Imagenes(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=False)
    imagen = models.FileField(null=False, upload_to='imagen/', validators=[FileExtensionValidator(['jpg','jpeg','PNG'])])

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    comentario = models.TextField(null=False, blank=False)