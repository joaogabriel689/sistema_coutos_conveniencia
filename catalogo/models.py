from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    imagem = models.ImageField(
        upload_to='/',
        blank=True,
        null=True
    )
    
    destaque = models.BooleanField(default=False)
    promocao = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    cliques = models.PositiveIntegerField(default=0)

    whatsapp = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.nome
