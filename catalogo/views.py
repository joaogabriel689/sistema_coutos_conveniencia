from django.shortcuts import render, get_object_or_404
from catalogo.models import Produto, Categoria


def index(request):
    products_principal = Produto.objects.filter(destaque=False, ativo=True)
    products_promotion = Produto.objects.filter(promocao=True, ativo=True)

    context = {
        "products_principal": products_principal,
        "products_promotion": products_promotion
    }
    return render(request, 'catalogo/index.html', context)


def produto_detalhe(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id, ativo=True)

    return render(
        request,
        'catalogo/product.html',
        {"product": produto}
    )


def list_produtos(request):
    list_categorys = Categoria.objects.all()
    list_products = Produto.objects.filter(ativo=True)

    category = request.GET.get("category")

    if category:
        list_products = list_products.filter(
            categoria__id=category
        )

    context = {
        'list_categorys': list_categorys,
        'list_products': list_products
    }

    return render(request, 'catalogo/list_produtos.html', context)



def contact(request):
    return render(request, "catalogo/contact.html")


def promocao_lista(request):
    produtos_promocao = Produto.objects.filter(promocao=True, ativo=True)
    return render(
        request,
        'catalogo/promocao_lista.html',
        {"produtos": produtos_promocao}
    )
