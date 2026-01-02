from django.test import TestCase
from catalogo.models import Categoria, Produto


class ProdutoModelTest(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Bebidas")

    def test_criacao_produto(self):
        produto = Produto.objects.create(
            nome="Coca-Cola",
            descricao="Refrigerante",
            preco=7.50,
            categoria=self.categoria,
            ativo=True
        )

        self.assertEqual(produto.nome, "Coca-Cola")
        self.assertTrue(produto.ativo)
        self.assertEqual(produto.categoria.nome, "Bebidas")

    def test_flags_padrao(self):
        produto = Produto.objects.create(
            nome="Água",
            preco=2.00,
            categoria=self.categoria
        )

        self.assertFalse(produto.destaque)
        self.assertFalse(produto.promocao)
        self.assertTrue(produto.ativo)
