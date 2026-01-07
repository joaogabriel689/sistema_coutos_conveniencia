from django.shortcuts import render, get_object_or_404, redirect
from catalogo.models import Produto, Categoria
from django.db.models import F

def index(request):
    products_principal = Produto.objects.order_by("clique").filter(ativo=True).all()[:5]
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

def aumentar_click(request, produto_id):
    Produto.objects.filter(id=produto_id).update(
        cliques=F('cliques') + 1
    )
    return redirect(produto_detalhe(request, produto_id))

def aumentar_click_whatsapp(request, produto_id):
    Produto.objects.filter(id=produto_id).update(
        cliques=F('whatsapp') + 1
    )
    produto = Produto.objects.get(id=produto_id)
    return redirect(f"https://wa.me/5567992404458?text=Olá,%20quero%20esse%20produto%20{produto.nome}")
