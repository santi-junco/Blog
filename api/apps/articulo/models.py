from django.db import models
from django.core.validators import FileExtensionValidator
from apps.usuario.models import Usuario
from apps.core.models import RelacionArticuloUsuario

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
    
    def cant_comentario(self, id_articulo):
        coment = Comentario.objects.filter(articulo=id_articulo).count()
        return coment
    
    def cant_likes(self, id_articulo):
        likes = Likes.objects.filter(articulo=id_articulo).count()
        return likes

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'articulo_Articulo'
        verbose_name_plural = 'Articulos'

class Imagenes(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=False)
    imagen = models.FileField(null=False, upload_to='imagen/', validators=[FileExtensionValidator(['jpg','jpeg','PNG'])])

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'articulo_imagenes'
        verbose_name_plural = 'Imagenes'

class Comentario(RelacionArticuloUsuario):
    comentario = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'articulo_comentario'
        verbose_name_plural = 'Comentarios'

class Likes(RelacionArticuloUsuario):

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'articulo_like'
        verbose_name_plural = 'Likes'