from django.db import models

class TimeStampedModel(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name=u'creado', help_text=u'Fecha de creacion')
    modificado = models.DateTimeField(auto_now=True, verbose_name=u'modificado', help_text=u'Fecha de modificaion')

    def __str__(self):
        return str(self.id)

    class Meta:
        abstract = True

class RelacionArticuloUsuario(TimeStampedModel):
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, null=False)
    articulo = models.ForeignKey('articulo.Articulo', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.id)
        
    class Meta:
        abstract = True