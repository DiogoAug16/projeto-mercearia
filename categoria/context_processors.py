from categoria.models import Categoria

def menu_categoria(request):
    lista_categoria = Categoria.objects.all()
    return dict(opcoes = lista_categoria)