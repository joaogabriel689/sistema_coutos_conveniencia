from django.test import TestCase
from django.urls import reverse
from catalogo.models import Categoria, Produto


class ProdutoFiltroTest(TestCase):

    def setUp(self):
        self.cat_bebidas = Categoria.objects.create(nome="Bebidas")
        self.cat_doces = Categoria.objects.create(nome="Doces")

        Produto.objects.create(
            nome="Coca-Cola",
            preco=7.50,
            categoria=self.cat_bebidas,
            ativo=True
        )

        Produto.objects.create(
            nome="Chocolate",
            preco=5.00,
            categoria=self.cat_doces,
            ativo=True
        )

    def test_filtro_por_categoria(self):
        response = self.client.get(
            reverse("list_produtos"),
            {"category": self.cat_bebidas.id}
        )

        self.assertContains(response, "Coca-Cola")
        self.assertNotContains(response, "Chocolate")

    def test_categoria_inexistente(self):
        response = self.client.get(
            reverse("list_produtos"),
            {"category": 999}
        )

        self.assertEqual(response.status_code, 200)
