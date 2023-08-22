from django.http import HttpResponse
from django.shortcuts import render
from burguer.models import Produto
def home(request):
    return render(request,'burguer/home.html')

def detalhe_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    context = {
        'produto': produto
    }
    return render(request, 'buguer/produto.html', context)
