
# catalogo/admin.py
from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "preco", "ativo", "destaque")
    list_filter = ("categoria", "ativo", "destaque", "promocao")
    search_fields = ("nome",)