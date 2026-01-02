
from django.contrib import admin
from .models import Produto, Categoria

admin.site.register(Categoria)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria', 'ativo')