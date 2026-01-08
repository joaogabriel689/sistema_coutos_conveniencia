
# catalogo/admin.py
from django.contrib import admin
from .models import Produto, Categoria, SubCategoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)

@admin.register(SubCategoria)
class SubCategorisAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria")

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "preco", "ativo", "destaque")
    list_filter = ("categoria", "ativo", "destaque", "promocao")
    search_fields = ("nome",)