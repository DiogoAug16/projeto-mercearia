from django.shortcuts import redirect, render

from carrinho.models import CarItem, Carrinho
from produtos.models import Produto

def getCarId(request):
    carSession = request.session.session_key
    if not carSession:
        carSession = request.session.create()
    return carSession

# Create your views here.
def visualizarCarrinho(request):
    return render(request, 'loja/carrinho.html')

def adicionarItemCarrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    try:
        carrinho = Carrinho.objects.get(car_id = getCarId(request))
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(
            car_id = getCarId(request)
        )
    carrinho.save()

    try:
        car_item = CarItem.objects.get(produto=produto, carrinho=carrinho)
        car_item.quantidade =+ 1
        car_item.save()
    except CarItem.DoesNotExist:
        car_item = CarItem.objects.create(
            produto = produto,
            quantidade = 1,
            carrinho = carrinho,
        )
        car_item.save()
    return redirect('carrinho')