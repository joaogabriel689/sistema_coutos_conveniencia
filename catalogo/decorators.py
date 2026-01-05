from .models import Produto
from django.db.models import F

def aumentarclick(function, id):
    Produto.objects.filter(id=id).update(
        cliques=F('cliques') + 1
    )
    return function
