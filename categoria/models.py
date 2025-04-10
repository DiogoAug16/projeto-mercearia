from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria_nome = models.CharField(max_length=80, unique=True)
    categoria_imagem = models.ImageField(upload_to='fotos/categorias', blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    categoria_descricao = models.TextField(max_length=250, blank=True)  

    def __str__(self):
        return self.categoria_nome