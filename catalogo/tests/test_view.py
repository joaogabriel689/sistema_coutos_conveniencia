from django.test import TestCase
from django.urls import reverse
from catalogo.models import Categoria, Produto


class ViewsTest(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Bebidas")
        self.produto = Produto.objects.create(
            nome="Coca-Cola",
            preco=7.50,
            categoria=self.categoria,
            destaque=True,
            promocao=True,
            ativo=True
        )

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Coca-Cola")

    def test_lista_produtos_view(self):
        response = self.client.get(reverse("list_produtos"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Coca-Cola")

    def test_produto_detalhe_view(self):
        response = self.client.get(
            reverse("produto_detalhe", args=[self.produto.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Coca-Cola")

    def test_contact_view(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
