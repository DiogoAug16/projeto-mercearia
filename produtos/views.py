from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from categoria.models import Categoria
from produtos.models import Produto

# Create your views here.


def visualizarLoja(request, categoria_slug=None):
    categorias = None
    produtos = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        produtos = Produto.objects.filter(categoria = categorias, esta_disponivel=True)
        prod_quant = produtos.count()
    else:
        produtos = Produto.objects.all().filter(esta_disponivel=True)
        prod_quant = produtos.count()

    context = {
        'produtos' : produtos,
        'prod_quant': prod_quant
    }

    return render(request, 'loja/loja.html', context)

def visualizarDetalheProduto(request, categoria_slug, produto_slug):
    produto = Produto.objects.get(slug = produto_slug, categoria__slug=categoria_slug)
    contexto = {
        'produto' : produto
    }

    return render(request, 'loja/produto_detalhe.html', contexto)
    