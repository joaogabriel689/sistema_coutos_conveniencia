from django.db import models
import requests


def imagem_valida(url):
        if not url:
            return False

        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            return (
                response.status_code == 200 and
                response.headers.get("Content-Type", "").startswith("image/")
            )
        except requests.RequestException:
            return False
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome

class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.TextField(max_length=100)
    imagem = models.TextField(max_length=255, null=True, blank=True)

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete= models.CASCADE, null=True, blank=True)
    
    imagem = models.TextField(max_length=255, null= True, blank=True)
    
    destaque = models.BooleanField(default=False)
    promocao = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    cliques = models.PositiveIntegerField(default=0)

    whatsapp = models.PositiveIntegerField(default=0)





    @property
    def imagem_final(self):
        if imagem_valida(self.imagem):
            return self.imagem

        if self.subcategoria and imagem_valida(self.subcategoria.imagem):
            return self.subcategoria.imagem

        if self.categoria and imagem_valida(self.categoria.imagem):
            return self.categoria.imagem

        return "https://github.com/joaogabriel689/sistema_coutos_conveniencia/blob/production/media/categorias/geral_tG66OXI.png?raw=true"


    def __str__(self):
        return self.nome
