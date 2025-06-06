from django.db import models
from django.urls import reverse

from categoria.models import Categoria

# Create your models here.
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=210, unique=True)
    descricao = models.TextField(max_length=300)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    imposto = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    imagens = models.ImageField(upload_to='fotos/produtos', blank=True)
    estoque = models.IntegerField()
    esta_disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.produto_nome

    def get_url(self):
        return reverse('visualizarDetalheProduto', args=[self.categoria.slug, self.slug])